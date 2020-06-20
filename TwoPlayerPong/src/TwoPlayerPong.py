from random import choice, uniform
from math import sin, cos, radians
from TwoPlayerPong.src import settings

import arcade


class PongApplication(arcade.Window):
    def __init__(self):
        super().__init__(settings.WINDOW_SIZE[0], settings.WINDOW_SIZE[1], settings.WINDOW_TITLE)
        self.ball_pos = settings.BALL_INIT_POS
        self.ball_step = [0, 0]  # [x, y]
        self.ball_vel = 3
        self.ball_deg = 0
        self.paddle_pos_1 = settings.PADDLE_INIT_POS_1
        self.paddle_pos_2 = settings.PADDLE_INIT_POS_2

        self.up1 = self.up2 = self.down1 = self.down2 = 0

        self.p1_score = self.p2_score = 0

        self.winning_side = choice((1, 2))

        self.playing_the_game = 0

        self.ticks = 0

    # Logic -----
    def paddle_movement(self):
        if self.up1:
            self.paddle_pos_1[1] += settings.PADDLE_MOVE_SPEED

        if self.down1:
            self.paddle_pos_1[1] -= settings.PADDLE_MOVE_SPEED

        if self.up2:
            self.paddle_pos_2[1] += settings.PADDLE_MOVE_SPEED

        if self.down2:
            self.paddle_pos_2[1] -= settings.PADDLE_MOVE_SPEED

    def render_paddle(self):
        arcade.draw_rectangle_filled(
            center_x=self.paddle_pos_1[0], center_y=self.paddle_pos_1[1],
            width=settings.PADDLE_SIZE[0], height=settings.PADDLE_SIZE[1],
            color=settings.PADDLE_COL
        )

        arcade.draw_rectangle_filled(
            center_x=self.paddle_pos_2[0], center_y=self.paddle_pos_2[1],
            width=settings.PADDLE_SIZE[0], height=settings.PADDLE_SIZE[1],
            color=settings.PADDLE_COL
        )

    def ball_movement(self):
        if self.ball_step == [0, 0]:  # Check if moving first
            if self.winning_side == 1:
                self.ball_deg = uniform(-45, 45)

            elif self.winning_side == 2:
                self.ball_deg = uniform(135, 225)

            self.ball_step = [cos(radians(self.ball_deg)), sin(radians(self.ball_deg))]

        self.ball_pos[0] += self.ball_step[0] * self.ball_vel
        self.ball_pos[1] += self.ball_step[1] * self.ball_vel

        # Collision with sides
        if self.ball_pos[1] + settings.BALL_RADIUS >= settings.WINDOW_SIZE[1] or self.ball_pos[1] - settings.BALL_RADIUS <= 0:
            self.ball_step[1] *= -1

        # Collision with paddles
        collision_1 = self.ball_pos[0] - settings.BALL_RADIUS <= self.paddle_pos_1[0] and self.paddle_pos_1[1] - \
                      settings.PADDLE_SIZE[1] <= self.ball_pos[1] <= self.paddle_pos_1[1] + settings.PADDLE_SIZE[1]

        collision_2 = self.ball_pos[0] + settings.BALL_RADIUS >= self.paddle_pos_2[0] and self.paddle_pos_2[1] - \
                      settings.PADDLE_SIZE[1] <= self.ball_pos[1] <= self.paddle_pos_2[1] + settings.PADDLE_SIZE[1]

        if collision_1 or collision_2:
            self.ball_step[0] *= -1

    def difficulty(self):
        if self.ticks % settings.PROGRESSION_ADVANCE_INTERVAL == 0 and self.ball_vel < settings.MAX_BALL_SPEED:
            self.ball_vel += 1

    def render_ball(self):
        arcade.draw_circle_filled(self.ball_pos[0], self.ball_pos[1], settings.BALL_RADIUS, settings.BALL_COL)

    def draw_score(self):
        arcade.draw_text(
            str(self.p1_score),
            settings.WINDOW_SIZE[0] / 4,
            settings.WINDOW_SIZE[1] - 1.5 * settings.SCORE_SIZE,
            settings.SCORE_COL,
            settings.SCORE_SIZE,
            font_name=settings.SCORE_FONT,
            bold=True
        )

        arcade.draw_text(
            str(self.p2_score),
            settings.WINDOW_SIZE[0] - settings.WINDOW_SIZE[0] / 4,
            settings.WINDOW_SIZE[1] - 1.5 * settings.SCORE_SIZE,
            settings.SCORE_COL,
            settings.SCORE_SIZE,
            font_name=settings.SCORE_FONT,
            bold=True
        )

    def reset(self):
        self.ball_step = [0, 0]
        self.ball_pos = [500, 375]
        self.playing_the_game = 0

        self.paddle_pos_1 = settings.PADDLE_INIT_POS_1
        self.paddle_pos_2 = settings.PADDLE_INIT_POS_2

    def detect_win(self):
        if self.ball_pos[0] < 0:
            self.p2_score += 1
            self.winning_side = 2
            self.reset()

        elif self.ball_pos[0] > settings.WINDOW_SIZE[0]:
            self.p1_score += 1
            self.winning_side = 1
            self.reset()

    # Loop -----
    def on_draw(self):
        """Rendering"""
        arcade.start_render()
        self.render_ball()
        self.render_paddle()
        self.draw_score()

    def on_update(self, delta_time: float):
        """Logic"""
        self.paddle_movement()

        if self.playing_the_game:
            self.ball_movement()
            self.detect_win()
            self.difficulty()

        self.ticks += 1

    # Control -----
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == settings.KEY_SET_1[0]:
            self.up1 = 1

        elif symbol == settings.KEY_SET_1[1]:
            self.down1 = 1

        elif symbol == settings.KEY_SET_2[0]:
            self.up2 = 1

        elif symbol == settings.KEY_SET_2[1]:
            self.down2 = 1

        elif symbol == settings.START_KEY:
            self.playing_the_game = 1

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == settings.KEY_SET_1[0]:
            self.up1 = 0

        elif symbol == settings.KEY_SET_1[1]:
            self.down1 = 0

        elif symbol == settings.KEY_SET_2[0]:
            self.up2 = 0

        elif symbol == settings.KEY_SET_2[1]:
            self.down2 = 0


if __name__ == '__main__':
    PongApplication()
    arcade.run()

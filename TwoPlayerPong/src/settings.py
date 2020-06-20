from arcade import key, color

WINDOW_SIZE = [1000, 750]
WINDOW_TITLE = 'Two Player Pong'

BALL_INIT_POS = [WINDOW_SIZE[0] / 2, WINDOW_SIZE[1] / 2]
BALL_RADIUS = 10
BALL_COL = color.WHITE
MAX_BALL_SPEED = 20  # Don't want the ball to phase through the paddles at light speed

PADDLE_SIZE = [20, 120]
PADDLE_COL = color.WHITE
PADDLE_INIT_POS_1 = [PADDLE_SIZE[0] / 2, WINDOW_SIZE[1] / 2]
PADDLE_INIT_POS_2 = [WINDOW_SIZE[0] - PADDLE_SIZE[0] / 2, WINDOW_SIZE[1] / 2]

PADDLE_MOVE_SPEED = 5

KEY_SET_1 = [key.W, key.S]  # [Up, Down]
KEY_SET_2 = [key.UP, key.DOWN]
START_KEY = key.SPACE

SCORE_COL = color.WHITE
SCORE_SIZE = 50
SCORE_FONT = 'Calibri'

PROGRESSION_ADVANCE_INTERVAL = 200

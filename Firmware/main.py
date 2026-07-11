import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (board.D7, board.D8, board.D9, board.D6)        # D7 D8, D9, D6
keyboard.row_pins = (board.D10, board.D0, board.D2, board.D3)       # D10, D0, D2, D3
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.N1, KC.N2, KC.N3,KC.KP_PLUS,
    KC.N4, KC.N5, KC.N6, KC.KP_MINUS,
    KC.N7, KC.N8, KC.N9, KC.KP_ASTERISK,
    KC.N0, KC.KP_DOT, KC.ENTER, KC.KP_SLASH
    ]
]

if __name__ == "__main__":
    keyboard.go()
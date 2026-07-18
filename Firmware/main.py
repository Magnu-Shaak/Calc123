import board                                        # Board
from oled_extention import init_oled                # Oled Display
from kmk.kmk_keyboard import KMKKeyboard            # Keys
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers               # Layer toggle
from kmk.modules.combos import Combos, Chord, Sequence
from kmk.modules.dynamic_sequences import DynamicSequences      #Dynamic Sequences
from kmk.modules.tapdance import TapDance
from kmk.extensions.media_keys import MediaKeys


#Initialize
keyboard = KMKKeyboard()
combos = Combos()
tapdance = TapDance()
keyboard.modules.append(Layers())
keyboard.modules.append(combos)
keyboard.modules.append(DynamicSequences())
keyboard.extensions.append(MediaKeys())
keyboard.modules.append(tapdance)
tapdance.tap_time = 750

#OLED Display
layer_names_map = {
    0: "Numpad",
    1: "Functions",
}
init_oled (keyboard, layer_names_map, board.D5, board.D4, 0x3C, 32, 128)

#Combos
combos.combos = [
    Chord((KC.KP_PLUS, KC.KP_MINUS), KC.TG(1)),
    Chord((KC.KP_Asterisk, KC.KP_SLASH), KC.TO(0)),
#    Chrod((KC.KC_PLUS, KC_ASRERISK), KC.TG(2))
]
Record = KC.TD(KC.PLAY_SEQUENCE, KC.RECORD_SEQUENCE(), KC.STOP_SEQUENCE())
Paste = KC.TD(KC.LCTL(KC.V),KC.LCTL(KC.LSFT(KC.V)))
Multiply = KC.TD(KC.ASTR, KC.CIRC)
Divide = KC.TD(KC.KP_SLASH, KC.PERC, KC.PIPE)


#Keyboard Layout
keyboard.col_pins = (board.D7, board.D8, board.D9, board.D6)        # D7 D8, D9, D6
keyboard.row_pins = (board.D10, board.D0, board.D2, board.D3)       # D10, D0, D2, D3
keyboard.diode_orientation = DiodeOrientation.COL2ROW


keyboard.keymap = [
    [
        KC.N1, KC.N2, KC.N3, KC.KP_PLUS,
        KC.N4, KC.N5, KC.N6, KC.KP_MINUS,
        KC.N7, KC.N8, KC.N9, Multiply,
        KC.N0, KC.KP_DOT, KC.LT(1,KC.ENTER), Divide,
    ],
    [
        KC.LCTL(KC.C), Paste, KC.LALT(KC.TAB), KC.TRNS,
        KC.LCTL(KC.Z), KC.LCTL(KC.Y), KC.LCTL(KC.BSLASH), KC.TRNS,
        KC.LCTL(KC.W), KC.LCTL(KC.LSFT(KC.T)), KC.LCTL(KC.T), KC.TRNS,
        KC.VOLU, KC.VOLD, Record, KC.TRNS,
    ],
]
#       Copy, Paste, Swich Tap 
#       Undo, Redo, Sp. Format
#       Close, Reopen, New Tab
#       Vol UP, Vol DN, Dynamic

if __name__ == "__main__":
    keyboard.go()
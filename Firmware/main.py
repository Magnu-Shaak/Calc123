import Firmware.board as board                      # Board
from kmk.kmk_keyboard import KMKKeyboard            # Keys
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
import busio                                        # OLED
from kmk.extensions.display import Display, TextEntry, ImageEntry
from kmk.extensions.display.ssd1306 import SSD1306
from kmk.modules.layers import Layers               # Layer toggle
from kmk.modules.combos import Combos, Chord, Sequence
from kmk.modules.dynamic_sequences import DynamicSequences      #Dynamic Sequences
from kmk.modules.tapdance import TapDance


#Initialize
keyboard = KMKKeyboard()
keyboard.modules.append(Layers())
combos = Combos()
keyboard.modules.append(combos)
keyboard.modules.append(DynamicSequences())
tapdance = TapDance()
keyboard.modules.append(tapdance)
tapdance.tap_time = 750


#OLED
i2c_bus = busio.I2C(board.D5, board.D4)     # D4 - SDA, D5 - SCL
driver = SSD1306(
    i2c = i2c_bus,
)
display = Display(
    display=driver,
    width=128,
    height=32,
    flip = False, 
    brightness=0.8,
    brightness_step=0.1,
)
#Combos
combos.combos = [
    Chord((KC.KP_PLUS, KC.KP_MINUS), KC.TG(1)),
    Chord((KC.KP_Asterisk, KC.KP_SLASH), KC.TO(0)),
    Chord(KC.KP_Plus, KC.LCTL(KC.LSFT(KC.V)),KC.RECORD_SEQUENCE),
#    Chrod((KC.KC_PLUS, KC_ASRERISK), KC.TG(2))
]
Record = KC.TD(KC.PLAY_SEQUENCE, KC.RECORD_SEQUENCE(), KC.STOP_SEQUENCE())

#Keyboard Layout
keyboard.col_pins = (board.D7, board.D8, board.D9, board.D6)        # D7 D8, D9, D6
keyboard.row_pins = (board.D10, board.D0, board.D2, board.D3)       # D10, D0, D2, D3
keyboard.diode_orientation = DiodeOrientation.COL2ROW


keyboard.keymap = [
    [
        KC.N1, KC.N2, KC.N3,KC.KP_PLUS,
        KC.N4, KC.N5, KC.N6, KC.KP_MINUS,
        KC.N7, KC.N8, KC.N9, KC.KP_ASTERISK,
        KC.N0, KC.KP_DOT, KC.LT(1,KC.ENTER), KC.KP_SLASH,
    ],
    [
        KC.LCTL(KC.C), KC.LCTL(KC.V), KC.LCTL(KC.LSFT(KC.V)), KC.TRNS,
        KC.LCTL(KC.Z), KC.LCTL(KC.Y), KC.LCTL(KC.BSLASH), KC.TRNS,
        KC.LCTL(KC.W), KC.LCTL(KC.LSFT(KC.T)), KC.LCTL(KC.W), KC.TRNS,
        KC.LCTL(KC.LSFT(KC.F5)), KC.LCTL(KC.K), Record, KC.TRNS,
    ],
]

if __name__ == "__main__":

    print("started")
    keyboard.go()
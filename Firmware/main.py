import Firmware.board as board                      # Board
from kmk.kmk_keyboard import KMKKeyboard            # Keys
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
import busio                                        # OLED
from kmk.extensions.display import Display, TextEntry, ImageEntry
from kmk.extensions.display.ssd1306 import SSD1306
from kmk.modules.layers import Layers               # Layer toggle
from kmk.modules.combos import Combos, Chord, Sequence


#Initialize
keyboard = KMKKeyboard()
layers = Layers()
keyboard.modules.append(layers)
combos = Combos()
keyboard.modules.append(combos)

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
#Change Layers
combos.combos = [
    Chord((KC.KP_PLUS, KC.KP_MINUS), KC.TG(1))
    Chord((KC.KP_Dot, KC.KP_SLASH), KC.TO(0))
]
#Keyboard Layout
keyboard.col_pins = (board.D7, board.D8, board.D9, board.D6)        # D7 D8, D9, D6
keyboard.row_pins = (board.D10, board.D0, board.D2, board.D3)       # D10, D0, D2, D3
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [
    KC.N1, KC.N2, KC.N3,KC.KP_PLUS,
    KC.N4, KC.N5, KC.N6, KC.KP_MINUS,
    KC.N7, KC.N8, KC.N9, KC.KP_ASTERISK,
    KC.N0, KC.KP_DOT, KC.LT(1,KC.ENTER), KC.KP_SLASH
    ]
    [
    
    ]
]

if __name__ == "__main__":

    print("started")
    keyboard.go()
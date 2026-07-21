import board                                        # Board
from oled_extension import init_oled                # Oled Display
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

# OLED Display
layer_names_map = {
    0: "Numpad",
    1: "Functions",
}
init_oled (
    keyboard, layer_names_map, board.D5, board.D4, 0x3C, 32, 128)

# Local Calculator
import math                     # TO_DO: ADD DOT, CLEAR, BSPACE,
og_process_key = keyboard.process_key

keyboard.calc_state = {
    "raw_str": "",
    "answer": "",
    "operator": "",
    "is_active": False,   
}
state = keyboard.calc_state
operator_list = {
    "KC.KP_PLUS": "+",
    "KC.KP_MINUS": "-",
    "KC.KP_ASTERISK": "*",
    "KC.KP_SLASH": "/",
    }
other_symbols_list = {
    "KC.ENTER": "=",
#    "KC.DOT": ".",
}

def clear():
    state["raw_str"] = ""
    state["operator"] = ""
    state["answer"] = ""

def running_total(kmk_name):
    if "=" in state["raw_str"] or "Error" in state["raw_str"]:
        if kmk_name in operator_list.keys():
            state["raw_str"] = state["answer"]
            state["operator"] = ""
        else: clear()

def calculator(operator, a, b):
    try:
        if operator == "+":
            return (a + b)
        elif operator == "-":
            return (a - b)
        elif operator == "*":
            return (a * b)
        elif operator == "^":
            return (a ** b)
        elif operator == "/":
            if b == "0": return "Error: Div by 0"
            return (a / b)
        elif operator == "%":
            return (a % b)
        elif operator == "|":
            if b == "0": return "Error: Div by 0"
            return (a // b)
        else:
            return "Error"
    except Exception:
        return "Error"
    
def calc_interpreter(key, is_pressed, coordinate):         #Interprites KMK into str for processor
    if not state["is_active"]:
        return og_process_key(key, is_pressed, coordinate)
    
    val = None
    keyboard.modules.layers.activate_layer(0)
    if is_pressed:
        kmk_name = str(key)

        running_total(kmk_name)

        if "KC.LT" in kmk_name and "KC.ENTER" in kmk_name:
            kmk_name = "KC.ENTER"

        if "KC.N" in kmk_name:
            val = kmk_name.split("KC.N")[-1]
#        elif KC.KP in kmk_name:
#            val = kmk_name.split("KC.KP_")[-1]
        elif kmk_name in operator_list.keys():
            if state["operator"]:                   # Multiple Operater Check
                return None
            val = operator_list.get(kmk_name)
            state["operator"] = val
        elif kmk_name in other_symbols_list.keys():
            val = other_symbols_list.get(kmk_name)
        else:
            return None
    
    if val is None: return None
    elif val == "=":                      # Send forward
        if not state["operator"] or state["operator"] not in state["raw_str"]:
            clear()
            return None
        
        str_a, operator, str_b = state["raw_str"].partition(state["operator"])
        if not str_b: return None
        a = float(str_a) if "." in str_a else int(str_a)
        b = float(str_b) if "." in str_b else int(str_b)
        result = calculator(operator, a, b)

        if isinstance(result, str) and "Error" in result:
            clear()
            state["raw_str"] = "Error"
            return None
        
        elif isinstance(result, float) and result.is_integer():
            result = int(result)

        state["answer"] = str(result)
        state["raw_str"] += val
        state["raw_str"] += str(result)
        state["operator"] = ""

        return None


    state["raw_str"] += val
    return None

keyboard.process_key = calc_interpreter
# Combos
combos.combos = [
    Chord((KC.KP_PLUS, KC.KP_MINUS), KC.TG(1)),
#    Chord((KC.KC_PLUS, KC_ASRERISK), KC.TG(2))
    Chord((KC.KP_ASTERISK, KC.KP_SLASH), KC.TO(0)),

]
Record = KC.TD(KC.PLAY_SEQUENCE, KC.RECORD_SEQUENCE(), KC.STOP_SEQUENCE())
Paste = KC.TD(KC.LCTL(KC.V),KC.LCTL(KC.LSFT(KC.V)))
# Multiply = KC.TD(KC.ASTR, KC.CIRC)
# Divide = KC.TD(KC.KP_SLASH, KC.PERC, KC.PIPE)


#Keyboard Layout
keyboard.col_pins = (board.D7, board.D8, board.D9, board.D6)        # D7 D8, D9, D6
keyboard.row_pins = (board.D10, board.D0, board.D2, board.D3)       # D10, D0, D2, D3
keyboard.diode_orientation = DiodeOrientation.COL2ROW


keyboard.keymap = [         # Maybe add another layer for Calculator active? 
    [
        KC.N1, KC.N2, KC.N3, KC.KP_PLUS,
        KC.N4, KC.N5, KC.N6, KC.KP_MINUS,
        KC.N7, KC.N8, KC.N9, KC.ASTR,
        KC.N0, KC.KP_DOT, KC.LT(1,KC.ENTER), KC.KP_SLASH,
    ],
    [
        KC.LCTL(KC.C), Paste, KC.LALT(KC.TAB), KC.TRNS,
        KC.LCTL(KC.Z), KC.LCTL(KC.Y), KC.LCTL(KC.BSLASH), KC.TRNS,
        KC.LCTL(KC.W), KC.LCTL(KC.LSFT(KC.T)), KC.LCTL(KC.T), KC.TRNS,
        KC.VOLU, KC.VOLD, Record, KC.TRNS,
    ],
]
#       Copy, Paste, Switch Tap 
#       Undo, Redo, Sp. Format
#       Close, Reopen, New Tab
#       Vol UP, Vol DN, Dynamic

if __name__ == "__main__":
    keyboard.go()
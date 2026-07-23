import board                                        # Board
from oled_extension import init_oled                # Oled Display
from kmk.kmk_keyboard import KMKKeyboard            # Keys
from kmk.keys import KC, Key
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

class RemoverKeys(Key):
    def __init__(self, key, **kwargs):
        super().__init__(**kwargs)
        self.name = self.name
    def __str__(self): return self.name
    def __repr__(self): return self.__str__()

Clear = RemoverKeys("KC.CLEAR")
Backspace = RemoverKeys("KC.BACKSPACE")

keyboard.calc_state = {
    "raw_str": "",
    "answer": "",
    "operator": "",
    "a": "",
    "b": "",
    "is_active": False,   
}
state = keyboard.calc_state
operator_list = {
    "KC.KP_PLUS": "+",
    "KC.KP_MINUS": "-",
    "KC.KP_ASTERISK": "*",
    "KC.KP_SLASH": "/",
    "KC.CIRCUMFLEX": "**",
    "KC.PERCENT": "%",
    "KC.PIPE": "//",
    }
other_symbols_list = {
    "KC.ENTER": "=",
    "KC.DOT": ".",
    "KC.CLEAR": "",
    "KC.BACKSPACE": "",
}

def clear():
    state["raw_str"] = ""
    state["operator"] = ""
    state["answer"] = ""
    state["a"] = ""
    state["b"] = ""

def running_total(kmk_name):
    if "=" in state["raw_str"]:
        if kmk_name in operator_list:
            state["a"] = state["answer"]
            state["raw_str"] = state["answer"]
            state["operator"] = ""
        else: clear()

def calculator(operator, a, b):
    try:
        ans = eval(state["raw_str"])
        return ans
    except Exception:
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
            if b == "0": return "Error: Div by 0"
            return (a % b)
        elif operator == "|":
            if b == "0": return "Error: Div by 0"
            return (a // b)
        else:
            return "Error"

def calc_interpreter(key, is_pressed, coordinate=None):         #Interprites KMK imputs for the calculator function
    if not state["is_active"]:
        return og_process_key(key, is_pressed, coordinate=None)
    
    val = None
    keyboard.modules.layers.activate_layer(0)
    if is_pressed:
        if "Error" in state["raw_str"]: clear()

        kmk_name = str(key)
        running_total(kmk_name)

        if "KC.ENTER" in kmk_name: kmk_name = "KC.ENTER"

        if "KC.N" in kmk_name:
            val = kmk_name.split("KC.N")[-1]
#        elif KC.KP in kmk_name:
#            val = kmk_name.split("KC.KP_")[-1]
        elif kmk_name in operator_list:
            if state["operator"]:                   # Multiple Operater Check
                return None
            val = operator_list.get(kmk_name)
            state["operator"] = val
        elif kmk_name in other_symbols_list:        # Duplicates checks, depends on symbol
            if kmk_name == "KC.Dot":
                # If no operator(so a) and decimal, --OR-- If operator (so b) and  decimal [ie. Invalid Inputs]
                if (not state["operator"] and "." in state["a"]) or (state["operator"] and "." not in state["b"]):
                    return None     # Don't add decimal
                pass
            elif kmk_name == "KC.ENTER":    # If "=" alr there and another abt to be entered
                if "=" in state["raw_str"]:
                    return None
                pass
            elif kmk_name == "KC.CLEAR":            # Remover Keys checks 
                clear()
                return None
            elif kmk_name == "KC.BACKSPACE":
                state["raw_str"] = state["raw_str"][:-1]
            else: return None
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
    if state["operator"]:   # and state["operator"] in state["raw_str"]
        state["a"], state[operator], state["b"] = state["raw_str"].partition(state["operator"])
    else:
        state["a"] = state["raw_str"]
    
    return None

keyboard.process_key = calc_interpreter

# Combos
combos.combos = [
    Chord((KC.KP_DOT, KC.KP_PLUS), KC.TG(1)),      # Toggles
    Chord((KC.KP_VOLD, KC.KP_PLUS), KC.TG(1)),
    Chord((KC.KP_PLUS, KC.KP_MINUS), KC.TG(0)),
    Chord((KC.KP_PLUS, KC.ASTR), KC.CIRC),           # Operators
    Chord((KC.KP_PLUS, KC.KP_SLASH), KC.PERC),
    Chord((KC.KP_MINUS, KC.KP_SLASH), KC.PIPE),
]
Record = KC.TD(KC.PLAY_SEQUENCE, KC.RECORD_SEQUENCE(), KC.STOP_SEQUENCE())
Paste = KC.TD(KC.LCTL(KC.V),KC.LCTL(KC.LSFT(KC.V)))



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
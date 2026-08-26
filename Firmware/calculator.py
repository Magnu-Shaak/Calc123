from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC, Key

keyboard = KMKKeyboard()

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

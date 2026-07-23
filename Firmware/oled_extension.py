import board        # My own OLED Extention
import busio
import time
import displayio
import terminalio
import adafruit_displayio_ssd1306
from adafruit_display_text import label
from kmk.extensions import Extension
from main import calc_state
try:
    from i2cdisplaybus import I2CDisplayBus
except ImportError:
    from displayio import I2cDisplay as I2CDisplayBus

# For Displaying Layer Name
class DisplayManager(Extension):
    def __init__(self, text_target, names_dict):
        self.text_target = text_target
        self.names_dict = names_dict
        self.last_layer = None

    def after_matrix_scan(self, keyboard):
        calc_state = getattr(keyboard, "calc_state", None)
        if calc_state and calc_state.get("is_active", False):
            current_text = calc_state.get("raw_str", "") or "0"
            for op in ["+", "-", "*", "/", "**", "%", "//", "="]:
                current_text = current_text.replace(op, f" {op} ")

            if current_text != self.text_target:
                self.text_target = current_text
                return

        active_list = keyboard.active_layers
        current_layer = max(active_list) if active_list else 0
        if current_layer != self.last_layer:
            self.last_layer = current_layer
            layer_name = self.names_dict.get(current_layer, f"LAYER {current_layer}")
            self.text_target.text = layer_name


    def on_runtime_init(self, keyboard): pass
    def during_lookahead(self, keyboard, active_layers): pass
    def before_matrix_scan(self, keyboard): pass  
    def before_hid_send(self, keyboard): pass
    def after_hid_send(self, keyboard): pass

def init_oled(keyboard, layer_names_map, scl_pin, sda_pin, display_address=0x3C, display_height=32, display_width=128):
    displayio.release_displays()                    # Reset display

    i2c_bus = busio.I2C(scl_pin, sda_pin)         # Initialize display (D5 - SCL, D4 - SDA)
    display_bus = I2CDisplayBus(i2c_bus, device_address=display_address)
    display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=display_width, height=display_height)
 
    oled_group = displayio.Group()                 # Text to Bitmap engine
    display_output = label.Label(
        terminalio.FONT,
        text="Jai Swaminarayan",
        color=0xFFFFFF,
        x=0,
        y=12
    )
    oled_group.append(display_output)
    display.root_group = oled_group
    time.sleep(3.0) 

    keyboard.extensions.append(DisplayManager(display_output, layer_names_map))
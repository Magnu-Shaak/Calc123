import board        
import busio
import time
import displayio
import terminalio
import adafruit_displayio_ssd1306
from adafruit_display_text import label
from kmk.extensions import Extension
try:
    from i2cdisplaybus import I2CDisplayBus
except ImportError:
    from displayio import I2cDisplay as I2CDisplayBus

# For Displaying Layer Name
class LayerTracker(Extension):
    def __init__(self, text_target, names_dict):
        self.text_target = text_target
        self.names_dict = names_dict

    def on_layer_change(self, keyboard, layer_state):
        active_list = keyboard.active_layers
        if active_list:
            current_layer = max(active_list)
        else:
            current_layer = 0
        layer_name = self.names_dict.get(current_layer, f"LAYER {current_layer}")
        self.text_target.text = layer_name

    def on_runtime_init(self, keyboard): pass
    def during_lookahead(self, keyboard, active_layers): pass
    def before_matrix_scan(self, keyboard): pass  
    def after_matrix_scan(self, keyboard): pass
    def before_hid_send(self, keyboard): pass
    def after_hid_send(self, keyboard): pass

def init_oled(keyboard, layer_names_map, scl_pin, sda_pin, display_address=0x3C, display_hight=32, display_width=128):
    displayio.release_displays()                    # Reset display

    i2c_bus = busio.I2C(scl_pin, sda_pin)         # Initialize display (D5 - SCL, D4 - SDA)
    display_bus = I2CDisplayBus(i2c_bus, device_address=display_address)
    display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=display_width, height=display_hight)
 
    oled_group = displayio.Group()                 # Text to Bitmap engine
    layer_label = label.Label(
        terminalio.FONT,
        text="Initializing",
        color=0xFFFFFF,
        x=0,
        y=12
    )
    oled_group.append(layer_label)
    display.root_group = oled_group
    time.sleep(3.0) 

    keyboard.extensions.append(LayerTracker(layer_label, layer_names_map))
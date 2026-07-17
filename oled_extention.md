# OLED Extention
This is my OLED extention I made in CircuitPy that is compatable to use with KMK. 
I Don't belive anyone will see this, but if you are, use the oled_extention_templete.py file. The oled_extention is configured to the board I am using.


## List of Supported features below:

Event Updating:
    Layer Changes
    
    
Display Chips:
    SSD 1306

## Configure
```python
# main.py or code.py
from oled_extention import init_oled                # Import

# Map the text displayed to layer index. If no text is defined, it defaults to "Layer x"
layer_names_map = {  # Name this whatever, just be consistant with the name in the init_oled function
    0: "Numpad",
    1: "Functions",
}

# Input your entries for each of the feilds. If no entry is added, some feilds have default values set
init_oled(keyboard, layer_names_map, scl_pin, sda_pin, display_hight=32, display_width=128, display_address=0x3C)

# For Example:
init_oled(keyboard, layer_names_map, board.D5, board.D4, 64, 128, 0x3C)
```
## Other
Comment on this Repo if you want me to add anythin. Image support and Mod Layers as events will probably be added the quickest.

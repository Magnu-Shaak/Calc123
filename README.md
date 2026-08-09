# Numpad
Making a Numpad accessory that also works as a stand-alone calculator!

Features:
- Numberpad (0-9, 4 operations,"=", ".")
    + Has a built in Local Calculator that displays on the OLED
- Custom Shortcuts Layer
- Displays Layer on OLED
    + Use it yourself: Info at [https://github.com/Magnu-Shaak/Calc123/blob/main/oled_extention.md](url)

3d render in Onshape

<img width="845" height="480" alt="image" src="https://github.com/user-attachments/assets/cdfa2535-12f6-4281-813e-846257810732" />

## BOM
- Also available at [https://github.com/Magnu-Shaak/Calc123/blob/main/bom.csv](url)
 
| Item | Quantity | Total Price | Link | Source | Notes | 
| --- | --- | --- | --- | --- | --- | 
 | PCB (5 piece) | 1 | $12.86 | https://www.pcbway.com/QuickOrderOnline.aspx | PCB way | From Actual Checkout page (Shipping DDP with Global Direct Shipping) | 
 | Devboard | 1 | $9.99 | <https://www.amazon.com/Pre-Soldered-Microcontroller-MicroPython-CircuitPython-Interfaces/dp/B09NNVNW7M> | Amazon | XIAO rp2040  | 
 | 1N4148 THT Diodes (100 piece) | 1 | $0.99 | https://www.aliexpress.us/item/3256809192784213.html | AliExpress Choice | Lowest Price Option* | 
 | Cherry MX Switches (10 piece) | 2  | $0.99 | https://www.aliexpress.us/item/3256807705085808.html | AliExpress Choice | "Limit 1 per color:1 white | 1 silver" | 
 | 0.91 in. OLED (5 piece) | 1 | $0.99 | https://www.aliexpress.us/item/3256808453793642.html | AliExpress Choice | Lowest Price Option* | 
 | White Keycaps (50 piece; white) | 1 | $0.99 | https://www.aliexpress.us/item/3256810533781399.html | AliExpress Choice | Lowest Price Option* | 
 | M3x16mm Screws (100 piece) | 1 | $0.99 | https://www.aliexpress.us/item/2255800046543591.html | AliExpress Choice | Lowest Price Option* | 
 | M3x5mmx4mm heatset Inserts (100 piece) | 1 | $0.99 | https://www.aliexpress.us/item/2255800046543591.html | AliExpress Choice | Lowest Price Option* | 
 | Case | 1 | $3.50 | Local Library | Local Library | $0.05 per gram | 
 | Soldering Irorn | 1 | $39.99 | https://www.amazon.com/PINECIL-Smart-Mini-Portable-Soldering/dp/B096X6SG13 | Amazon | Pinecil: Cheapest heat adjustable soldering Iron | 
 | Soldering Stand & Sponge | 1 | $4.99 | https://www.microcenter.com/product/659033/Mini-soldering_stand_with_sponge | Micro Center | Eclipse Enterprice Mini | 
 | Solder (50 g) | 1 | $8.99 | https://www.amazon.com/MAIYUM-63-37-Solder-Electrical-Soldering/dp/B075WB98FJ?th=1 | Amazon | "MAIYUM 63-37 Tin-Lead Rosin Core Solder Wire 0.8mm,50g g" | 
 | Solder Wick | 1 | $4.99 | https://www.microcenter.com/product/693022/Desoldering_Wick | MicroCenter | iFixit | 
 | *Footnote |  |  | *Lowest Price Option. Smaller quantities only avalible for same price |  |   | 

## Demo links

PCB Demo [Link](https://kicanvas.org/?repo=https%3A%2F%2Fgithub.com%2FMagnu-Shaak%2FCalc123%2Ftree%2Fmain%2FPCB)

OnShape Demo [Link](https://cad.onshape.com/documents/84cb760b87cada0103a9576e/w/b2684d83a2c2c7ea59db64e2/e/a0996dbd1c890850b6caf7a1?renderMode=0&uiState=6a6621498755df13821d28c6)
(click on search bar and hit enter again to load properly)

Code is visible under the Firmware folder

## Asembly

BOM (Bill of Materials) - [https://github.com/Magnu-Shaak/Calc123/blob/main/BOM.csv](url)

 [Insert BOM table here]

0 - Gather your Materials (PCB, Case parts, Devboard, and a usb-c to [something] cable to connect to your computer

1 - Download Circuit Python (v9.2.9) from circuitpython.org for the microcontroller [here](https://adafruit-circuit-python.s3.amazonaws.com)

2 - Download KMK (as .zip) from the kmk_firmware repo on github [here](https://github.com/KMKfw/kmk_firmware)

3 - Download the dependency files from the circuitpython.org/libraries (for the circuit python 9.x version) or from [here](https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/download/20260729/adafruit-circuitpython-bundle-9.x-mpy-20260729.zip)

4 - Download "main.py" and "oled_extension.py" from this repo. They are stored under the "Production" Folder

5 - Mount the microcontroller to your computer
    -Hold the 'B' (boot) bottom
    -Connect it to the computer via a usb-c to [anything on your computer] cable
    -Release the 'B' bottom

6 - Upload Circuit Python's .u2f file onto the microcontroller
    -It Should self eject and reconnect as CIRCUITPY

7 - From the kmk_firmware zip file, Upload the "KMK" folder and boot.py into the root of the CIRCUITPY drive

8.5 - If there is not already a "lib" folder in the root of your CIRCUITPY drive, make one

9 - From the circuit python bundle zip file, Upload the "adafruit_bus_device" and "adafruit_display_text" folders and "adafruit_displayio_ssd1306" file into the lib folder of your CIRCUITPY drive

10 - Eject your CIRCUITPY drive, and disconnect your microcontroller from your computer.

11 - Solder your XIAO RP 2040 devboard and 16 diodes (make sure they are oriented correctly) to the back of your PCB

12 - Place the Top Plate onto the front of your PCB, and align it with the mx key switch positions

13 - Solder the Key switches to the PCB on the back. The plate should be supported by the mx switches when you flip back over

14 - Install the Heatset Inserts to the bottom of your Case

15 - Place the PCB and Top Plate onto the supports in the case

16 - Screw the plate onto your PCB

16.5 - Add the Key Caps onto the MX Switches

17 - Slide in the Custom Insert
16 - Connect your Macropad to the computer and begin using it.








## All Images

  Schematic (Controller)

<img width="396" height="148" alt="image" src="https://github.com/user-attachments/assets/a686e848-113f-484f-980b-cca4f1314c52" />

  Schematic (Key Array)

<img width="550" height="254" alt="image" src="https://github.com/user-attachments/assets/51550049-dc31-4964-bbb7-284b34d0fd5d" />


  PCB Design (KiCad)

<img width="463" height="573" alt="image" src="https://github.com/user-attachments/assets/02ac58bb-bbfc-46d3-9afb-14df1b330701" />

  PCB Render (KiCad)
  
<img width="450" height="555" alt="image" src="https://github.com/user-attachments/assets/af24ea04-6e9a-484b-b9b5-dd2d77b416e4" />

  Case (Onshape)

<img width="568" height="266" alt="image" src="https://github.com/user-attachments/assets/b5abf3b6-45ff-4a97-b2ec-6e699604d3d6" />

  USB Cutout

<img width="543" height="244" alt="image" src="https://github.com/user-attachments/assets/f59b94cf-c650-4c5e-ac40-11f9cbf1673f" />

  Custom Insert (Onshape)

<img width="600" height="356" alt="image" src="https://github.com/user-attachments/assets/df8cff87-1239-46f8-89a6-8ad8e57e0572" />

  Code is under Firmware/main.py and Firmware/oled_extension.py

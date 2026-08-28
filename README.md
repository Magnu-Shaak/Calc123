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
Also available at [https://github.com/Magnu-Shaak/Calc123/blob/main/bom.csv](url)
| Item                      | Quantity | Listed Price | Total Cost | Link                                                                                  | Source        | Notes                                                                    |         |
|---------------------------|----------|--------------|------------|---------------------------------------------------------------------------------------|---------------|--------------------------------------------------------------------------|---------|
| PCB (5 piece)             | 1        | 4            | 5.76       |                                                                                       | JLC PCB       | Together with another order, paying with JLC account (Saves on shipping) |         |
| XIAO RP2040               | 1        | 4.9          | 4.9        | https://www.digikey.com/en/products/detail/seeed-technology-co-ltd/102010428/14672129 | DigiKey       |                                                                          |         |
| Diodes                    | 16       | 0.8          | 0.8        | https://www.digikey.com/en/products/detail/diotec-semiconductor/1N4148/13164514       | DigiKey       |                                                                          |         |
| "Switches                 |          |              |            |                                                                                       |               |                                                                          |         |
| (32 piece)"               | 1        | 10.99        | 10.99      | https://www.amazon.com/gp/aw/d/B09NNN4XPB                                             | Amazon        | Cheaper than AliExpress                                                  |         |
| 0.91 in. OLED (2 piece)   | 1        | 5.99         | 0          | https://www.amazon.com/Dorhea-Display-Module-SSD1306-3-3V-5V/dp/B08F9F8BYB            | Amazon        | Cheaper than Digikey with manu. Shipping. Can pay for myself             |         |
|                           |          |              |            |                                                                                       |               |                                                                          |         |
| Soldering Iron (Pinecil)* | 1        | 39.99        | 39.99      | https://www.amazon.com/PINECIL-Smart-Mini-Portable-Soldering/dp/B096X6SG13            | Amazon        | Cheapest Adjustable Soldering Iron                                       |         |
| Solder (0.5 oz)           | 1        | 2.97         | 2.97       | https://www.digikey.com/en/products/detail/chip-quik-inc/NCSW-031-0-5OZ/13531391      | DigiKey       | 63/37 tin-lead solder (0.031"")                                          |         |
| De-soldering Braid        | 1        | 2.59         | 2.59       | https://www.digikey.com/en/products/detail/chip-quik-inc/SOLDERWICK2-0/14636561       | DigiKey       | 0.08"                                                                    | 5 foot" |
| Soldering Stand & Sponge  | 1        | 3.28         | 3.28       | https://www.digikey.com/en/products/detail/soldered-electronics/555024/29271457       | Digikey       | Soldered Electronics: ""Soldering Iron Stand""                           |         |
|                           |          |              |            |                                                                                       |               |                                                                          |         |
| Case                      | 1        | 3.5          | 0          |                                                                                       | Local Library | $0.05 per gram, will pay for myself                                      |         |
| Key Caps (10 piece)       | 2        | 9.9          | 9.9        | https://www.digikey.com/en/products/detail/adafruit-industries-llc/5039/14313478      | DigiKey       | Adafruit, cheaper than singles                                           |         |
|                           |          |              |            |                                                                                       |               |                                                                          |         |
| M2 screw (16mm)           | 5        | 0.65         | 0.65       | http://digikey.com/en/products/detail/essentra-components/50M020040P016B/26883690     | DigiKey       | Essentra Components, 5th one was 1 cent                                  |         |
| M2 heatset Inserts        | 5        | 1.09         | 1.09       | https://www.digikey.com/en/products/detail/tri-star-industries-inc/M20X157C/13535373  | DigiKey       | Edit 3d model, 5th one was 1 cent                                        |         |
|                           |          |              |            |                                                                                       |               |                                                                          |         |
| DigiKey: Shipping and Tax | 8 (32)   | 9.09         | 10.45      | https://www.digikey.com/ordering/shoppingcart                                         | DigiKey       | Shipping with USPS Ground Advantage (4.99)                               |         |
| Amazon: Shipping and Tax  | s        | 3.82         | 3.82       |                                                                                       | Amazon        | Free shipping with prime                                                 |         |
|                           |          |              |            |                                                                                       |               |                                                                          |         |
| Total                     | 71       | 103.56       | 97.19      |                                                                                       |               |                                                                          |         |

## Demo links

PCB Demo [Link](https://kicanvas.org/?repo=https%3A%2F%2Fgithub.com%2FMagnu-Shaak%2FCalc123%2Ftree%2Fmain%2FPCB)

OnShape Demo [Link](https://cad.onshape.com/documents/84cb760b87cada0103a9576e/w/b2684d83a2c2c7ea59db64e2/e/a0996dbd1c890850b6caf7a1?renderMode=0&uiState=6a6621498755df13821d28c6)
(click on search bar and hit enter again to load properly)

Code is visible under the Firmware folder

## Asembly

BOM (Bill of Materials) - above, or at [https://github.com/Magnu-Shaak/Calc123/blob/main/BOM.csv](url)

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

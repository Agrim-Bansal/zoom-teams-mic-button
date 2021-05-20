import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import digitalio
import board
from time import sleep


led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

teams_mute = digitalio.DigitalInOut(board.GP13 )
zoom_mute = digitalio.DigitalInOut(board.GP10 )

zoom_mute.switch_to_input(pull=digitalio.Pull.DOWN)
teams_mute.switch_to_input(pull=digitalio.Pull.DOWN)

kbd = Keyboard(usb_hid.devices)


sleep(1)
zoom_mic_status = False
teams_mic_status = False

while True: 
    if zoom_mute.value == True:
        if zoom_mic_status == False:
            kbd.press(Keycode.ALT)
            kbd.press(Keycode.A)
            kbd.release_all()
            zoom_mic_status = True
    else:
        if zoom_mic_status == True:
            kbd.press(Keycode.ALT)
            kbd.press(Keycode.A)
            kbd.release_all()
            zoom_mic_status = False

    if teams_mute.value == True:
        if teams_mic_status == False:
            kbd.press(Keycode.CONTROL)
            kbd.press(Keycode.SHIFT)
            kbd.press(Keycode.M)
            kbd.release_all()
            teams_mic_status = True
    else:
        if teams_mic_status == True:
            kbd.press(Keycode.CONTROL)
            kbd.press(Keycode.SHIFT)
            kbd.press(Keycode.M)
            kbd.release_all()
            teams_mic_status = False


    led.value=zoom_mute.value or teams_mute.value
# Imports
import board
import digitalio

import usb_hid

from hid_gamepad import Gamepad

# Debug LED

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led.value = True



gp = Gamepad(usb_hid.devices)

pins = (board.GP0,board.GP1,board.GP2,board.GP3,board.GP4,board.GP5,board.GP6,board.GP7,board.GP8)
gamepad_buttons = (1,4,5,3,2,6,7,8,9)

buttons = [digitalio.DigitalInOut(pin) for pin in pins]
for button in buttons:
    button.direction = digitalio.Direction.INPUT
    button.pull = digitalio.Pull.UP

while True:
    led.value = True

    for i, button in enumerate(buttons):
        gamepad_button_num = gamepad_buttons[i]
        if button.value:
            gp.release_buttons(gamepad_button_num)
        else:
            gp.press_buttons(gamepad_button_num)
item = 0
rain: game.LedSprite = None
"""
YourNAme - Your class name
"""
 #---------------------------
 def on_pin_pressed_p0():
     if input.temperature() > 0:
         basic.show_string("+")
         elif input.temperature() < 0:
             basic.show_string("+")
             else: 
                 basic.show_string("Zero")
                 input.on_pin_pressed(TouchPin.P0, on_pin_presses_p0)
                 #------------------------------------------
                 def on_button_pressed_a():
                     global item
item += 1
basic.show_number(item)
input.on_button_pressed(Button.A, on_button_pressed_a)
#-------------------------------------------
def on_button_pressed_b():
    global item
    item += 1
    basic.show_number(item)
    input.on_button_pressed(Button.B, on_button_pressed_b)
    #-------------------------------------------
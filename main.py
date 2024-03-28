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

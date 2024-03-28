item = 0
rain: game.LedSprite = None
# AljoharaAldaej104
def on_pin_pressed_p0():
    if input.temperature() > 0:
        basic.show_string("+")
    else:
        if input.temperature() < 0:
            basic.show_string("-")
        else:
            basic.show_string("Zero")
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_button_pressed_a():
    global item
    item += 1
    basic.show_number(item)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global item
    item += -1
    basic.show_number(item)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    global rain
    rain = game.create_sprite(randint(0, 4), 0)
    for index in range(4):
        rain.change(LedSpriteProperty.Y, 1)
    basic.pause(200)
    rain.delete()
basic.forever(on_forever)

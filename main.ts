let item = 0
let rain : game.LedSprite = null
//  AljoharaAldaej104
input.onPinPressed(TouchPin.P0, function on_pin_pressed_p0() {
    if (input.temperature() > 0) {
        basic.showString("+")
    } else if (input.temperature() < 0) {
        basic.showString("-")
    } else {
        basic.showString("Zero")
    }
    
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    item += 1
    basic.showNumber(item)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    item += -1
    basic.showNumber(item)
})
basic.forever(function on_forever() {
    
    rain = game.createSprite(randint(0, 4), 0)
    for (let index = 0; index < 4; index++) {
        rain.change(LedSpriteProperty.Y, 1)
    }
    basic.pause(200)
    rain.delete()
})

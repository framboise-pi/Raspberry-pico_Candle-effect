# Candle effect and micorpython
Simple code for a candle effect, applied on 4 outputs, for having 4 asynchronous candles.

** there are 2 values you should change to see the differences with your candle(s) **

pin_led_0_pwm.freq(300)
_I'd say from 200 to 1000_

time.sleep(.1)

## how it works
It randoms a integer in 16bits (from 0 to 65535), for changing light level on each candles,
takes a .sleep and goes on for ever and ever.

## Notes
I use 2xLED(s) - old red ones 3mm - by output, and a R=330Ohms.
<br>A total of 8 red LEDs and PICO displays less than 80mA.

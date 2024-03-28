# Candle effect and micropython
Simple code for a candle effect, applied on 4 outputs, for having 4 asynchronous candles.

** there are 2 values you should change to see the differences with your candle(s) **

<br>pin_led_0_pwm.freq(300)
<br>_I'd say from 200 to 1000_
<br>
<br>time.sleep(.1)
<br>_from (.01) to (.1)_
<br>
## how it works
It randoms a 16bits integer (from 0 to 65535), for changing light level on each candles,
takes a .sleep and goes on for ever and ever.

## Notes
I use 2xLED(s) - old red ones 3mm - by output, (with a R=330Ohms on each output).
<br>A total of 8 red LEDs and PICO displays less than 80mA current consumption.
<br>Can hold candles for days with a battery.

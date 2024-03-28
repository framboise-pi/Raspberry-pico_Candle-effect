Simple code for a candle effect,
applied on 4 outputs, for having 4 asynchronous candles.

2 values you should change to see the differences with your candle(s)
# do not hesitate to test different frequency values
pin_led_0_pwm.freq(300)
# I'd say from 200 to 1000

# do not hesitate to test different sleep values
time.sleep(.1)

It randoms a integer in 16bits (from 0 to 65535), for changing light level.

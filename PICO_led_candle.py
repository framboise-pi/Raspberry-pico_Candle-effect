# github.com/framboise-pi (Camille Lafontaine)
# Candle effect - MicroPython - Raspberry Pico
from machine import Pin
from machine import PWM
import random
import time

# IN THIS VERSION: 4 LEDS USED = 4 CANDLES
pin_led_0 = Pin(0, mode=Pin.OUT)
pin_led_0_pwm = PWM(pin_led_0)

pin_led_1 = Pin(1, mode=Pin.OUT)
pin_led_1_pwm = PWM(pin_led_1)

pin_led_2 = Pin(2, mode=Pin.OUT)
pin_led_2_pwm = PWM(pin_led_2)

pin_led_3 = Pin(3, mode=Pin.OUT)
pin_led_3_pwm = PWM(pin_led_3)

# do not hesitate to test different frequency values
pin_led_0_pwm.freq(300)
pin_led_1_pwm.freq(300)
pin_led_2_pwm.freq(200)
pin_led_3_pwm.freq(200)


while True:
    hasar = random.randint(0, 65536)
    pin_led_0_pwm.duty_u16(hasar)
    hasar = random.randint(0, 65536)
    pin_led_1_pwm.duty_u16(hasar)
    hasar = random.randint(0, 65536)
    pin_led_2_pwm.duty_u16(hasar)
    hasar = random.randint(0, 65536)
    pin_led_3_pwm.duty_u16(hasar)
    # do not hesitate to test different sleep values
    time.sleep(.1)
    
#####
# FUNCTIONS MEMO
#####
# pin_led.toggle()
# pin_led.on()
# pin_led.high()
# pin_led.value(1)
# pin_led.off()
# pin_led.low()
# pin_led.value(0)

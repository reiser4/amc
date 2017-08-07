import Adafruit_BBIO.PWM as PWM
import time

pin = "P8_13"

#PWM.start(channel, duty, freq=2000, polarity=0)
#duty values are valid 0 (off) to 100 (on)
PWM.start(pin, 50)
#PWM.set_duty_cycle(pin, 25.5)
#PWM.set_frequency(pin, 10)

for i in range(0,100):
	print i
	PWM.set_duty_cycle(pin,i)
	time.sleep(0.1)

time.sleep(5)

PWM.stop(pin)
PWM.cleanup()

#set polarity to 1 on start:
#PWM.start(pin, 50, 2000, 1)

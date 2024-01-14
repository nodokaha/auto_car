import pigpio
import time

def main(control, speed):
	pi=pigpio.pi()
	pi.set_mode(2, pigpio.OUTPUT)
	pi.set_mode(3, pigpio.OUTPUT)
	pi.set_mode(23, pigpio.OUTPUT)
	pi.set_mode(24, pigpio.OUTPUT)
	pi.set_mode(18, pigpio.OUTPUT)

	pi.hardware_PWM(18, 490, speed)

	if ( control == 0 ):
			pi.hardware_PWM(18, 490, sys.argv[2])
	elif ( control == 1 ):
			pi.write(2, 0)
			pi.write(3, 0)
			pi.write(23, 0)
			pi.write(24, 0)
	elif ( control == 2 ):
			pi.write(2, 0)
			pi.write(3, 1)
			pi.write(23, 0)
			pi.write(24, 1)
	elif ( control == 3 ):
			pi.write(2, 0)
			pi.write(3, 0)
			pi.write(23, 0)
			pi.write(24, 1)
	elif ( control == 4 ):
			pi.write(2, 0)
			pi.write(3, 1)
			pi.write(23, 0)
			pi.write(24, 0)
	elif ( control == 5 ):
			pi.write(2, 1)
			pi.write(3, 0)
			pi.write(23, 1)
			pi.write(24, 0)
	elif ( control == 6 ):
			pi.write(2, 1)
			pi.write(3, 1)
			pi.write(23, 1)
			pi.write(24, 1)

	pi.stop()

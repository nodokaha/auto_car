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

	match control:
		case 0:
			pi.write(2, 0)
			pi.write(3, 0)
			pi.write(23, 0)
			pi.write(24, 0)
		case 1:
			pi.write(2, 0)
			pi.write(3, 1)
			pi.write(23, 0)
			pi.write(24, 1)
		case 2:
			pi.write(2, 1)
			pi.write(3, 0)
			pi.write(23, 1)
			pi.write(24, 0)
		case 4:
			pi.write(2, 1)
			pi.write(3, 1)
			pi.write(23, 1)
			pi.write(24, 1)
		case 5:
			pi.hardware_PWM(18, 490, sys.argv[2])

	pi.stop()

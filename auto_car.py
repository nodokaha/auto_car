import wiringpi as gpio
#import cgi
#form = cgi.FiledStorage()
gpio.wiringPiSetup()
gpio.pinMode(2,gpio.OUTPUT)
gpio.pinMode(3,gpio.OUTPUT)
gpio.pinMode(23,gpio.OUTPUT)
gpio.pinMode(24,gpio.OUTPUT)
#gpio.pinMode(18,gpio.OUTPUT)
gpio.pwmSetMode(gpio.PWM_MODE_MS)
gpio.pwmSetClock(400)
gpio.pwmSetRange(1024)

gpio.pwmWrite(18, 0)
#gpio.digitalWrite(18, gpio.HIGH)
gpio.digitalWrite(2, gpio.LOW)
gpio.digitalWrite(3, gpio.HIGH)
gpio.digitalWrite(23, gpio.LOW)
gpio.digitalWrite(24, gpio.HIGH)


import pigpio
import time

pi=pigpio.pi()		# pigpioを初期化してpiという変数に入れる

pi.set_mode(2, pigpio.OUTPUT)	# 2番ピンを出力に設定する

pi.write(2, 1)			# 2番ピンに1を設定する(電圧を出力させる)
time.sleep(5)			# 5秒待つ
pi.write(2, 0)			# 2番ピンに0を設定する(電圧を止める)
pi.stop()			# 終了させる


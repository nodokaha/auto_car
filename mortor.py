import pigpio
import time

pi=pigpio.pi()		# pigpioを初期化してpiという変数に入れる

pi.set_mode(2, pigpio.OUTPUT)		# 2番ピンを出力に設定する
pi.set_mode(3, pigpio.OUTPUT)		# 3番ピンを出力に設定する

# 正転
pi.write(2, 0)				# 2番ピンを0に設定する
pi.write(3, 1)				# 3番ピンを1に設定する

time.sleep(5)				# 5秒待つ

# ブレーキ
pi.write(2, 1)				# 2番ピンを1に設定する
pi.write(3, 1)				# 3番ピンを1に設定する

pi.stop()

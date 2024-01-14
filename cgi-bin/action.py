#!/usr/bin/env python3
import cgi
import autocar_control
form = cgi.FieldStorage()

print('Content-Type: text/html; charset=utf-8')
print()
# print('<h1>Hello, World</h1>')
#print('<form method="POST">')
#print('<input type="checkbox" name="item" value=1 />')
#print('<input type="submit">')
#print('</form>')

#item = form.getvalue("item")
#if "1" == item:
#	print('<h2>Checked!</h2>')
#else:
#	print('<h2>Un Checked!</h2>')
speed = int(form.getvalue("speed"))
mortor = int(form.getvalue("mortor"))
control = ["set", "stop", "roll", "turn_right", "turn_left", "back_roll", "brake"].index(mortor)

autocar_control.main(control, speed)

print(form)
redirectURL = "/"
print('<html>')
print('  <head>')
print('    <meta http-equiv="refresh" content="0;url='+str(redirectURL)+'" />') 
print('  </head>')
print('</html>')

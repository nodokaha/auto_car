#!/usr/bin/python3
import cgi
form = cgi.FieldStorage()
print('Content-Type: text/html; charset=utf-8')
print()
print('<h1>Hello, World</h1>')
print('<form method="POST">')
print('<input type="checkbox" name="item" value=1 />')
print('<input type="submit">')
print('</form>')

item = form.getvalue("item")
if "1" == item:
	print('<h2>Checked!</h2>')
else:
	print('<h2>Un Checked!</h2>')

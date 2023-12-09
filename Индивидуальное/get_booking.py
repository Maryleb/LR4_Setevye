from jinja2 import Template
import sqlite3
from booking_model import get_booked_rooms

param_1 = 2
param_2 = 7
conn = sqlite3.connect("booking.sqlite")
f_damp = open('booking.db', 'r', encoding='utf-8-sig')
damp = f_damp.read()
f_damp.close()
conn.executescript(damp)
conn.commit()

df_booked_rooms = get_booked_rooms(conn, param_1, param_2)
conn.close()

f_template = open('booking_templ.html', 'r', encoding='utf-8-sig')
html = f_template.read()
f_template.close()

template = Template(html)
result_html = template.render(
 param_1 = param_1,
 param_2 = param_2,
 booked_rooms = df_booked_rooms,
 len = len)


f = open('booking.html', 'w', encoding='utf-8-sig')
f.write(result_html)
f.close()

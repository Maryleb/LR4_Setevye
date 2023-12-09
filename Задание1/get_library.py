from jinja2 import Template
import sqlite3
from library_model import get_publisher
from library_model import get_genre
from library_model import get_book
from library_model import get_author
from library_model import get_reader
from library_model import get_book_author
from library_model import get_book_reader

conn = sqlite3.connect("library(1).sqlite")
df_publisher = get_publisher(conn)
df_genre = get_genre(conn)
df_book = get_book(conn)
df_author = get_author(conn)
df_reader = get_reader(conn)
df_book_author = get_book_author(conn)
df_book_reader = get_book_reader(conn)
conn.close()

f_template = open('library_temp.html', 'r', encoding='utf-8-sig')
html = f_template.read()
f_template.close()

template = Template(html)
result_html = template.render(name1 = "publisher", relation1 = df_publisher, len=len,
                              name2 = "genre", relation2= df_genre,
                              name4 = "author", relation4 = df_author,
                              name3 = "reader", relation3 = df_reader,
                              name5 = "book_author", relation5 = df_book_author,
                              name6 = "book", relation6 = df_book,
                              name7 = "book_reader", relation7 = df_book_reader)

f = open('library.html', 'w', encoding ='utf-8-sig')
f.write(result_html)
f.close()
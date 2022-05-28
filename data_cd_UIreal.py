from tkinter import *
from urllib.request import urlopen
from bs4 import BeautifulSoup
from tkinter import ttk
import collections
collections.Callable = collections.abc.Callable


window=Tk()
window.title('Top 100 Songs in UK')
window.state("zoomed")

s = ttk.Style()
s.theme_use('clam')
s.configure('Treeview', rowheight=40)
tree = ttk.Treeview(window, column=("c1", "c2", "c3", "c4"), show='headings', height=1920)

tree.column("# 1", anchor=CENTER)
tree.heading("# 1", text="Pos")
tree.column("# 2", anchor=CENTER)
tree.heading("# 2", text="Song Name")
tree.column("# 3", anchor=CENTER)
tree.heading("# 3", text="Singer")
tree.column("# 4", anchor=CENTER)
tree.heading("# 4", text="Publisher")

weburl='https://www.officialcharts.com/charts/'
url=urlopen(weburl)
urlsoup=BeautifulSoup(url, 'lxml')
realurl=urlsoup('div', {'class':'title-artist'})
lst=list()
num=0

for name in realurl:
    num=num+1
    title=name.find('div', {'class':'title'})
    lst.append(title)
    artist=name.find('div', {'class':'artist'})
    lst.append(artist)
    publisher=name.find('div', {'class':'label-cat'})
    lst.append(publisher)
    tree.insert('', 'end', text="1", values=(num, title.text, artist.text, publisher.text))


tree.pack()
window.mainloop()

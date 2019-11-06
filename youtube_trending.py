#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import *
from bs4 import BeautifulSoup
from urllib import urlopen
import webbrowser


source=urlopen("https://www.youtube.com/feed/trending").read()
soup=BeautifulSoup(source,'html5lib')
trending_div=soup.find_all("a", class_ = "yt-uix-tile-link")


def open_url(url_path):
    #
    def main_print():
        webbrowser.open(url_path)
    return main_print

class Application(Frame):

    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()
        self.i = 0


    def createWidgets(self):

        for div in trending_div[0:10]:
            #title
            self.title=div.get('title')
            self.label_title=Label(self.frame, text=self.title,width=100)
            #url
            self.url="www.youtube.com"+div.get('href')
            #button
            self.open_url_button = Button(self.frame)
            self.open_url_button["text"] = "OPEN"
            self.open_url_button["command"] = open_url(self.url)



            self.open_url_button.grid(row=self.i,column=0,sticky=E)
            self.label_title.grid(row=self.i, column=1,sticky=W)
            self.i+=1



root = Tk()
app = Application(master=root)
app.createWidgets()
root.mainloop()


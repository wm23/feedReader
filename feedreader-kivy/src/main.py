__author__ = 'wojtek'

import kivy
kivy.require('1.9.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label


from feedreader.lib import dummy

class MyApp(App):

    def build(self):
        return Label(text=dummy.dummy())


if __name__ == '__main__':
    MyApp().run()
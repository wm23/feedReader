import kivy
kivy.require('1.9.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label

import sys
#sys.path.insert(0, "/pub/btsync/Praca/Projekty/FeedReader/feedReader/feedreader-kivy/src")
#sys.path.insert(0, "/pub/btsync/Praca/Projekty/FeedReader/feedReader/feedreader-base/src")

from feedreader.ui.mainview import MainView


__author__ = 'wojtek'
__version__ = "0.0.1"

APPLICATION_TITLE = "Feed Reader"
APPLICATION_VERSION = __version__

TEMPLATES_DIRECTORY = "feedreader/ui/templates"

class FeedReaderApp(App):
    kv_directory = TEMPLATES_DIRECTORY

    def build(self):
        print sys.path

        self.title = APPLICATION_TITLE
        return MainView()


if __name__ == '__main__':
    FeedReaderApp().run()
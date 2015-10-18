__author__ = 'wojtek'


from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ListProperty, ObjectProperty, DictProperty

from feedreader.lib.api import FeedReader


class FeedItemsList(Screen):
    order = ObjectProperty()
    data = DictProperty()


    def __init__(self, **kw):
        super(FeedItemsList, self).__init__(**kw)
        self.order = ["{0}".format(index) for index in range(19,-1,-1)]
        self.data = {str(item.id): {'title': item.title, 'summary': item.summary, 'image': item.image, 'is_selected': False} for item in FeedReader.getFeedItems("aaa")}

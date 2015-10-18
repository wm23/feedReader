__author__ = 'wojtek'

from kivy.uix.listview import CompositeListItem
from kivy.properties import ObjectProperty

class FeedListItemLabel(CompositeListItem):
    text = ObjectProperty()
    title = ObjectProperty()
    image = ObjectProperty()
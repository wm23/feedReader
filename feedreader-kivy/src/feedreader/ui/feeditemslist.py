__author__ = 'wojtek'


from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ListProperty, ObjectProperty, DictProperty


class FeedItemsList(Screen):
    item_strings = ObjectProperty()
    integers_dict = DictProperty()

    args_converter = lambda self, row_index, rec: \
            {'text': rec['text'],
             'manager': self.manager,
             'size_hint_y': None,
             'height': 25,
             'cls_dicts': []}

    def __init__(self, **kw):
        super(FeedItemsList, self).__init__(**kw)
        self.item_strings = ["{0}".format(index) for index in range(99,-1,-1)]
        self.integers_dict = {str(i): {'text': str(i), 'is_selected': False} for i in range(100)}

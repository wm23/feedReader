from kivy.properties import ListProperty, ObjectProperty, DictProperty
from kivy.uix.rst import RstListItem

__author__ = 'wojtek'
__version__ = "0.0.1"
APPLICATION_TITLE = "Feed Reader"
APPLICATION_VERSION = "0.0.1"

TEMPLATES_DIRECTORY = "templates"

import kivy

kivy.require('1.0.10')

from kivy.app import App
from kivy.uix.modalview import ModalView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.listview import ListView, ListItemLabel
from kivy.adapters.listadapter import ListAdapter
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.adapters.dictadapter import DictAdapter
from kivy.uix.listview import ListItemButton, ListItemLabel, CompositeListItem
from kivy.uix.listview import SelectableView
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

#Window.clearcolor = get_color_from_hex('#FFFFFF')

class MyListItem(CompositeListItem):
    selected_color = ListProperty([0.8, 0.8, 0.8, 1])
    deselected_color = ListProperty([1, 1, 1, 1])
    state_color = ListProperty()

    def select(self, *args):
        self.state_color = self.selected_color
        self.color=(1,0,0,1)
        super(MyListItem, self).select(*args) #Just in case

    def deselect(self, *args):
        self.state_color = self.deselected_color
        super(MyListItem, self).deselect(*args) #Just in case

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            #Naive way to access `ListView.adapter.handle_selection`
            self.parent.parent.parent.adapter.handle_selection(self)
            print(self.state_color)

            return True

        return super(MyListItem, self).on_touch_up(touch)


class FeedItemView(Screen):
    text = ObjectProperty()
    manager = ObjectProperty(None,  allownone=True)


    def do_onreturn(self):
        print("AAAAAAAAAAAAAa")
        self.manager.current = "screen_one"
        self.manager.remove_widget(self)



        # sm.switch_to(screens[0])get_screen(name)



class MainView(BoxLayout):
    manager = ObjectProperty(None)
    item_strings = ObjectProperty()
    dict_adapter = ObjectProperty()
    integers_dict = DictProperty()

    list_posts = ObjectProperty(None)

    # args_converter = lambda self, row_index, rec: {
    #         'text': rec['text'],
    #         'is_selected': rec['is_selected'],
    #         'size_hint_y': None,
    #         'height': 25}

    args_converter = lambda self, row_index, rec: \
            {'text': rec['text'],
            'size_hint_y': None,
            'height': 25,
            'cls_dicts': [{'cls': ListItemButton,
                    'kwargs': {'text': rec['text'], 'on_press': self.do_press}},
                {'cls': ListItemLabel,
                    'kwargs': {'text': "Middle-{0}".format(rec['text']),
                            'is_representing_cls': True}},
                {'cls': ListItemButton,
                    'kwargs': {'text': rec['text']}}]}

    def __init__(self, **kwargs):
        self.item_strings = ["{0}".format(index) for index in range(99,-1,-1)]
        self.integers_dict = {str(i): {'text': str(i), 'is_selected': False} for i in range(100)}
        self.dict_adapter = DictAdapter(sorted_keys=self.item_strings,
                                   data=self.integers_dict,
                                   args_converter=self.args_converter,
                                   selection_mode='single',
                                   allow_empty_selection=False,
                                   cls = MyListItem)
        super(MainView, self).__init__(**kwargs)

    def do_press(self, button):
        screen = FeedItemView();
        screen.text = button.text
        screen.name = "AAAAA"
        self.manager.add_widget(screen)
        self.manager.current = 'AAAAA'
        # self.manager.switch_to(screen)

    def do_onbutton(self):
        self.dict_adapter.sorted_keys = ["{0}".format(index) for index in range(100)]



        

class FeedReaderApp(App):
    kv_directory = TEMPLATES_DIRECTORY

    def build(self):
        self.title = APPLICATION_TITLE + " " + APPLICATION_VERSION
        return MainView()



if __name__ == '__main__':
    FeedReaderApp().run()

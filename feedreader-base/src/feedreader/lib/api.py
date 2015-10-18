__author__ = 'wojtek'

from feedreader.lib.logic.feeditemsmanager import FeedItemsManager
#from feedreader.lib.logic.testfeeditemsmanager import TestFeedItemsManager as FeedItemsManager

class FeedReader:
    """
    Facade class with API of base library
    """

    @staticmethod
    def getFeedItems(parent_group):
        return FeedItemsManager.getItems(parent_group)
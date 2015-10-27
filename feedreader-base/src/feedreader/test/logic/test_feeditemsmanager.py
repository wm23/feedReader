import unittest

__author__ = 'wojtek'

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from feedreader.lib.logic.feeditemsmanager import FeedItemsManager
from feedreader.lib.model import Base, Feed, FeedItem, FeedItemContent, Group
from feedreader.lib import data



class FeedItemsManagerTests(unittest.TestCase):

        GROUP1_ID = 1
        GROUP2_ID = 2
        GROUP3_ID = 3
        GROUP4_ID = 4

        GROUP1_ITEMS_COUNT = 4
        GROUP2_ITEMS_COUNT = 1
        GROUP3_ITEMS_COUNT = 2
        GROUP4_ITEMS_COUNT = 1

        def testGetItems(self):
            session = self.create_sample_data

            items = FeedItemsManager.getItems(session, self.GROUP1_ID)
            self.assertTrue(isinstance(items[0], data.FeedItem), "getItems should return feedreader.lib.data.FeedReader objects")

            self.assertEqual(len(FeedItemsManager.getItems(session, self.GROUP1_ID)), self.GROUP1_ITEMS_COUNT)
            self.assertEqual(len(FeedItemsManager.getItems(session, self.GROUP2_ID)), self.GROUP2_ITEMS_COUNT)
            self.assertEqual(len(FeedItemsManager.getItems(session, self.GROUP3_ID)), self.GROUP3_ITEMS_COUNT)
            self.assertEqual(len(FeedItemsManager.getItems(session, self.GROUP4_ID)), self.GROUP4_ITEMS_COUNT)



        @property
        def create_sample_data(self):
            engine = create_engine('sqlite:///:memory:', echo=True)

            Base.metadata.bind = engine
            DBSession = sessionmaker()
            DBSession.bind = engine
            session = DBSession()

            Base.metadata.create_all(engine)

            group1_id = self.insert(session, Group(id=self.GROUP1_ID, name="Test group 1"))
            group2_id = self.insert(session, Group(id=2, name="Test group 1/2", parrent_group_id=group1_id))
            group3_id = self.insert(session, Group(id=self.GROUP3_ID, name="Test group 1/3", parrent_group_id=group1_id))
            group4_id = self.insert(session, Group(id=4, name="Test group 1/3/4", parrent_group_id=group3_id))

            feed1_id = self.insert(session, Feed(name="Test feed in group 1", group_id=group1_id))
            feed2_id = self.insert(session, Feed(name="Test feed in group 2", group_id=group2_id))
            feed3_id = self.insert(session, Feed(name="Test feed in group 3", group_id=group3_id))
            feed4_id = self.insert(session, Feed(name="Test feed in group 4", group_id=group4_id))

            feed_item = FeedItem(author="Test author", title="feed item 1", feed_id=feed1_id)

            self.insert(session, feed_item)
            self.insert(session, FeedItem(author="Test author", title="feed item 2", feed_id=feed2_id))
            self.insert(session, FeedItem(author="Test author", title="feed item 3", feed_id=feed3_id))
            self.insert(session, FeedItem(author="Test author", title="feed item 4", feed_id=feed4_id))

            return session

        def insert(self, session, param):
            session.add(param)
            session.commit()
            session.refresh(param)
            return param.id


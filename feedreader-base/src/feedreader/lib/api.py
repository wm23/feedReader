#!/usr/bin/python
# -*- coding: UTF-8 -*-

__author__ = 'wojtek'

from feedreader.lib.logic.feeditemsmanager import FeedItemsManager
#from feedreader.lib.logic.testfeeditemsmanager import TestFeedItemsManager as FeedItemsManager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from feedreader.lib.model import Base

class FeedReader:
    """
    Facade class with API of base library
    """

    @staticmethod
    def getFeedItems(parent_group):
	engine = create_engine('sqlite:///:memory:', echo=True)

        Base.metadata.bind = engine
        DBSession = sessionmaker()
        DBSession.bind = engine
        session = DBSession()

        Base.metadata.create_all(engine)

        return FeedItemsManager.getItems(session, parent_group)
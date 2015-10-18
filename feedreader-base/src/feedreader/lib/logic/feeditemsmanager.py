__author__ = 'wojtek'

from feedreader.lib import model
from feedreader.lib import data

class FeedItemsManager():

    @staticmethod
    def getItems(session, group_id):
        result = []
        for group in session.query(model.Group).filter_by(parrent_group_id=group_id):
            result.extend(FeedItemsManager.getItems(session, group.id))

        for feed in session.query(model.Feed).filter_by(group_id=group_id):
            for item in session.query(model.FeedItem).filter_by(feed_id=feed.id):
                result.append(item.to_dto())

        return result


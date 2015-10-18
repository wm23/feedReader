__author__ = 'wojtek'

import collections

Feed = collections.namedtuple('Feed', 'id title subtitle etag link update_frequency updated updated_parsed')
FeedItem = collections.namedtuple('FeedItem', 'id title summary image feed contents author link published parsed tags')
Group = collections.namedtuple('Group', 'id parrent_group_id name') #is_top_group groups feeds')
__author__ = 'wojtek'

from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)

from feedreader.lib.api import FeedReader

__all__ = [FeedReader]
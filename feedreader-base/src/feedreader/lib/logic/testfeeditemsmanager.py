#!/usr/bin/python
# -*- coding: UTF-8 -*-


__author__ = 'wojtek'
from feedreader.lib.data import FeedItem


class TestFeedItemsManager():

    @staticmethod
    def getItems(session, parent_group):
        result = [
            FeedItem('1', 'Cimoszewicz: W Krynicy wiało surrealizmem, ciekło od wazeliny. Więcej tu nie przyjadę', '- Zadano wielki cios idei Forum Ekonomicznego w Krynicy. Ono stało się jednostronnie partyjniackie - ocenił w „Faktach po Faktach” decyzję o przyznaniu prezesowi PiS tytułu Człowieka Roku były premier Włodzimierz Cimoszewicz.', 'http://r-scale-f1.dcs.redcdn.pl/scale/o2/tvn/web-content/m/p1/i/d1a69640d53a32a9fb13e93d1c8f3104/f0a2a959-c69e-4d93-98e5-f92fab9a25f3.png?type=0&srcmode=3&srcx=0/1&srcy=0/1&srcw=972&srch=547&dstw=972&dsth=547', 'feed', [], '', '','','',''),
            FeedItem('2', 'Title2', 'subtitle', 'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRKOWUeCOLFIxYSq5ZUxKEZbb9eqfqZ_8UidTEMbhfG6bhXtcqQig', 'feed', [], '', '','','',''),
            FeedItem('3', 'Title3', 'subtitle', 'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRKOWUeCOLFIxYSq5ZUxKEZbb9eqfqZ_8UidTEMbhfG6bhXtcqQig', 'feed', [], '', '','','',''),
            FeedItem('4', 'Title4', 'subtitle', 'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRKOWUeCOLFIxYSq5ZUxKEZbb9eqfqZ_8UidTEMbhfG6bhXtcqQig', 'feed', [], '', '','','',''),
            FeedItem('0', 'Title10', 'subtitle', 'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRKOWUeCOLFIxYSq5ZUxKEZbb9eqfqZ_8UidTEMbhfG6bhXtcqQig', 'feed', [], '', '','','',''),

            FeedItem('11', 'Title1', 'subtitle', 'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRKOWUeCOLFIxYSq5ZUxKEZbb9eqfqZ_8UidTEMbhfG6bhXtcqQig', 'feed', [], '', '','','',''),
            FeedItem('12', 'Title2', 'subtitle', 'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRKOWUeCOLFIxYSq5ZUxKEZbb9eqfqZ_8UidTEMbhfG6bhXtcqQig', 'feed', [], '', '','','',''),
            FeedItem('13', 'Title3', 'subtitle', 'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRKOWUeCOLFIxYSq5ZUxKEZbb9eqfqZ_8UidTEMbhfG6bhXtcqQig', 'feed', [], '', '','','',''),
            FeedItem('14', 'Title4', 'subtitle', 'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRKOWUeCOLFIxYSq5ZUxKEZbb9eqfqZ_8UidTEMbhfG6bhXtcqQig', 'feed', [], '', '','','',''),
            FeedItem('10', 'Title10', 'subtitle', 'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRKOWUeCOLFIxYSq5ZUxKEZbb9eqfqZ_8UidTEMbhfG6bhXtcqQig', 'feed', [], '', '','','',''),

            FeedItem('21', 'Title1', 'subtitle', 'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRKOWUeCOLFIxYSq5ZUxKEZbb9eqfqZ_8UidTEMbhfG6bhXtcqQig', 'feed', [], '', '','','',''),
            FeedItem('22', 'Title2', 'subtitle', 'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRKOWUeCOLFIxYSq5ZUxKEZbb9eqfqZ_8UidTEMbhfG6bhXtcqQig', 'feed', [], '', '','','',''),
            FeedItem('23', 'Title3', 'subtitle', 'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRKOWUeCOLFIxYSq5ZUxKEZbb9eqfqZ_8UidTEMbhfG6bhXtcqQig', 'feed', [], '', '','','',''),
            FeedItem('24', 'Title4', 'subtitle', 'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRKOWUeCOLFIxYSq5ZUxKEZbb9eqfqZ_8UidTEMbhfG6bhXtcqQig', 'feed', [], '', '','','',''),
            FeedItem('20', 'Title10', 'subtitle', 'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRKOWUeCOLFIxYSq5ZUxKEZbb9eqfqZ_8UidTEMbhfG6bhXtcqQig', 'feed', [], '', '','','',''),
#            FeedItem = collections.namedtuple('FeedItem', 'id title summary feed contents author link published parsed tags')

        ]
        return result

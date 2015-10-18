__author__ = 'wojtek'

import unittest
import logging

from feedreader.lib import model

class ModelTests(unittest.TestCase):

    def test_model_classes(self):
        for klass in self.inheritors(model.Base):
            self.check_if_class_has_methods(klass)

    def inheritors(self, klass):
        subclasses = set()
        work = [klass]
        while work:
            parent = work.pop()
            for child in parent.__subclasses__():
                if child not in subclasses:
                    subclasses.add(child)
                    work.append(child)
        return subclasses

    def check_if_class_has_methods(self, klass):
        instance = klass()
        try:
            instance.to_dto()
        except AttributeError, e:
            self.fail("Class '%s' should overwrite method: to_dto()" % (klass.__name__))

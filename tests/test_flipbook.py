#!/usr/bin/env python
# -*- coding: utf-8 -*-

from daumenkivy.flipbook import FlipBook


class TestFlipBook(object):
    """TestCase for the FlipBook carousel.
    """
    def setup(self):
        self.fb = FlipBook("FlipBook01")

    def test_name(self):
        assert self.fb.name == "FlipBook01"

    def teardown(self):
        pass


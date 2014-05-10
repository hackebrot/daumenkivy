#!/usr/bin/env python
# -*- coding: utf-8 -*-

from daumenkivy.daumenkivyapp import DaumenkivyApp


class TestApp(object):
    """TestCase for DaumenkivyApp.
    """
    def setup(self):
        self.app = DaumenkivyApp()

    def test_name(self):
        assert self.app.name == 'daumenkivy'

    def test_no_flip_books(self):
        err_msg = "flip_books is expected to be empty at first"
        assert not self.app.flip_books, err_msg

    def teardown(self):
        pass


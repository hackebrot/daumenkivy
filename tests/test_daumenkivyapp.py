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

    def teardown(self):
        pass


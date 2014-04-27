#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from daumenkivy.daumenkivyapp import DaumenkivyApp


class TestDaumenkivyApp(unittest.TestCase):
    """TestCase for DaumenkivyApp.
    """
    def setUp(self):
        self.app = DaumenkivyApp()

    def test_name(self):
        self.assertEqual(self.app.name, 'daumenkivy')

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
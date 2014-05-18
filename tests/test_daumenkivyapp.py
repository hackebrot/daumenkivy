#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from daumenkivy.daumenkivyapp import DaumenkivyApp


@pytest.fixture(scope="class")
def daumenkivy_app():
    return DaumenkivyApp()


class TestDaumenkivyApp(object):
    """TestCase for DaumenkivyApp.
    """
    def test_name(self, daumenkivy_app):
        assert daumenkivy_app.name == 'daumenkivy'


class TestFlipBooks(object):
    """TestCase for DaumenkivyApps flip_books functionality.
    """
    def test_no_flip_books(self, daumenkivy_app):
        err_msg = "flip_books is expected to be empty at first"
        assert not daumenkivy_app.flip_books, err_msg

    def test_create_flip_book(self, daumenkivy_app):
        daumenkivy_app.create_flip_book("FlipBook01")

        err_msg = "flip_books is expected to contain a FlipBook"
        assert daumenkivy_app.flip_books, err_msg


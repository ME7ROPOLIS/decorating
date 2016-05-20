#!/usr/bin/env python
# coding=utf-8
#
#   Python Script
#
#   Copyright © Manoel Vilela
#
#

import unittest
import time
from decorating import debug, animated


class TestAnimatedDecorator(unittest.TestCase):

    args = ('banana', 'choque')

    def test_decorator_function_with_args(self):
        @debug
        @animated('with args')
        def with_args(*args):
            time.sleep(0.5)
            return args

        self.assertEqual(with_args(*self.args), self.args,
                         'need returns the same I/O')

    def test_decorator_function_without_args(self):

        @debug
        @animated()
        def without_args(*args):
            time.sleep(0.5)
            return args

        self.assertEqual(without_args(*self.args), self.args,
                         'need returns the same I/O')

    def test_decorator_function_decorated(self):
        @debug
        @animated
        def decorated(*args):
            time.sleep(0.5)
            return args

        self.assertEqual(decorated(*self.args), self.args,
                         'need returns the same I/O')

    def test_decorator_with_context_manager(self):
        @debug
        @animated
        def animation(*args):
            time.sleep(1)

        with animated('testing something'):
            self.assertIsNone(animation(*self.args),
                              'need returns the same I/O')

    def test_decorator_with_nested_context_managers(self):

        @debug
        @animated('with args')
        def with_args(*args):
            time.sleep(0.5)
            return args

        with animated('level1'):
            with animated('level2'):
                with animated('level3'):
                    x = with_args(*self.args)
                y = with_args(*self.args)
            z = with_args(*self.args)

        for i in (x, y, z):
            self.assertEqual(x, self.args, 'need returns the same I/O')


if __name__ == '__main__':
    unittest.main()

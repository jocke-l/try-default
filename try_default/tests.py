import unittest

from . import try_default
from ._utils import curried


class Curried(unittest.TestCase):
    def test_identity(self):
        self.assertEqual(curried(lambda: 1), 1)
        self.assertEqual(curried(lambda a: a)(1), 1)

    def testcurried(self):
        curried_func = curried(lambda a, b, c: a + b + c)
        self.assertEqual(curried_func(1)(2)(3), 6)
        self.assertEqual(curried_func(1)(2, 3), 6)
        self.assertEqual(curried_func(1, 2, 3), 6)
        self.assertEqual(curried_func(1, 2)(3), 6)


class TryDefault(unittest.TestCase):
    def test_core_features(self):
        self.assertEqual(try_default(lambda: [][1], {IndexError: 0}), 0)
        self.assertEqual(try_default(lambda: [1][0], {IndexError: 0}), 1)

    def test_parent_catch(self):
        def raise_keyboard_interrupt():
            raise KeyboardInterrupt

        self.assertEqual(try_default(raise_keyboard_interrupt,
                                     {KeyboardInterrupt: 0}), 0)
        self.assertEqual(try_default(raise_keyboard_interrupt,
                                     {BaseException: 0}), 0)

    def test_reraise_unhandled_exception(self):
        with self.assertRaises(IndexError):
            try_default(lambda: [][1], {})

    def test_args(self):
        def get_actual_budget(costs, headroom):
            return sum(costs) + headroom

        get_budget = try_default(get_actual_budget, {TypeError: 0})

        broken_costs = [25, 25, None, 10]
        clean_costs = [25, 25, 10]

        self.assertEqual(get_budget(broken_costs, 100), 0)
        self.assertEqual(get_budget(clean_costs, 100), 160)

    def test_empty_args(self):
        with self.assertRaises(TypeError):
            try_default(lambda a: 1, {TypeError: 1})()

    def test_decorator(self):
        @try_default({KeyboardInterrupt: 0})
        def foo(a, b):
            raise KeyboardInterrupt

        self.assertEqual(foo(1, 2), 0)

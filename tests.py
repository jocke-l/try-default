import unittest

from try_default import try_default


def raise_unbound_local_error():
    raise UnboundLocalError


def raise_keyboard_interrupt():
    raise KeyboardInterrupt


class TryDefault(unittest.TestCase):
    def test_core_features(self):
        self.assertEqual(try_default(lambda: [][1], {IndexError: 0}), 0)
        self.assertEqual(try_default(lambda: [1][0], {IndexError: 0}), 1)

    def test_parent_catch(self):
        self.assertEqual(try_default(raise_unbound_local_error, {NameError: 0}), 0)
        self.assertEqual(try_default(raise_keyboard_interrupt, {BaseException: 0}), 0)

    def test_reraise_unhandled_exception(self):
        with self.assertRaises(IndexError):
            try_default(lambda: [][1], {})

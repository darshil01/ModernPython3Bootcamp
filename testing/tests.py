import unittest

from activities import eat, nap, is_funny

class ActivityTests(unittest.TestCase):
    def test_eat_healthy(self):
        self.assertEqual(eat("broccoli", ishealthy=True),
        "I'm eating broccoli, because my body is a temple."
            )
    def test_eat_unhealty(self):
        self.assertEqual(eat("pizza", ishealthy=False),
        "I'm eating pizza, because YOLO!"
            )

    def test_short_nap(self):
        self.assertEqual(nap(1),
        "I'm feeling refreshed after my 1 hour nap"
            )
    def test_long_nap(self):
        self.assertEqual(nap(3),
        "Ugh I overslept. I didn't mean to nap for 3 hours!"
        )

    def test_is_funny_tim(self):
        self.assertFalse(is_funny('tim'), "time should not be funny")

    def test_is_funny_anyone_else(self):
        self.assertTrue(is_funny('blue'), "blue should be funny")
        self.assertTrue(is_funny('tammy'), "tammy should be funny")
        self.assertTrue(is_funny('sven'), "sven should be funny")

if __name__ == "__main__":
    unittest.main()
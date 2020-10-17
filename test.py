#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import app

class TestMyModule(unittest.TestCase):
    
    def test_sum(self):
        self.assertEqual(app.sum(1, 2), 3)

    def test_sum_mala(self):
        self.assertNotEqual(app.sum(1, 2), 3)

if __name__ == "__main__":
    unittest.main()
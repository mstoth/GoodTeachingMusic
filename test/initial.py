import unittest
import os
import json
from common.database import Database
from flask import Flask, render_template, request, session
from models.Piece import Piece

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.app = Flask("testing")
        self.app.secret_key="michael"

    def test_piece_creation(self):
        piece = Piece(title='prelude',composer='bach',instrument='piano')
        self.assertEqual(piece.title,'prelude')


if __name__ == '__main__':
    unittest.main()

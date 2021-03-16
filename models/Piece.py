from common.database import Database
import datetime
import uuid


class Piece(object):

    def __init__(self, title, composer, instrument,_id=uuid.uuid4().hex):
        self.title=title
        self.composer=composer
        self.instrument=instrument
        self._id = uuid.uuid4().hex if _id is None else _id

    def save_to_mongo(self):
        Database.insert(collection='pieces',data=self.json())

    def new_piece(selfself, title, composer, instrument, _id):
        piece = Piece(title=title,
                      composer=composer,
                      instrument=instrument,
                      id = uuid.uuid4().hex if _id is None else _id)
        piece.save_to_mongo()

    def json(self):
        return {
            'id': self._id,
            'title': self.title,
            'composer': self.composer,
            'instrument': self.instrument
        }

    @classmethod
    def from_mongo(clscls, id):
        post_data = Database.find_one(collection='pieces', query={'id',id})


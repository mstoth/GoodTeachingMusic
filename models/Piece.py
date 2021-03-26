from common.database import Database
import datetime
import uuid


class Piece(object):

    def __init__(self, title, composer, instrument,
                 approved=False,created_at='',difficulty='',
                 genre='',recording="",sheet="",updated_at="",comment="",id=uuid.uuid4().hex):
        self.title=title
        self.composer=composer
        self.instrument=instrument
        self.approved=approved
        self.comment=comment
        self.created_at=created_at
        self.difficulty=difficulty
        self.genre=genre
        self.id = uuid.uuid4().hex if id is None else id
        self.recording=recording
        self.sheet=sheet
        self.updated_at=updated_at

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
            'id': self.id,
            'title': self.title,
            'composer': self.composer,
            'instrument': self.instrument,
            'title': self.title,
            'composer': self.composer,
            'instrument': self.instrument,
            'approved': self.approved,
            'comment': self.comment,
            'created_at': self.created_at,
            'difficulty': self.difficulty,
            'genre': self.genre,
            'recording': self.recording,
            'sheet': self.sheet,
            'updated_at': self.updated_at
        }

    @classmethod
    def from_mongo(cls, id):
        post_data = Database.find_one(collection='pieces', query={'id':id})


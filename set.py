# Contain table/class set which represents named multiple of terms

import db_connection as db
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class Set(db.Base):
    """Contain information of set and including terms."""

    __tablename__ = 'sets'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    terms = relationship('Term', back_populates='set')

    def __init__(self, name):
        self.name = name.strip().lower()

    def __repr__(self):
        return f'Set(id={self.id}, name={self.name})'

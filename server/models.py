
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db

# Models go here!

class Owner(db.Model, SerializerMixin):
    __tablename__ = "owners"

    serialize_rules = ("-cats.owner", )

    id = db.Column(db.Integer, primary_key=True)

    # Relationships
    cats = db.relationship("Cat", back_populates="owner")

    pass

class Cat(db.Model, SerializerMixin):
    __tablename__ = "cats"

    serialize_rules = ("-owner.cats", )

    id = db.Column(db.Integer, primary_key=True)

    # Relationships
    owner_id = db.Column(db.Integer, db.ForeignKey("owners.id"))
    owner = db.relationship("Owner", back_populates="cats")

    pass
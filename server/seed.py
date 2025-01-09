#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, Owner, Cat

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!

        print("Deleting data...")
        Owner.query.delete()
        Cat.query.delete()

        print("Creating owners...")
        owner1 = Owner(name=fake.name())
        owner2 = Owner(name=fake.name())
        owner3 = Owner(name=fake.name())

        owners = [owner1, owner2, owner3]
        db.session.add_all(owners)

        print("Creating cats...")
        for owner in owners:
            cat1 = Cat(name=fake.first_name(), owner=owner)
            cat2 = Cat(name=fake.first_name(), owner=owner)
            cat3 = Cat(name=fake.first_name(), owner=owner)

            cats = [cat1, cat2, cat3]
            db.session.add_all(cats)


        db.session.commit()

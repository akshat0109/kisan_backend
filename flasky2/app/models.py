
<<<<<<< HEAD
=======
#Add all common models/tables in this file.

>>>>>>> a04b520446070bdfc33af0bcb0ed4389979c0015
from app import db

class Base(db.Model):
    __abstract__ = True
    created_on =      db.Column((db.DateTime))
    updated_by =      db.Column((db.String(64)))
    updated_on =      db.Column((db.DateTime))


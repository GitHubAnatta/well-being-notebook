from tinydb import TinyDB
import shelve

db = TinyDB("file.db")

db.insert({"fruit":"apple", "count":1})

print(db.all())



with shelve.open("experimental-shelf.db") as shelf:
    shelf['key1'] = {
        'int': 4,
    }
    print(shelf['key1'])



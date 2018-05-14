from tinydb import TinyDB

db = TinyDB("file.db")

db.insert({"fruit":"apple", "count":1})

print(db.all())

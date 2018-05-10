import shelve

with shelve.open("experimental-shelf.db") as shelf:
    shelf['key1'] = {
        'int': 4,
    }

print(shelf)

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



DATABASE_FILE_STR = "wbn_db_file.db"

SQLITE_FALSE_INT = 0
SQLITE_TRUE_INT = 1
SQLITE_NULL_STR = "NULL"
NO_REFERENCE_INT = -1
NO_REST_REMINDER_INT = -1
NO_BREATHING_REMINDER_INT = -1
NOT_USED_YET_INT = -1
NOT_IMAGE_SET_STR = ""



def init():
    print(sqlalchemy.__version__)

# ":memory:"
db_engine = create_engine("sqlite:///" + DATABASE_FILE_STR, echo=True)

Base = declarative_base()


class KindPhrase(Base):
    __tablename__ = "kind_phrases"

    id = Column(Integer, primary_key=True)
    phrase = Column(String)

    def __repr__(self):
        return "<KindPhrase(phrase='{0}')>".format(self.phrase)


# print(KindPhrase())

Base.metadata.create_all(db_engine)


example_phrase = KindPhrase(phrase="instance phrase with space_______")
print(example_phrase.phrase)
Session = sessionmaker()
Session.configure(bind=db_engine)
session = Session()

session.add(example_phrase)
session.commit()

count = 0
for instance in session.query(KindPhrase):
    if count == 1:
        instance.phrase += "edited"
    count += 1

session.commit()

for instance in session.query(KindPhrase):
    print(instance.phrase)


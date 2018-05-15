import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. getting a session, which will be shared for the whole application
# 2.

print(sqlalchemy.__version__)

db_engine = create_engine("sqlite:///sqlalchemy_test.db", echo=True)


class Helper:
    __session = None
    __base_class = None

    @staticmethod
    def get_base():
        if Helper.__base_class is None:
            Helper.__base_class = declarative_base()
            Helper.__base_class.metadata.create_all(db_engine)
        return Helper.__base_class

    @staticmethod
    def get_session():
        if Helper.__session is None:
            # ":memory:"

            SessionClass = sessionmaker()
            SessionClass.configure(bind=db_engine)
            Helper.__session = SessionClass()
        return Helper.__session


class KindPhrase(Helper.get_base()):
    __tablename__ = "kind_phrases"

    id = Column(Integer, primary_key=True)
    phrase = Column(String)

    def __repr__(self):
        return "<KindPhrase(phrase='{0}')>".format(self.phrase)


# print(KindPhrase())


example_phrase = KindPhrase(phrase="new lines")
print(example_phrase.phrase)

Helper.get_session().add(example_phrase)
Helper.get_session().commit()

count = 0
for instance in Helper.get_session().query(KindPhrase):
    if count == 1:
        instance.phrase += "edited"
    count += 1

Helper.get_session().commit()

for instance in Helper.get_session().query(KindPhrase):
    print(instance.phrase)


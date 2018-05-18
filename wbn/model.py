import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Integer
# from sqlalchemy import DateTime
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import wbn.wbn_global


DATABASE_FILE_STR = "wbn_db_file.db"

SQLITE_FALSE_INT = 0
SQLITE_TRUE_INT = 1
SQLITE_NULL_STR = "NULL"
NO_REFERENCE_INT = -1
NO_REST_REMINDER_INT = -1
NO_BREATHING_REMINDER_INT = -1
NOT_USED_YET_INT = -1
NOT_IMAGE_SET_STR = ""


print(sqlalchemy.__version__)


# ":memory:"
db_engine = create_engine("sqlite:///" + DATABASE_FILE_STR, echo=True)

Base = declarative_base()


class SupportPhrase(Base):
    __tablename__ = "support_phrases"

    id = Column(Integer, primary_key=True)
    support_phrase = Column(String)
    last_time_used = Column(Integer, default=NOT_USED_YET_INT)
    # -we use Unix time stamp even though datetime is sort of availalbe
    starred = Column(Boolean, default=False)
    # to add with alembic: image_path = Column(String, )

    def __repr__(self):
        return "<KindPhrase(support_phrase='{0}', last_time_used='{1}', starred='{2}')>".format(
            self.support_phrase,
            self.last_time_used,
            self.starred
        )


# print(KindPhrase())

Base.metadata.create_all(db_engine)


session_class = sessionmaker()
session_class.configure(bind=db_engine)
session = session_class()

"""

example_phrase = SupportPhrase(support_phrase="instance phrase with space_______")
print(example_phrase.support_phrase)

session.add(example_phrase)
session.commit()

count = 0
for instance in session.query(SupportPhrase):
    if count == 1:
        instance.support_phrase += "edited"
    count += 1

session.commit()

for instance in session.query(SupportPhrase):
    print(instance.support_phrase)
"""




compassion_support_phrase_str_list = [
    ("Please be kind to yourself", False),
    ("Look at your mind with compassionate eyes", False),
    ("Is there more you want to say to feel better?", False),
    ("What can i do to feel better?", False),
    ("Is there someone that i can contact to get support?", False),
    ("What can i do long-term to deal with the causes of suffering?", False),
    ("May i hold my suffering with mindfulness and compassion", False),
    ("What other people have had experiences similar to yours?", False),
    ("How would i like to feel today?", False),
    ("What's one small thing i can do to feel better?", False),
    ("How would i like to feel today? What's one small thing i can do go toward this?", False),
    ("What are my needs right now?", False),
    ("What was the most painful thing that happened to me today?", True)
]

"""
"Which people in my life are nonjudgemental, compassionate and caring and truly have my well-being in mind?",
"Which people in my life are nonjudgemental, compassionate and caring and truly have my well-being in mind? How can i spend more time with them?",
"What's one thing i can do to support myself when i feel anxious, sad or depressed?",
"What are some physical activities that i enjoy?",
"Which stories are often playing in my head?",
"Which stories are often playing in my head? What's one story that i can interpret in a different way?",
'Which stories are often playing in my head? Can i "translate to giraffe language"? In other words can i see my needs in this situation?',
"How can i externalize a persistent problem in my life, to reduce blaming?",
"How can i internalize a persistent problem in my life so that i can do something positive for myself?",
"What is one feeling that i have had a hard time with?",
"What's one habit/practice that i can start that can bring more joy/peace into my life",
"What would i say to someone (that i care about) who is also struggling with the same feelings and problems that i am?",
"How can i be a caring friend to myself?",
"What is stopping me from being more kind to myself?",
"What is stopping me from being more kind to myself? What's one small thing that i can do to start removing this obstacle?",
"What's one kind thing that i can say to myself when i'm in need of emotional support?",
"If i loved myself whole heartedly, how would i treat myself each day?",
"If i loved myself whole heartedly, how would i treat myself each day? What's one small thing i can do like this today?",
"What can i learn from a recent mistake?",
"What are my best qualities?",
"""


def populate_db_with_setup_data():
    for (it_support_phrase_str, it_starred_bool) in compassion_support_phrase_str_list:
        session.add(SupportPhrase(support_phrase=it_support_phrase_str, starred=it_starred_bool))


if not wbn.wbn_global.db_file_exists_at_application_startup_bl:
    populate_db_with_setup_data()


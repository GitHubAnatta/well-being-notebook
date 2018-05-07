import csv
import enum
import datetime
import typing
import wbn.db_schema
import wbn.db


class MoveDirectionEnum(enum.Enum):
    up = 1
    down = 2


class MinOrMaxEnum(enum.Enum):
    min = "MIN"
    max = "MAX"


def db_exec(i_sql: str, i_params: tuple=None):
    db_connection = wbn.db.Helper.get_db_connection()
    db_cursor = db_connection.cursor()
    # noinspection PyUnusedLocal
    db_cursor_result = None
    if i_params is not None:
        db_cursor_result = db_cursor.execute(i_sql, i_params)
    else:
        db_cursor_result = db_cursor.execute(i_sql)
    db_connection.commit()
    return db_cursor_result


class SelfCompassionM:
    def __init__(
        self,
        i_id: int,
        i_vert_order: int,
        i_phrase: str,
        i_last_time_used: int,
        i_image_path: str
    ) -> None:
        self._id_int = i_id
        self._vert_order_int = i_vert_order
        self._support_phrase_str = i_phrase
        self._last_time_used_int = i_last_time_used
        self._image_path_str = i_image_path

    @property
    def id(self) -> int:
        return self._id_int

    @property
    def support_phrase(self) -> str:
        return self._support_phrase_str

    @support_phrase.setter
    def support_phrase(self, i_new_phrase: str) -> None:
        self._support_phrase_str = i_new_phrase
        self._update_obj(
            wbn.db_schema.Schema.SelfCompassionSupportPhrasesTable.Cols.support_phrase,
            i_new_phrase
        )

    @property
    def vert_order(self) -> int:
        return self._vert_order_int

    @vert_order.setter
    def vert_order(self, i_new_vert_order: int) -> None:
        self._vert_order_int = i_new_vert_order
        self._update_obj(
            wbn.db_schema.Schema.SelfCompassionSupportPhrasesTable.Cols.support_phrase,
            i_new_vert_order
        )

    @property
    def last_time_used(self) -> int:
        return self._last_time_used_int

    @last_time_used.setter
    def last_time_used(self, i_last_time_used: int) -> None:
        self._last_time_used_int = i_last_time_used
        self._update_obj(
            wbn.db_schema.Schema.SelfCompassionSupportPhrasesTable.Cols.last_time_used,
            i_last_time_used
        )

    @property
    def image_path(self) -> str:
        return self._image_path_str

    @last_time_used.setter
    def last_time_used(self, i_image_path: str) -> None:
        self._image_path_str = i_image_path
        self._update_obj(
            wbn.db_schema.Schema.SelfCompassionSupportPhrasesTable.Cols.image_path,
            i_image_path
        )

    def _update_obj(self, i_col_name: str, i_new_value) -> None:
        SelfCompassionM._update(self._id_int, i_col_name, i_new_value)

    @staticmethod
    def _update(i_id: int, i_col_name: str, i_new_value):
        db_exec(
            "UPDATE " + wbn.db_schema.Schema.SelfCompassionSupportPhrasesTable.name
            + " SET " + i_col_name + " = ?"
            + " WHERE " + wbn.db_schema.Schema.SelfCompassionSupportPhrasesTable.Cols.support_phrase + " = ?",
            (i_new_value, str(i_id))
        )

    @staticmethod
    def add(i_support_phrase: str) -> None:
        vertical_order_last_pos_int = SelfCompassionM._get_highest_or_lowest_sort_value(MinOrMaxEnum.max)
        # -this is the last pos before the new entry has been added, therefore + 1 is added below
        db_exec(
            "INSERT INTO " + wbn.db_schema.Schema.SelfCompassionSupportPhrasesTable.name + "("
            + wbn.db_schema.Schema.SelfCompassionSupportPhrasesTable.Cols.vertical_order + ", "
            + wbn.db_schema.Schema.SelfCompassionSupportPhrasesTable.Cols.support_phrase
            + ") VALUES (?, ?)",
            (vertical_order_last_pos_int + 1, i_support_phrase)
        )

    @staticmethod
    def _get_highest_or_lowest_sort_value(i_min_or_max: MinOrMaxEnum) -> int:
        db_cursor_result = db_exec(
            "SELECT " + i_min_or_max.value
            + " (" + wbn.db_schema.Schema.SelfCompassionSupportPhrasesTable.Cols.vertical_order + ")"
            + " FROM " + wbn.db_schema.Schema.SelfCompassionSupportPhrasesTable.name
        )
        return_value_int = db_cursor_result.fetchone()[0]
        # -0 has to be added here even though there can only be one value

        if return_value_int is None:
            # -to prevent error when the tables are empty
            return 0
        return return_value_int

    @staticmethod
    def get(i_id: int):  # -cannot write type PhrasesM here, unknown why
        db_cursor_result = db_exec(
            "SELECT * FROM " + wbn.db_schema.Schema.SelfCompassionSupportPhrasesTable.name
            + " WHERE " + wbn.db_schema.Schema.SelfCompassionSupportPhrasesTable.Cols.id + "=?",
            (str(i_id),)
        )
        sc_db_te = db_cursor_result.fetchone()
        return SelfCompassionM(*sc_db_te)
        # -the asterisk (*) will "expand" the tuple into separate arguments for the function header

    @staticmethod
    def get_all() -> list:
        ret_phrase_list = []
        db_cursor_result = db_exec(
            "SELECT * FROM " + wbn.db_schema.Schema.SelfCompassionSupportPhrasesTable.name
            + " ORDER BY " + wbn.db_schema.Schema.SelfCompassionSupportPhrasesTable.Cols.vertical_order
        )
        sc_db_te_list = db_cursor_result.fetchall()
        for sc_db_te in sc_db_te_list:
            ret_phrase_list.append(SelfCompassionM(*sc_db_te))
        return ret_phrase_list

    @staticmethod
    def remove(i_id: int) -> None:
        db_exec(
            "DELETE FROM " + wbn.db_schema.Schema.SelfCompassionSupportPhrasesTable.name
            + " WHERE " + wbn.db_schema.Schema.SelfCompassionSupportPhrasesTable.Cols.id + "=?",
            (str(i_id),)
        )

    @staticmethod
    def is_empty() -> bool:
        db_cursor_result = db_exec(
            "SELECT count(*) FROM "
            + wbn.db_schema.Schema.SelfCompassionSupportPhrasesTable.name
        )
        empty_rows_te = db_cursor_result.fetchone()
        # logging.debug("*empty_rows_te = " + str(*empty_rows_te))
        if empty_rows_te[0] == 0:
            return True
        else:
            return False



compassion_support_phrase_str_list = [
    "Please be kind to yourself",
    "Look at your mind with compassionate eyes",
    "Is there more you want to say to feel better?",
    "What can i do to feel better?",
    "Is there someone that i can contact to get support?",
    "What can i do long-term to deal with the causes of suffering?",
    "May i hold my suffering with mindfulness and compassion",
    "What other people have had experiences similar to yours?",
    "How would i like to feel today?",
    "What's one small thing i can do to feel better?",
    "How would i like to feel today? What's one small thing i can do go toward this?",
    "What are my needs right now?",
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
    "{{{{{{{{{What was the most painful thing that happened to me today?"
]


def populate_db_with_setup_data():
    for compassion_support_phrase_str in compassion_support_phrase_str_list:
        SelfCompassionM.add(compassion_support_phrase_str)


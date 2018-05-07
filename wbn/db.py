import datetime
import shutil
import sqlite3
import logging
import wbn.db_schema
import wbn.self_compassion_model
import wbn.wbn_global

SQLITE_FALSE_INT = 0
SQLITE_TRUE_INT = 1
SQLITE_NULL_STR = "NULL"
NO_REFERENCE_INT = -1
NO_REST_REMINDER_INT = -1
NO_BREATHING_REMINDER_INT = -1
NOT_USED_YET_INT = -1
NOT_IMAGE_SET_STR = ""


def get_schema_version(i_db_conn: sqlite3.Connection) -> int:
    t_cursor = i_db_conn.execute("PRAGMA user_version")
    return t_cursor.fetchone()[0]


def set_schema_version(i_db_conn, i_version_it: sqlite3.Connection) -> None:
    i_db_conn.execute("PRAGMA user_version={:d}".format(i_version_it))


def initial_schema_and_setup(i_db_conn: sqlite3.Connection) -> None:
    # Auto-increment is not needed in our case: https://www.sqlite.org/autoinc.html

    i_db_conn.execute(
        "CREATE TABLE " + wbn.db_schema.Schema.SelfCompassionSupportPhrasesTable.name + "("
        + wbn.db_schema.Schema.SelfCompassionSupportPhrasesTable.Cols.id + " INTEGER PRIMARY KEY, "
        + wbn.db_schema.Schema.SelfCompassionSupportPhrasesTable.Cols.vertical_order + " INTEGER NOT NULL, "
        + wbn.db_schema.Schema.SelfCompassionSupportPhrasesTable.Cols.support_phrase + " TEXT NOT NULL, "
        + wbn.db_schema.Schema.SelfCompassionSupportPhrasesTable.Cols.last_time_used + " INTEGER NOT NULL "
        + "DEFAULT" + "'" + str(NOT_USED_YET_INT) + "'" + ", "
        + wbn.db_schema.Schema.SelfCompassionSupportPhrasesTable.Cols.image_path + " TEXT NOT NULL "
        + "DEFAULT" + "'" + str(NOT_IMAGE_SET_STR) + "'"
        + ")"
    )


"""
Example of db upgrade code:
def upgrade_1_2(i_db_conn):
    backup_db_file()
    i_db_conn.execute(
        "ALTER TABLE " + DbSchemaM.ObservancesTable.name + " ADD COLUMN "
        + DbSchemaM.ObservancesTable.Cols.user_text + " TEXT DEFAULT ''"
    )    
"""


upgrade_steps = {
    2: initial_schema_and_setup,
}


class Helper(object):
    __db_connection = None  # "Static"

    # noinspection PyTypeChecker
    @staticmethod
    def get_db_connection() -> sqlite3.Connection:

        if Helper.__db_connection is None:
            Helper.__db_connection = sqlite3.connect(wbn.wbn_global.get_database_filename())

            # Upgrading the database
            # Very good upgrade explanation:
            # http://stackoverflow.com/questions/19331550/database-change-with-software-update
            # More info here: https://www.sqlite.org/pragma.html#pragma_schema_version
            current_db_ver_it = get_schema_version(Helper.__db_connection)
            target_db_ver_it = max(upgrade_steps)
            database_tables_dropped_bool = False
            for upgrade_step_nr_int in range(current_db_ver_it + 1, target_db_ver_it + 1):
                if upgrade_step_nr_int in upgrade_steps:
                    upgrade_steps[upgrade_step_nr_int](Helper.__db_connection)
                    set_schema_version(Helper.__db_connection, upgrade_step_nr_int)

            if not wbn.wbn_global.db_file_exists_at_application_startup_bl:
                wbn.self_compassion_model.populate_db_with_setup_data()

        return Helper.__db_connection


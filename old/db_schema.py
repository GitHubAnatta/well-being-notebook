
class Schema:

    class SelfCompassionSupportPhrasesTable:
        name = "self_compassion_support_phrases"

        class Cols:
            id = "id"  # key
            vertical_order = "vertical_order"
            # title = "title"  # -if not set will be automatically using the first parts of the quote
            support_phrase = "support_phrase"
            last_time_used = "last_time_used"
            image_path = "image_path"
            # last used: written for, selected at random, selected manually

    class SettingsTable:
        name = "settings"

        class Cols:
            id = "id"  # there is only one settings row
            # run_on_startup = "run_on_startup"


class Config(object):
    TG_BOT_TOKEN = os.environ.get("1517012496:AAH0rdr-uyymDSH0Rpr_dpn4ifCxbHNP6EY")
    APP_ID = int(os.environ.get("1805953"))
    API_HASH = os.environ.get("392de18bff66ef71e062f9c674017c63")
    OWNER_ID = int(os.environ.get("1365941967")
    AUTH_CHANNEL = set(int(x) for x in os.environ.get("-1001219257465", "1365941967").split())
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")
    ARIA_TWO_STARTED_PORT = int(os.environ.get("ARIA_TWO_STARTED_PORT", 6800))
    MAX_TG_SPLIT_FILE_SIZE = int(os.environ.get("MAX_TG_SPLIT_FILE_SIZE", 1072864000))
    FINISHED_PROGRESS_STR = os.environ.get("FINISHED_PROGRESS_STR", "█")
    UN_FINISHED_PROGRESS_STR = os.environ.get("UN_FINISHED_PROGRESS_STR", "░")
    TG_OFFENSIVE_API = os.environ.get("TG_OFFENSIVE_API", None)
    CUSTOM_FILE_NAME = os.environ.get("CUSTOM_FILE_NAME", "")
    LEECH_COMMAND = os.environ.get("LEECH_COMMAND", "leech")
    YTDL_COMMAND = os.environ.get("YTDL_COMMAND", "ytdl")
    RCLONE_CONFIG = os.environ.get("RCLONE_CONFIG", "")
    DESTINATION_FOLDER = os.environ.get("DESTINATION_FOLDER", "Torrent Uploads")
    GLEECH_COMMAND = os.environ.get("GLEECH_COMMAND", "gleech")
    INDEX_LINK = os.environ.get("INDEX_LINK", "")
    TELEGRAM_LEECH_COMMAND_G = os.environ.get("TELEGRAM_LEECH_COMMAND_G", "tleech")
    CANCEL_COMMAND_G = os.environ.get("CANCEL_COMMAND_G", "cancel")
    GET_SIZE_G = os.environ.get("GET_SIZE_G", "getsize")
    STATUS_COMMAND = os.environ.get("STATUS_COMMAND", "status")
    SAVE_THUMBNAIL = os.environ.get("SAVE_THUMBNAIL", "savethumbnail")
    CLEAR_THUMBNAIL = os.environ.get("CLEAR_THUMBNAIL", "clearthumbnail")
    UPLOAD_AS_DOC = os.environ.get("UPLOAD_AS_DOC", "False")
    PYTDL_COMMAND_G = os.environ.get("PYTDL_COMMAND_G", "pytdl")
    LOG_COMMAND = os.environ.get("LOG_COMMAND", "log")
    CLONE_COMMAND_G = os.environ.get("CLONE_COMMAND_G", "gclone")
    UPLOAD_COMMAND = os.environ.get("UPLOAD_COMMAND", "upload")
    RENEWME_COMMAND = os.environ.get("RENEWME_COMMAND", "renewme")

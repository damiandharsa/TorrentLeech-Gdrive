from tobrot.sample_config import Config

#Fill your all data, read readme for reference

#FOR CUSTOM COMMANDS READ REAME AND FILL THEM...

class Config(Config):
    TG_BOT_TOKEN= "1517012496:AAH0rdr-uyymDSH0Rpr_dpn4ifCxbHNP6EY"
    APP_ID = 1805953
    API_HASH = "392de18bff66ef71e062f9c674017c63"
    OWNER_ID = 1365941967
    AUTH_CHANNEL = [-1001219257465]
    DESTINATION_FOLDER = "Torrent Uploads" #Name of your folder read readme(not id of the folder)
    #Just don't fill RCLONE_CONFIG vars, insted copy your rclone.conf file in root directory
    #if your wanted to fill -- fill your rclone config like this(Your config may have some extra value or less. so Don't worry)
    RCLONE_CONFIG = """
[DRIVE]
type = drive
client_id = 960520486382-1mb6dt91qcv7n5qedidk8suso18gt22e.apps.googleusercontent.com
client_secret = n8_HBJ6gAjUstn0FKLF7L33R
scope = drive
root_folder_id = 1mn2d5kAfc8-T75ak_7lONXvCVyyHOQXe
token = {"access_token":"dharsavalentine"}
team_drive = 0AE2bWjd3h9gMUk9PVA
"""

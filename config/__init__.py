import os

class Config:
    API_ID = int( os.getenv("api_id","2552785") )
    API_HASH = os.getenv("api_hash","811930f007ed16f87d66bf83813ac7aa")
    CHANNEL = int( os.getenv("channel_files_chat_id","-1001157608302") )
    CHANNEL_USERNAME = os.getenv("channel_username","DaalFile")
    TOKEN = os.getenv("token","1716174020:AAHBraO7zw4St82rSxjaodkDUCgl7qsj7g0")
    DOMAIN  = os.getenv("domain","https://daalfile.herokuapp.com")

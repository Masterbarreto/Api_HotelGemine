import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MONGO_URI = os.getenv("MONGO_URI")
    MONGO_DB = os.getenv("MONGO_DB")
    API_KEY = os.getenv("API_KEY")

    @staticmethod
    def validate():
        if not Config.MONGO_URI or not Config.MONGO_DB or not Config.API_KEY:
            raise ValueError("❌ Configurações incompletas. Verifique o arquivo .env.")

from pymongo import MongoClient, errors
from api.shared.config import Config

def conectar_banco():
    Config.validate()

    try:
        # Tenta conectar ao MongoDB com timeout de 5 segundos
        client = MongoClient(Config.MONGO_URI, serverSelectionTimeoutMS=5000)
        client.server_info()  # força uma conexão para validar

        db = client[Config.MONGO_DB]
        print("✅ Banco está conectado")

    except errors.ServerSelectionTimeoutError as err:
        print("❌ Erro ao conectar ao banco:", err)

def get_database():
    Config.validate()
    try:
        client = MongoClient(Config.MONGO_URI, serverSelectionTimeoutMS=5000)
        client.server_info()  # força uma conexão para validar
        print("✅ Banco está conectado")
        return client[Config.MONGO_DB]
    except errors.ServerSelectionTimeoutError as err:
        print("❌ Erro ao conectar ao banco:", err)
        return None

if __name__ == "__main__":
    conectar_banco()
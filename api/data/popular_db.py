import os
import json
from pymongo.collection import Collection
from api.services.db_service import get_database

def enviar_dados(colecao: str, dados: list[dict]):
    db = get_database()
    if db is None:
        print("❌ Não foi possível obter a instância do banco de dados.")
        return

    collection: Collection = db[colecao]
    try:
        if isinstance(dados, list):
            collection.insert_many(dados)
            print(f"✅ {len(dados)} registros inseridos na coleção '{colecao}'.")
        else:
            collection.insert_one(dados)
            print(f"✅ Banco de dados Populado '{colecao}'.")
    except Exception as e:
        print(f"❌ Erro ao inserir dados: {e}")

# 🔥 ESSA É A FUNÇÃO USADA PELO POETRY
def popular_db():
    print("✅ Executando função popular_db()...")
    current_dir = os.path.dirname(__file__)
    json_path = os.path.join(current_dir, "hotel_faq.json")

    with open(json_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    enviar_dados("hotel_faq", data["hotel_faq"])

# ✅ Isso garante que funcione mesmo rodando direto
if __name__ == "__main__":
    popular_db()

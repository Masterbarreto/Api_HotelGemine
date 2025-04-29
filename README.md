﻿# Gemini Hotel Chat

Este projeto é um chatbot inteligente desenvolvido para o setor hoteleiro. Ele utiliza modelos de linguagem generativa (LLM) para responder perguntas frequentes e interagir com os usuários de forma eficiente. A aplicação combina tecnologias modernas como FastAPI, MongoDB e integração com IA para oferecer uma solução prática e escalável.

---

![Case Study Banner]

Este projeto faz parte de um **case de estudos** sobre o uso de modelos de linguagem generativa (LLM) para criar um chatbot eficiente e funcional. O objetivo é explorar tecnologias modernas como FastAPI, MongoDB e integração com IA para resolver problemas reais no setor hoteleiro.

---

## 📦 Instalação

1. Certifique-se de ter o **Python 3.13** ou superior instalado.
2. Instale as dependências do projeto utilizando o **Poetry**:

    ```bash
   pip install poetry
   ```
    
   ```bash
   poetry install
   ```

---

## 🚀 Comandos Disponíveis

O projeto inclui os seguintes comandos que podem ser executados via **Poetry**:

### 1. **`get_db`**
Verifica a conexão com o banco de dados MongoDB e garante que ele está acessível. Útil para validar se as configurações estão corretas.
```bash
poetry run get_db
```

### 2. **`poplution`**
Popula o banco de dados MongoDB com as informações do arquivo `hotel_faq.json`. Este comando é essencial para carregar as perguntas frequentes no banco de dados.
```bash
poetry run poplution
```

### 3. **`start_chat`**
Inicia o chatbot do Gemini Hotel localmente, permitindo interações diretas no terminal.
```bash
poetry run start_chat
```

### 4. **`start_Api`**
Inicia o módulo de API para acessar o chatbot via endpoints HTTP. Ideal para integrar o chatbot com aplicações externas.

```bash
cd api     
```

```bash
poetry run start_Api
```

---

## 🛠️ Execução

Para iniciar o projeto e interagir com o chatbot, você pode usar o comando `start_Api` para rodar a API e acessar as rotas disponíveis.

```bash
poetry run start_Api
```

A API será iniciada no endereço `http://127.0.0.1:8000`.

---

## 🌐 Rotas da API

Abaixo estão as rotas disponíveis na API:

- **`GET /`**  
  Retorna uma mensagem de boas-vindas para confirmar que a API está funcionando.

- **`POST /start_chat`**  
  Inicia uma nova sessão de chat e retorna um `session_id` único para a interação.

- **`POST /chat_bot`**  
  Envia uma pergunta ao chatbot e retorna a resposta gerada.  
  **Exemplo de payload:**
  ```json
  {
      "session_id": "123e4567-e89b-12d3-a456-426614174000",
      "question": "Qual é o horário de check-in?"
  }
  ```

- **`POST /end_chat`**  
  Finaliza uma sessão de chat com base no `session_id`.

---

## 📂 Estrutura do Projeto

Abaixo está a estrutura principal do projeto e uma breve descrição de cada diretório:

- **`api/services`**  
  Contém os serviços principais, como integração com IA (`gemini_ai.py`) e banco de dados (`db_service.py`).

- **`api/data`**  
  Inclui dados e scripts para popular o banco de dados, como o arquivo `hotel_faq.json`.

- **`api/shared`**  
  Configurações compartilhadas, como variáveis de ambiente e validações (`config.py`).

- **`api/main.py`**  
  Arquivo principal para inicializar a aplicação FastAPI e definir as rotas.

- **`api/run_api.py`**  
  Script para iniciar o servidor FastAPI utilizando o Uvicorn.

---

## 📝 Configuração do Ambiente

Certifique-se de configurar as variáveis de ambiente no arquivo `.env`. Um exemplo de configuração está abaixo:

```
MONGO_URI=mongodb+srv://<usuario>:<senha>@<cluster>.mongodb.net/?retryWrites=true&w=majority
MONGO_DB=ClusterIA
API_KEY="sua-chave-de-api"
```

---

## 📊 Dados do Banco de Dados

O banco de dados MongoDB armazena as perguntas frequentes na coleção `hotel_faq`. O arquivo `hotel_faq.json` contém os dados iniciais que podem ser carregados utilizando o comando `poplution`.

---

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests. Certifique-se de seguir as boas práticas de desenvolvimento e incluir testes para novas funcionalidades.

---

## 📄 Licença

Este projeto é distribuído sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.# Api_HotelGemine


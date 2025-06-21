
# 🧑‍💻 API de Usuários – Flask + Swagger

API REST desenvolvida com **Flask**, usando **SQLAlchemy** para modelagem, **Flasgger** para documentação interativa e **Pytest** para testes automatizados. O projeto realiza operações completas de CRUD (Create, Read, Update, Delete) sobre a entidade `User`.

---

## 📂 Estrutura Geral

```
APIUSER-FLASK/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── models/
│   │   └── user_model.py
│   ├── controllers/
│   │   └── user_controller.py
│   └── routes/
│       └── user_routes.py
├── tests/
│   ├── conftest.py
│   └── test_users.py
├── run.py
└── requirements.txt
```

---

## ⚙️ Como executar o projeto

1. **Clone o repositório**  
   ```bash
   git clone <url-do-repositorio>
   cd APIUSER-FLASK
   ```

2. **Crie o ambiente virtual**  
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   ```

3. **Instale as dependências**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute a aplicação**  
   ```bash
   flask run
   ```

5. Acesse no navegador:  
   🔗 [http://127.0.0.1:5000/apidocs/](http://127.0.0.1:5000/apidocs/)

---

## 📌 Funcionalidades disponíveis

- 📤 Criar usuário (`POST /users`)
- 📥 Listar todos os usuários (`GET /users`)
- 🔍 Consultar por ID (`GET /users/<id>`)
- 📝 Atualizar informações (`PUT /users/<id>`)
- ❌ Excluir usuário (`DELETE /users/<id>`)

---

## 🧾 Tecnologias utilizadas

- Python + Flask
- SQLAlchemy
- Flasgger (Swagger UI)
- Pytest
- SQLite (banco local)



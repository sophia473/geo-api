# 🌍 Geo API - Consulta de Endereços

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Render](https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github)

API desenvolvida em Python com o framework FastAPI para consulta de endereços brasileiros através do CEP, utilizando integração com o serviço externo ViaCEP.

---

# 🚀 Como testar a aplicação

A aplicação está hospedada no Render e pode ser testada diretamente pelo navegador ou por ferramentas como Postman e Insomnia.

## 🔗 Links rápidos

- **Aplicação online:**  
  https://geo-api-sophia.onrender.com

- **Documentação Swagger:**  
  https://geo-api-sophia.onrender.com/docs

---

# 🛠️ Exemplo de uso

Para consultar um endereço, adicione o CEP ao final da URL:

```bash
https://geo-api-sophia.onrender.com/cep/01310100
````

### Exemplo de resposta

```json
{
  "cep": "01310-100",
  "logradouro": "Avenida Paulista",
  "bairro": "Bela Vista",
  "localidade": "São Paulo",
  "uf": "SP"
}
```

---

# ✨ Funcionalidades

* ✅ Consulta de CEP em tempo real via ViaCEP
* ✅ Validação de CEP inválido
* ✅ Tratamento de erros da API
* ✅ Testes automatizados de integração
* ✅ Deploy contínuo utilizando Render
* ✅ Documentação automática com Swagger

---

# 📁 Estrutura do projeto

```text
├── main.py                 # Código principal e rotas da API
├── test_integration.py     # Testes automatizados
├── requirements.txt        # Dependências do projeto
└── README.md               # Documentação do projeto
```

---

# 🛠️ Tecnologias e ferramentas

O projeto foi desenvolvido utilizando:

* **Python 3.10+**
* **FastAPI**
* **HTTPX**
* **Pytest**
* **Uvicorn**
* **Render**
* **Git & GitHub**

---

# ⚙️ Como rodar o projeto localmente

## 1️⃣ Clone o repositório

```bash
git clone https://github.com/sophia473/geo-api.git
```

## 2️⃣ Acesse a pasta do projeto

```bash
cd geo-api
```

## 3️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

## 4️⃣ Execute o servidor

```bash
uvicorn main:app --reload
```

## 5️⃣ Acesse no navegador

```bash
http://127.0.0.1:8000
```

---

# 📌 Endpoints disponíveis

| Método | Endpoint     | Descrição                  |
| ------ | ------------ | -------------------------- |
| GET    | `/`          | Página inicial da API      |
| GET    | `/cep/{cep}` | Consulta endereço pelo CEP |

---

# 🧪 Executando os testes

```bash
pytest
```

---

# 👩‍💻 Autora

Desenvolvido por **Sophia Silva Melo**

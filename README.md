# 🗺️ Geo API

API REST em Python com FastAPI para consulta de endereços a partir de CEP brasileiro.

## 🚀 Aplicação publicada
🔗 (link será adicionado após o deploy)

## Endpoints

| Método | Rota | Descrição |
|---|---|---|
| GET | `/` | Mensagem de boas-vindas |
| GET | `/cep/{cep}` | Retorna endereço completo pelo CEP |

## Como rodar localmente

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Acesse: https://geo-api-sophia.onrender.com
from unittest.mock import AsyncMock, patch, MagicMock
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_cep_valido():
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "cep": "01310-100",
        "logradouro": "Avenida Paulista",
        "bairro": "Bela Vista",
        "localidade": "São Paulo",
        "uf": "SP",
    }

    with patch("httpx.AsyncClient.get", new_callable=AsyncMock, return_value=mock_response):
        response = client.get("/cep/01310100")

    assert response.status_code == 200
    assert response.json()["estado"] == "SP"
    assert response.json()["cidade"] == "São Paulo"

def test_cep_invalido_formato():
    response = client.get("/cep/123")
    assert response.status_code == 400

def test_cep_nao_encontrado():
    mock_response = MagicMock()
    mock_response.json.return_value = {"erro": True}

    with patch("httpx.AsyncClient.get", new_callable=AsyncMock, return_value=mock_response):
        response = client.get("/cep/00000000")

    assert response.status_code == 404
import httpx
from fastapi import FastAPI, HTTPException

app = FastAPI(title="Geo API", description="Consulta de endereços por CEP")

@app.get("/")
def root():
    return {"mensagem": "Bem-vindo à Geo API! Use /cep/{cep} para consultar um endereço."}

@app.get("/cep/{cep}")
async def buscar_cep(cep: str):
    cep_limpo = cep.replace("-", "").strip()

    if not cep_limpo.isdigit() or len(cep_limpo) != 8:
        raise HTTPException(status_code=400, detail="CEP inválido. Use 8 dígitos numéricos.")

    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://viacep.com.br/ws/{cep_limpo}/json/")

    dados = response.json()

    if "erro" in dados:
        raise HTTPException(status_code=404, detail="CEP não encontrado.")

    return {
        "cep": dados.get("cep"),
        "logradouro": dados.get("logradouro"),
        "bairro": dados.get("bairro"),
        "cidade": dados.get("localidade"),
        "estado": dados.get("uf"),
    }
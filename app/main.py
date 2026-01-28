from fastapi import FastAPI

app = FastAPI(title="NF Simples")

@app.get("/")
def health_check():
    return {"status": "ok", "message": "NF Simples rodando"}

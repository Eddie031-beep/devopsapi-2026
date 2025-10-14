from fastapi import FastAPI, HTTPException
app = FastAPI(title="DevOpsAPI 2026", version="0.1.0")

@app.get("/health")
def health(): return {"status":"ok"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None): return {"item_id": item_id, "q": q}

@app.get("/error")
def error(): raise HTTPException(status_code=500, detail="Simulated failure")

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agents.graph import build_graph


app = FastAPI()
graph = build_graph()

class TransactionRequest(BaseModel):
    # You can expand this if you want to accept transactions inline
    path: str = "agents/tools/data/transactions.json"  # default path

@app.get("/")
def root():
    return {"message": "🚀 Banking Insights API is up!"}

@app.post("/analyze")
def analyze_transactions(request: TransactionRequest):
    try:
        result = graph.invoke({})  # Optional: pass {"path": request.path} if using input
        return {"summary": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
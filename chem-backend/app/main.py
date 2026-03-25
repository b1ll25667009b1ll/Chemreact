from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="ChemReact AI Backend")

class ReactionRequest(BaseModel):
    reactants: List[str]

class ReactionResponse(BaseModel):
    input: List[str]
    predicted_products: List[str]
    conditions: Optional[str] = None
    confidence: float

@app.get("/")
def home():
    return {"message": "ChemReact AI Backend Running"}

@app.post("/predict", response_model=ReactionResponse)
def predict(req: ReactionRequest):

    # TEMP RULE-BASED OUTPUT (we will replace with ML later)
    products = [f"Product_of_{r.strip()}" for r in req.reactants]

    return ReactionResponse(
        input=req.reactants,
        predicted_products=products,
        conditions="Heat ~80C, solvent: DMF",
        confidence=0.42
    )

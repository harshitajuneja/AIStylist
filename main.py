from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .schemas import StylistRequest
from .recommender import recommend_dresses
from .database import supabase


app = FastAPI(
    title="AI Stylist API"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def health():

    return {
        "status": "AI Stylist API running"
    }


@app.post("/recommend")
def recommend(request: StylistRequest):

    recommendations = recommend_dresses(
        request
    )

    return {
        "recommendations": recommendations
    }
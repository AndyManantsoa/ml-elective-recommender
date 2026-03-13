from fastapi import APIRouter
from app.models.schemas import RecommendationResponse, UserInput
from app.services.recommender import recommend

router = APIRouter()

@router.post("/recommend", response_model=RecommendationResponse)
def get_recommendations(user: UserInput):

    results = recommend(user)

    return {
        "recommendations": results
    }
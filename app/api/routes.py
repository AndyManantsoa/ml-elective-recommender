from fastapi import APIRouter
from app.models.schemas import UserInput
from app.services.recommender import recommend

router = APIRouter()

@router.post("/recommend")
def get_recommendations(user: UserInput):

    results = recommend(user)

    return {
        "recommendations": results
    }
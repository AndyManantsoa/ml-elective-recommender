from pydantic import BaseModel, Field
from typing import List

class SubjectGrade(BaseModel):
    subject: str
    grade: str


class UserInput(BaseModel):
    userId: str
    cgpa: float = Field(..., ge=0.0, le=10.0)
    semester: int = Field(..., ge=1)
    favoriteSubjects: List[str]
    subjectGrades: List[SubjectGrade]
    areaOfInterest: List[str]


class RootResponse(BaseModel):
    message: str


class HealthResponse(BaseModel):
    status: str


class RecommendationResponse(BaseModel):
    recommendations: List[str]
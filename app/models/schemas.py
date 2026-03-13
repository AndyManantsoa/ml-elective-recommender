from pydantic import BaseModel
from typing import List

class SubjectGrade(BaseModel):
    subject: str
    grade: str

class UserInput(BaseModel):
    userId: str
    cgpa: float
    semester: int
    favoriteSubjects: List[str]
    subjectGrades: List[SubjectGrade]
    areaOfInterest: List[str]
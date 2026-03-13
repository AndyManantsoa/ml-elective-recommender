from app.data.electives import electives
from app.utils.scoring import grade_map

def recommend(user):

    scores = {}

    for elective, data in electives.items():

        score = 0

        # subject strength
        for s in user.subjectGrades:
            if s.subject in data["subjects"]:
                score += grade_map.get(s.grade, 0) * 0.4

        # interest match
        for interest in user.areaOfInterest:
            if interest in data["branches"]:
                score += 2 * 0.3

        # favorite subjects
        for fav in user.favoriteSubjects:
            if fav in data["subjects"]:
                score += 2 * 0.2

        # cgpa bonus
        if user.cgpa >= 8:
            score += 0.5

        scores[elective] = score

    top3 = sorted(scores, key=scores.get, reverse=True)[:3]

    return top3
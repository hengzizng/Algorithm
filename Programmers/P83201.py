from collections import defaultdict


def solution(scores):
    def convert(score):
        converted = "F"

        if score >= 90:
            converted = "A"
        elif score >= 80:
            converted = "B"
        elif score >= 70:
            converted = "C"
        elif score >= 50:
            converted = "D"
        
        return converted


    answer = ""
    student_count = len(scores)

    for col in range(student_count):
        scores_count = defaultdict(int)
        self_score, score_sum = scores[col][col], 0

        for row in range(student_count):
            scores_count[scores[row][col]] += 1
            score_sum += scores[row][col]
        
        min_score, max_score = min(scores_count.keys()), max(scores_count.keys())
        if scores_count[self_score] == 1 and (self_score in {min_score, max_score}):
            answer += convert((score_sum - self_score) / (student_count - 1))
        else:
            answer += convert(score_sum / student_count)

    return answer
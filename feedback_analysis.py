def positive_feedback_percentage(ratings):
    if not ratings:
        return "No ratings available!"
    
    positive = len([rating for rating in ratings if rating >= 4])
    percentage = (positive / len(ratings)) * 100
    return f"Positive Feedback: {percentage:.1f}%"

ratings = [5, 4, 3, 5, 2, 4, 1, 5]
print(positive_feedback_percentage(ratings))

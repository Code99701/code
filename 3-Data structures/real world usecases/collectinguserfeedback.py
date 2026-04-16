# Collecting user feedback
feedback = ["Great service!", "Very satisfied", "Could be better", "Excellent experience"]

# Adding new feedback
feedback.append("Not happy with the service")

# Counting specific feedback
positive_feedback_count = sum(1 for comment in feedback if "great" in comment.lower() or "excellent" in comment.lower() or "execellent" in comment.lower()) 
print(f"Positive Feedback Count: {positive_feedback_count}")


# Printing all feedback
print("User Feedback:")
for comment in feedback:
    print(f"- {comment}")
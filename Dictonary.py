
# Step 1&2
student_scores = {
    "Cameron": 90,
    "Dylan": 85,
    "Lauren": 78,
    "Connor": 92,
    "James": 88
}

# Step 3
print(student_scores)

# Step 4
average_score = sum(student_scores.values()) / len(student_scores)
print(f"Average test score: {average_score:.2f}")

# Step 5
student_name_input = input("Enter a student's name to check their score: ")
if student_name_input in student_scores:
    print(f"{student_name_input}'s score is {student_scores[student_name_input]}")
else:
    print(f"{student_name_input} is not found in the student scores.")

# Step 6
update_student_name = input("Enter the name of the student to update their score: ")
if update_student_name in student_scores:
    new_score = int(input(f"Enter {update_student_name}'s new score: "))
    student_scores[update_student_name] = new_score
    print("Updated student scores:")
    print(student_scores)
else:
    print(f"{update_student_name} is not found in the student scores.")


 
 
 

# Step 7
remove_student_name = input("Enter the name of the student to remove: ")
if remove_student_name in student_scores:
    del student_scores[remove_student_name]
    print("Updated student scores after removing the student")
    print(student_scores)
else:print(f"{remove_student_name}is not found in the student scores")



# Step 8
highest_score = max(student_scores.values())
highest_scorer = [name for name, score in student_scores.items() if score == highest_score][0]
print(f"Highest score : {highest_score}, achevied by {highest_scorer}")



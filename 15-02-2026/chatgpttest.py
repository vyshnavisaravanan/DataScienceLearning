import numpy as np

student_marklist = np.array([
    [78, 85, 92, 88],
    [90,75,85,80],
    [65,70,72,68],
    [88,92,95,90],
    [80,85,88,86]])

student_list = np.array(["aa","bb","cc","dd","ee"])
subject_list = np.array(["eng", "tam","maths","science","history"])

print("student Marklist", student_marklist)

highest_score = np.max(student_marklist)
print("Hightest Score", highest_score)

average_score = student_marklist.mean(axis=1)
print("average Score per student", average_score)

average_subject_score = student_marklist.mean(axis=0)
print("average Score per subject", average_subject_score)

#maximum score per subject
max_score_subject = student_marklist.max(axis=0)
print("max score per subject", max_score_subject)

max_score_position = np.unravel_index(np.argmax(student_marklist), student_marklist.shape)
print("max score postion", max_score_position)

max_score_student_name = student_list[max_score_position[0]]
print("max score of stud", max_score_student_name)

max_score_subject_name = subject_list[max_score_position[1]]
print("max score sub", max_score_subject_name)

for i, subject in enumerate(subject_list):
    student_index =  np.argmax(student_marklist[:,i])
    student_name = student_list[student_index]
    print(f"Top score in {subject}: {max_score_subject[i]} by {student_name}")

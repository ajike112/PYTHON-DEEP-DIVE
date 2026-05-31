
## SUM: Python has lots of built-in functions to help us work with numbers. One of them helps us calculate the sum (the total)

student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
total_score = sum(student_scores)
print(total_score)

## For loop could be used to solve this too.

sum = 0
for score in student_scores:
    sum += score
print(sum)


## Using For loop to loop through each of the scores in the list of student_scores:
max_score = 0
for score in student_scores: 
    if score > max_score:
        max_score = score
print(max_score)
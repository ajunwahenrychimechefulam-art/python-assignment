

student = {
    "Pleasant" : (85, 70),
    "Drake" :(20, 70),
    "josh" : (30, 63),
}
average_score = 0
for student, score in student.items():
    for i in score:
        average_score += sum(score) / len(score)
        print(average_score)


thistuple = ("apple", "orange", "banana","cherry")
i = 0
while i < len(thistuple):
    print(thistuple)
    i = i + 1 + 2



    thistuple = {"apple", "banana","cherry",
    False, 1,2}
    print(thistuple)


    thistuple = {"apple", "banana","cherry",
    True, 1,2}
    print(thistuple)

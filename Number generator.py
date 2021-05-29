"""
If A=1, B=2, C=3...... Z=26, this program will calculate the total value of your name
"""

letter = [" "]
for i in range(97, 123):
    letter.append(chr(i))

answer = 0

Name = input("Enter name in lowercase: ")

for i in range(0, len(Name)):
    number = letter.index(Name[i])
    answer = answer + number

print("Total value:", answer)

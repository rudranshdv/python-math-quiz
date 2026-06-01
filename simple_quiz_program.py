import random

num1 = random.randint(1, 10)
num2 = random.randint(1, 10)

answer = int(input("What is " + str(num1) + " + " + str(num2) + "? "))

correct = num1 + num2

print("Correct answer was:", correct)
print("Your answer was:", answer)
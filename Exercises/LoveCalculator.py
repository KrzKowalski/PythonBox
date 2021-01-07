# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1 = "Krzysztof Kowalski"
name2 = "Justyna Kowalska"
names = name1+name2
t = names.lower().count("t")
r = names.lower().count("r")
u = names.lower().count("u")
e = names.lower().count("e")
first_number = t + r + u + e
l = names.lower().count("l")
o = names.lower().count("o")
v = names.lower().count("v")
e2 = names.lower().count("e")
second_number = l + o + v + e2
score = int(str(first_number) + str(second_number))
# score = int(combined)
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 < score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")

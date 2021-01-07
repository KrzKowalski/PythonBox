#Remember to use the random module 👇
import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
generated_number = random.randint(1, 1000)
if generated_number % 2 == 0:
    result = "Tails"
else:
    result = "Heads"
print(result)
list()
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
figury = [rock, scissors, paper]

wybor_gracza = int(input("Co wybierasz? Wpisz: 0 dla kamień, 1 dla nożyce, 2 dla papier.\n"))
# wybor_gracza = 1
print(figury[wybor_gracza])
wybor_komputera = random.randint(0,2)
print("Komputer wybrał:")
print(figury[wybor_komputera])

if wybor_gracza == 0 and wybor_komputera == 1 or\
        wybor_gracza == 1 and wybor_komputera == 2 or\
        wybor_gracza == 2 and wybor_komputera ==0:
    print("WYGRAŁEŚ!")
elif wybor_gracza == wybor_komputera:
    print("REMIS!")
else:
    print("PRZEGRAŁEŚ!")

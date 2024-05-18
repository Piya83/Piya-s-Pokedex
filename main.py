import csv

#m stands for menu so mline means menu line, we are going to use this to print the menu
mline1 = "1. Display pokemon with their types and statistics"
mline2 = "2. Display the first Pokemon of a Type of your choice"
mline3 = "3. Display all Pokemons with Total Base stat of your choice"
mline4 = "4. Display all Pokemons with a minimum set of stats"
mline5 = "5. Display all lengendary Pokemons of specific Type 1 and Type 2"
mline6 = "6. Surprise me"
mline7 = "7. Quit"

file = open("Pokemon.csv")
text = file.read()

with open('Pokemon.csv') as file:  #opens the csv file
  csv_reader = csv.reader(file)
  rows = list(csv_reader)
List = []
for i in range(1, 801):
  List.append(rows[i])  #creates a list of all the pokemon


def number_of_pokemon(number):  #function to find the number of pokemon
  '''takes an argument and prints out number of pokemon based on the argument'''

  if int(number) < 1 or int(number) > 800:
    print("Please enter a valid number!")
  else:
    print(
        "No  Name                            Type 1  Type 2  Total  HP  Attack  Defense "
        + "Sp. Atk  Sp. Def  Speed  Generation  Legendary")
    for i in range(int(number)):
      print(
          "{0:<4}{1:<32}{2:<8}{3:<8}{4:<7}{5:<4}{6:<8}{7:<8}{8:<9}{9:<9}{10:<7}{11:<12}{12}"
          .format(List[i][0], List[i][1], List[i][2], List[i][3], List[i][4],
                  List[i][5], List[i][6], List[i][7], List[i][8], List[i][9],
                  List[i][10], List[i][11], List[i][12]))


def pokemon_type(type):  #type is the type of pokemon
  '''takes an argument and prints out the first pokemon in the list with the type equal to the argument'''

  not_found = True
  for i in range(800):
    if not_found & (List[i][2] == type or List[i][3] == type):
      print(
          "{0:<4}{1:<32}{2:<8}{3:<8}{4:<7}{5:<4}{6:<8}{7:<8}{8:<9}{9:<9}{10:<7}{11:<12}{12}"
          .format(List[i][0], List[i][1], List[i][2], List[i][3], List[i][4],
                  List[i][5], List[i][6], List[i][7], List[i][8], List[i][9],
                  List[i][10], List[i][11], List[i][12]))
      not_found = False
  if not_found:
    print("No pokemon of this type")


def total_base_stat(stat):  #stat is the total base stat
  '''takes an argument and prints out the first pokemon in the list with the total base stat equal to the argument'''

  for i in range(800):
    if List[i][4] == stat:
      print(
          "{0:<4}{1:<32}{2:<8}{3:<8}{4:<7}{5:<4}{6:<8}{7:<8}{8:<9}{9:<9}{10:<7}{11:<12}{12}"
          .format(List[i][0], List[i][1], List[i][2], List[i][3], List[i][4],
                  List[i][5], List[i][6], List[i][7], List[i][8], List[i][9],
                  List[i][10], List[i][11], List[i][12]))


def min_base_stat(hp, attack, defense, speed):
  '''takes an four argument and prints out the first pokemon in the list that have stats that are greater than or equal to the respective arguments'''

  not_found = True
  for i in range(800):
    if int(List[i][5]) >= hp and int(List[i][6]) >= attack and int(
        List[i][7]) >= defense and int(List[i][8]) >= speed:
      print(
          "{0:<4}{1:<32}{2:<8}{3:<8}{4:<7}{5:<4}{6:<8}{7:<8}{8:<9}{9:<9}{10:<7}{11:<12}{12}"
          .format(List[i][0], List[i][1], List[i][2], List[i][3], List[i][4],
                  List[i][5], List[i][6], List[i][7], List[i][8], List[i][9],
                  List[i][10], List[i][11], List[i][12]))
      not_found = False
  if not_found:
    print("No such powerful pokemon")


def legendary_pokemon(
    type1, type2):  #type1 and type2 are the types of the legendary pokemon
  '''takes two arguments and prints out the first pokemon in the list that have the types equal to the respective arguments'''

  not_found = True
  for i in range(800):
    if List[i][12] == 'TRUE' and (
        (type1 == List[i][2] and type2 == List[i][3]) or
        (type2 == List[i][2] and type1 == List[i][3])):
      print(
          "{0:<4}{1:<32}{2:<8}{3:<8}{4:<7}{5:<4}{6:<8}{7:<8}{8:<9}{9:<9}{10:<7}{11:<12}{12}"
          .format(List[i][0], List[i][1], List[i][2], List[i][3], List[i][4],
                  List[i][5], List[i][6], List[i][7], List[i][8], List[i][9],
                  List[i][10], List[i][11], List[i][12]))
      not_found = False
  if not_found:
    print("No such Legendary pokemon")


def whos_that_starter(
):  #surprise me! Guess the starter pokemon (mudkip, charmander, pikachu)
  '''randomly generates the text art of one of three pokemon and asks the user to guess the pokemon'''

  import random
  starter_num = random.randint(0, 2)
  starter_list = ['Mudkip', 'Pikachu', 'Charmander']
  if starter_num == 0:
    print('''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠴⡖⠉⢱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣔⠁⠀⠃⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⠏⢸⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡎⠀⢸⠀⠀⡆⠀⢠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠈⠀⠀⡇⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠃⠀⡌⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢣⠀⠀⠀⠀⠀⢀⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⠸⠀⠀⠀⠀⠐⠺⠄⣀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⠔⠒⢄
⠀⠀⠀⠀⠀⣠⠞⠁⠀⠇⠀⠀⠀⠀⠀⠀⠈⠑⢄⠀⠀⠀⣀⠔⠊⠀⠀⠀⠀⢸
⠀⠀⠀⠀⡰⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣣⡠⠊⣀⣀⠀⢀⣠⠤⠒⡘
⢀⣤⣄⣰⣧⠀⠀⡰⡆⠀⠀⠀⠀⡔⣆⠀⠀⣴⣿⣿⣿⣿⣿⡟⠊⠁⠀⠀⢠⠃
⠈⣿⣿⣿⣿⣇⠀⠻⠇⠀⠀⠀⠀⠻⠏⠀⣸⣿⣿⣿⣿⣿⣿⣧⣄⠀⠀⠀⠎⠀
⣰⣿⣿⣿⣿⣿⡏⢰⠒⠒⠒⠒⠒⠒⠀⢉⣿⣿⣿⣿⣿⣿⣿⠿⠛⠀⠀⡜⠀⠀
⠉⠛⢿⣿⣿⡿⣿⠧⣀⠀⠀⠀⠀⢀⡠⠚⣿⣿⠿⣿⣿⣿⠹⠉⠐⢒⠞⠀⠀⠀
⠀⠀⠘⠿⠋⠀⡸⠓⠢⠭⣭⠭⠭⠥⢤⠐⠋⠀⠀⢸⠛⠛⠀⢇⡠⠊⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡰⠁⠀⠀⢀⠜⠑⠆⠤⠬⡄⠀⠀⠀⢸⠀⠀⠀⠸⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⢴⠁⠀⢀⡴⠁⠀⢸⠀⠀⢀⠷⡀⠀⠀⢸⠲⢄⠀⠀⢣⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠛⠒⠊⠁⠀⠀⠀⠈⠉⠈⠁⠀⠱⣀⣄⡼⠀⠀⠉⠋⠁⠀⠀⠀⠀⠀''')

  elif starter_num == 1:
    print('''⠸⣷⣦⠤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣤⠀⠀⠀
⠀⠙⣿⡄⠈⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠔⠊⠉⣿⡿⠁⠀⠀⠀
⠀⠀⠈⠣⡀⠀⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⠁⠀⠀⣰⠟⠀⠀⠀⣀⣀
⠀⠀⠀⠀⠈⠢⣄⠀⡈⠒⠊⠉⠁⠀⠈⠉⠑⠚⠀⠀⣀⠔⢊⣠⠤⠒⠊⠉⠀⡜
⠀⠀⠀⠀⠀⠀⠀⡽⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠩⡔⠊⠁⠀⠀⠀⠀⠀⠀⠇
⠀⠀⠀⠀⠀⠀⠀⡇⢠⡤⢄⠀⠀⠀⠀⠀⡠⢤⣄⠀⡇⠀⠀⠀⠀⠀⠀⠀⢰⠀
⠀⠀⠀⠀⠀⠀⢀⠇⠹⠿⠟⠀⠀⠤⠀⠀⠻⠿⠟⠀⣇⠀⠀⡀⠠⠄⠒⠊⠁⠀
⠀⠀⠀⠀⠀⠀⢸⣿⣿⡆⠀⠰⠤⠖⠦⠴⠀⢀⣶⣿⣿⠀⠙⢄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢻⣿⠃⠀⠀⠀⠀⠀⠀⠀⠈⠿⡿⠛⢄⠀⠀⠱⣄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⠈⠓⠦⠀⣀⣀⣀⠀⡠⠴⠊⠹⡞⣁⠤⠒⠉⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⠃⠀⠀⠀⠀⡌⠉⠉⡤⠀⠀⠀⠀⢻⠿⠆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠰⠁⡀⠀⠀⠀⠀⢸⠀⢰⠃⠀⠀⠀⢠⠀⢣⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢶⣗⠧⡀⢳⠀⠀⠀⠀⢸⣀⣸⠀⠀⠀⢀⡜⠀⣸⢤⣶⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠻⣿⣦⣈⣧⡀⠀⠀⢸⣿⣿⠀⠀⢀⣼⡀⣨⣿⡿⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠻⠿⠿⠓⠄⠤⠘⠉⠙⠤⢀⠾⠿⣿⠟⠋''')

  elif starter_num == 2:
    print('''⠀⠀⠀⠀⠀⠀⠀⡀⠠⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡔⠁⠀⠀⠀⠈⠑⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣜⠃⠀⠀⠀⢘⢳⢆⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⠔⠉⠀⠀⠀⠀⣜⠀⢸⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢸⠀⡀⠀⠀⠀⠀⠈⠉⠁⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠀⠀
⠀⡤⢄⣳⣦⠤⠤⠤⠄⣄⡲⡪⠀⡇⠀⢀⡀⢤⠀⠀⠀⢠⠒⢋⠤⠀
⠘⢝⠁⠈⠙⠷⠒⠒⠾⠓⢎⠀⠀⠁⠉⠁⠈⢛⠆⠀⠀⠈⢷⣿⠀⣆
⠀⠀⠑⢄⠀⡘⠀⠀⠀⠀⠀⠣⡀⠀⠀⣀⠔⠁⠀⠀⠀⢀⠃⠹⢷⡄
⠀⠀⠀⠀⠑⡇⠀⠀⠀⠀⠀⠀⢡⠀⠈⡄⠀⠀⠀⠀⠀⠈⠣⢤⡼⠀
⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⡆⠀⠰⠀⠀⠀⠀⠀⠀⠀⡌⡇⠀
⠀⠀⠀⠀⠀⢠⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⡇⠀⠀⠀⠀⢀⠌⢠⠃⠀
⠀⠀⠀⠀⡐⠉⠣⡀⠀⠀⠀⠀⢀⠃⠂⠐⡎⠁⠒⠂⠈⠀⣠⠏⠀⠀
⠀⠀⠀⠀⡀⠀⠀⠈⠒⡤⠀⠠⠊⠀⠀⠀⡠⣀⣀⠠⢄⠾⠃⠀⠀⠀
⠀⠀⣀⡤⠚⠲⠀⠀⠸⡁⠀⢘⠄⠀⠀⣠⠋⠁⠀⠉⠁⠀⠀⠀⠀⠀
⠀⠈⠛⡊⠂⠀⠀⠒⠂⠁⠀⠘⢖⣔⣶⡲⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀''')

  if input(
      "Guess the name of this pokemon: ").title() == starter_list[starter_num]:
    print("Correct!\n")
  else:
    print("You have guessed wrong! The pokemon's name is {}.\n".format(
        starter_list[starter_num]))


choice = 0
while choice != 7:
  print("{0}\n{1}\n{2}\n{3}\n{4}\n{5}\n{6}".format(mline1, mline2, mline3,
                                                   mline4, mline5, mline6,
                                                   mline7))
  choice = input("Enter your choice: ")
  if len(str(choice)) == 0:
    print("Please enter a number from 1-7\n")
  elif choice.isnumeric() and 1 <= int(
      choice
  ) <= 7:  #program checks that the input is a number and that it is between 1 and 7, then runs the corresponding function depending on the number (choice)
    if choice == '1':
      number_of_pokemon(input("Enter number of pokemon to be displayed: "))
    if choice == '2':
      pokemon_type(input("Enter a type: "))
    if choice == '3':
      total_base_stat(input("Enter Total Base stat: "))
    if choice == '4':
      min_base_stat(int(input("Enter minimum HP: ")),
                    int(input("Enter minimum Attack: ")),
                    int(input("Enter minimum Defense: ")),
                    int(input("Enter minimum Speed: ")))
    if choice == '5':
      legendary_pokemon(input("Enter type 1: "), input("Enter type 2: "))
    if choice == '6':
      whos_that_starter()
    if choice == '7':
      break
  else:
    print("Please enter a valid input!")

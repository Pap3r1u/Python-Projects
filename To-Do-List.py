list = []
#prints all the options and asks the user what they would like to do from the choices given
print("Welcome to my To-Do List app")
print()
print("\033[92m1.\033[0m Add Task")
print("\033[92m2.\033[0m Delete Task")
print("\033[92m3.\033[0m Show List")
print("\033[92m4.\033[0m Nothing")
print()

#asks the user what they would like to add and then adds it to the list. 
def add_item():
  task = input("Enter in a task: ")
  list.append(task)
  print()
  for item in list:
    print(item)
  print()

#pops any item that the user wants to delete and then prints out the list again if the item is not in the list the console will let the use know.
def delete_item():
  print()
  for item in list:
    print(item)
  try:
    print()
    delete = int(input("what item would you like to delete.(type in the index value): "))
    list.pop(delete - 1)
    print()
    for item in list:
      print(item)
    print()
    if len(list) == 0:
      print("You have no items in your list!")
      print()
  except IndexError:
    print("That item does not exist! ")



#Shows the list
def show_list():
  print()
  for item in list:
    print(item)
  print()
  
""""
Asks the user what they would like to do from the choices givens the user. Also includes a way to ensure that if the use inputs in a number it doesn't give us an error 
"""

#The first user interaction that determines what the user would like to do out of the 4 options printed out. 

try:
  first = input("what would you like to do: ")
  if type(int(first)) != int:
      raise ValueError
  else:
    first = int(first)
except ValueError:
  print("Your input must be a number")
  exit()

#Main Loop to ensure that the code keeps running till the user doesnt want it to 
while True:
  if first == 1:
    add_item()
    first = int(input("what would you like to do: "))
  elif first == 2:
    delete_item()
    first = int(input("what would you like to do: "))
  elif first == 3:
    show_list()
    first = int(input("what would you like to do: "))
  elif first == 4:
    print("Program Closed")
    exit()
  else:
    print("error")

# write your code here
from typing import Dict

print("Enter the number of friends joining (including you):")
number_of_joining = input()

if int(number_of_joining) <= 0:
    print("No one is joining for the party")
    exit(0)
else:
    print("Enter the name of every friend (including you), each on a new line:")

dict_of_joining: dict[str, int] = {}

i = 0
while i < int(number_of_joining):
    a = input()
    dict_of_joining[a] = 0
    i = i + 1
else:
    print(dict_of_joining)

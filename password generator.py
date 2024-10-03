import random

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

arr1 = []
arr2 = []
arr3 = []


a1 = int(input("enter the number of alphabets you want in ur password"))
a2 = int(input("enter the number of digits you want in ur password"))
a3 = int(input("enter the number of symbols you want in ur password"))

for i in range(1,a1+1):
    arr1.append(random.choice(alphabets))

for i in range(1, a2+1):
    arr2.append(random.choice(digits))

for i in range(1, a3+1):
    arr3.append(random.choice(symbols))

password = "".join( arr1 + arr2 + arr3)
print(f"your password is: {password}")

    




    



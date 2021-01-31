print('Hello, world!')

print("-----------------------------------")
print("")
c = 5

#while
while c != 0:
    print(c)
    c -= 1

print("-----------------------------------")
print("Explicito é melhor do que implicito")
print("-----------------------------------")

c = 5

while c:
    print(c)
    c -= 1

print("-----------------------------------")
print("-------------BREAK-------------")

while True:
    response = input()
    if int(response) % 7 == 0: 
        break
    else:
        print("Não é divisivel por 7")

        
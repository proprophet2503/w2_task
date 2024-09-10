temp = 0
num = int(input("Enter a number: "))

for i in range (2, int((num/2)+1)):
    if (num % i == 0):

        temp+=1
        break


if (temp == 0 and num!= 1):
    print("IT IS A PRIME")
else:
    print("IT IS NOT A PRIME")




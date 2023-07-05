#while
num = int(input("Insert a number:"))

i = 1
while i <= num:
    print(str(i), end=" ")
    i += 1

#for
num = int(input("Insert a number:"))

for i in range(1, num+1):
    print(i, end=" ")    
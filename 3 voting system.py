#Method 1
age = int(input("Insert your age: "))
if age >=18:
    print("vote")
else:
    print("Cant vote")

#Method 2
age = int(input("Insert your age:"))

result = "Vote" if age >= 18 else "Can not vote"

print(result)

#Method 3
age = int(input("Insert your age:"))
print("Vote") if age >= 18 else print("Can not vote")
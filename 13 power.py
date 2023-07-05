# Method 1 using Inbuilt Functions
base = float(input("Enter Base number: "))
expo = float(input("Enter Expo Number: "))
temp=pow(base,expo)

print(temp)

#Method 2 without using inbuilt functions
base = int(input("Enter Base number: "))
expo = int(input("Enter Expo Number: "))

# result = base**expo

result = 1
# for i in range(0, expo):
#     result = result * base

# for i in range(1, expo+1):
#     result = result * base

# for i in range(expo, 0, -1):
#     result *= base

# for expo in range(expo, 0, -1):
#     result *= base

while expo != 0:
    result *= base
    expo -= 1

print(result)
print(expo)
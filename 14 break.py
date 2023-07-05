# Write a program to print all numbers between two intervals, namely low and high. But, with a special condition
# that if any number in the range while getting printed becomes divisible by 13 then you must not print anything
# further and stop. (Do this using the Break Statement)

# Example -

# Input -
# 1 10
# Output 
# 1 2 3 4 5 6 7 8 9 10

# Input
# 10 20
# Output
# 10 11 12 13

# Input
# -18 0
# Output
# -18 -17 -16 -15 -14 -13

#Method (For Loop)
low, high = input("Enter the two numbers: ").split()

for i in range(int(low), int(high)+1):
    print(i, end = " ")
    if i % 13 == 0:
        break


#Method2 (While Loop)
list1 = list(map(int, input("Numbers: ").split()))
# list1 = [int(x) for x in input("Numbers: ").split()]
# list1 = [int(x) for x in input("Numbers: ").split(',')]

low = list1[0]
high = list1[1]

while low <= high:
    print(low, end=" ")
    if int(low) % 13 == 0:
        break
    low += 1
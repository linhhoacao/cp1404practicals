# a. count in 10s from 0 to 100:
for i in range(0, 110, 10):
    print(i, end=' ')
print()

# b. count down from 20 to 1:
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c. print n stars. Ask the user for a number, then print that many stars (*), all on one line.
num_stars = int(input("Number of stars: "))
for _ in range(num_stars):
    print("*", end='')
print()

# d. print n lines of increasing stars. Using the same number as above, print lines of increasing stars, starting at 1 with no blank line.
for i in range(1, num_stars + 1):
    for _ in range(i):
        print("*", end='')
    print()
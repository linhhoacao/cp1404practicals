import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_QUICK_PICK = 6

def generate_quick_picks(num_quick_picks):
    for _ in range(num_quick_picks):
        numbers = random.sample(range(MIN_NUMBER, MAX_NUMBER + 1), NUMBERS_PER_QUICK_PICK)
        numbers.sort()
        print(*numbers, sep=" ")

num_quick_picks = int(input("How many quick picks? "))
generate_quick_picks(num_quick_picks)
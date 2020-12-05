import random

# PLEASE Edit

#This is a lotto machine you win some money for guessing right

nums = [1,2,3,4,5,6,7,8,9]
other_nums = [0,1,2,3,4,5,6,7,8,9]
for i in range(5):
    luckey_numbers = nums [random.randint(0,8)], other_nums [random.randint(0,9)]

player = input('ENTER 2 NUMBERS BETWEEN 1-9 SEPARATED BY COMMA!!:')
if len(player) >= 4:
        raise 'AN ERROR OCCURED!!!  TRY 2 NUMBERS ONLY'
if (player) != (luckey_numbers):
    print('Better luck next powerball draw')
else:
    print(f'congrats you earned your self $50 for picking{luckey_numbers}')
    
print(f"YOUR SCORES: {player}")
print(f"Today's luckey numbers {luckey_numbers}")


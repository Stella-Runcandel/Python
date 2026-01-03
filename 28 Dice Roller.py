import random
#● ┌ ┐ │ └ ┘
dice_art = {
1: ("┌─────────┐",
    "│         │",
    "│    ●    │",
    "│         │",
    "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}
'''for dice in dice_art:
    dice_o_int = dice_art[dice]
    for line in dice_o_int:
        print(line)'''

dice = []
total = 0
number_of_dice = int(input("How many dice"))

for die in range(number_of_dice):
    dice.append(random.randint(1,6))

print(dice)
'''
for die in dice:
    for line in dice_art[die]:
        print(line)
'''
#here orignally i wrote dice_art.get(dice[die][row]) here it broke cause it's tryna see the row like what is it indexing? uc an't index number
#but if u add a pranthesis about dice[dice] all of a sudden [row] is applied to the value of get(dice[dice]) which means the tupple
#thus the row is appliekd to the relavant tupple


for row in range(5):
    for die in dice: 
        print(dice_art.get(die)[row],end = "")
    print() 

'''for row in range(5):
    for die in range(len(dice)): 
        print(dice_art.get(dice[die])[row], end="")
    print() '''


for dice_num in dice:
    total += dice_num
print(f'Total: {total}')

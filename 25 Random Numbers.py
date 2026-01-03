import random
low = 1
high = 100
num = random.randint(low,high)
num2 = random.random()
print(num)
print(num2)
options = ("rock", "paper", "scissors")
option = random.choice(options)
print(option)
cards = ['2','3','4','5','6','7','8','9','10','J',"k","Q","A"]

random.shuffle(cards)

print(cards)

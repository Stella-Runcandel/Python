# format specifiers = {value:flags} format a value based on what
# flags are inserted; flags are like instructions given to python on how to print

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator
price_1 = 3.14159
price_2 = -9870.65
price_3 = 1200.34

print(f'Price 1 is ${price_1:.2f}') #after collen the . means desimals to be displayed, then numebr is number of desimals and f indicates floating point num
print(f'Price 2 is ${price_2:.2f}') #or to .1f or .3f (roudning takes place)
print(f'Price 3 is ${price_3:.2f}')
print(f'Price 1 is ${price_1:10}') #to give space to in wich it has to give value just add number after :
print(f'Price 1 is ${price_1:010}') #to give space to in wich it has to give value just add number after : if the number is preceed by 0
#it's 0 padded... x many zeros infornt of it until the zeros and the number combien to take up given spaces
print(f'Price 1 is ${price_1:<10}') #to justifyi it to the left, other flags can be stcked together? this one left justifeid and makes 10 spaces
print(f'Price 1 is ${price_1:>10}') #to justifyi it to the right, other flags can be stcked together? this one right justifeid and makes 10 spaces
#justifyi means ig to push?
print(f'Price 1 is ${price_1:^10}') #to center the value in given spaces
print(f'Price 1 is ${price_1:+}') #to display positive or negative valeu depends on number
print(f'Price 1 is ${price_1: }') #to display a space infront of positive numbers, aligns them evenly with negative ones
#by align i mean the starting poitns align evenely
print(f'Price 1 is ${price_3:,}') #to seprate thousands 

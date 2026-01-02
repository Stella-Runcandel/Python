#nexterd loops -> a loop in a loop, can be any type of loop

for x in range(0,3): #what if we want to print it 3x we could also do range (3) do note this goes form 0 to 2 
    for y in range (1,10): #coutns form 1 to 9
        print(y, end = "")
    print()

#rectangle generator
rows = int(input("Enter in the # of rwos: "))
columns = int(input("Enter in the # of columns: "))
symbol = input("Enter a symbol to use: ")
for z in range(rows): #what if we want to print it 3x we could also do range (3) do note this goes form 0 to 2 
    for a in range (columns): #coutns form 1 to 9
        print(symbol, end = " ")
    print()
#for loop -> executes block of code for fixed amount of time
# you can itterate anything which is iterable < over a range, string, sequence, etc.>

for x in range(1,11):
    print(x)
for x in reversed(range(1,11)):
    print(x)
print(f'Happy New Year')
for x in range(1,11, 2):
    print(x)

credit_card_number = '1234-5678-9101-1121'
#remember contiute and break #continue skips to the next iteration
for x in range (1,21):
    if x== 13:
        continue
    else:
        print(x)
#break stops it
for x in range (1,21):
    if x == 13:
        break
    else: 
        print(x)
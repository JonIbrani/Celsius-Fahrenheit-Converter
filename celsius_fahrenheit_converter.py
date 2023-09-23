def convert_cel_to_far(C):
    F = C * 9/5 + 32    
    print(f'{F}°F')
      

def convert_far_to_cel(F):
    C = (F - 32) * 5/9
    print(f'{C}°C')

print('This program converts the celsius to fahrenheit also reverse.')
user = int(input(f'Write {1} if you want to convert celsius to fahrenheit or press {2} if you want to do the reverse.\n' ))

if user == 1:
    x = int(input("Write the value of celsius you want to convert:\n"))
    convert_cel_to_far(x)


elif user ==2:
    y = int(input("Write the value of fahrenheit you want to convert:\n"))
    convert_far_to_cel(y)

else:
    print("You need to write either 1 or 2.")






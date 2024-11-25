# Apollos Eastman
# Nov 25 2024
# While Loops

a = True
temps = []

while a == True:
    temp = int(input('Enter a tempurature in Fahrenheit (-9999 to quit):'))
    if temp == -9999:
        break
    else:
        temps.append(temp)

print(f'Temperatures inputted: {temps}')
average = sum(temps) / len(temps)
print (f'Average tempurature: {average:.2f}°F')

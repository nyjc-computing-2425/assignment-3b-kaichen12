stdform = input('Enter a number in scientific notation: ')
stdform = stdform.strip(' ')
stdform1 = stdform.replace('x10^','E')
string = f'This number in E notation is {stdform1}.'
print(string)

# Type your code below

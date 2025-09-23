# identify the parts of code below

def double_amount(amount):
    double = amount * 2
    print('Twice that amount is ' + str(double))
    return double

num = int(input('Enter a number:\n'))
print(double_amount(num))
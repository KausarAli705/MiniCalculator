def main():
    keep_going = 'y'
    while keep_going == 'y':
        x = int(input("enter the number for x: "))
        y = int(input("enter the number for y: "))
        print('---------------------------')
        print("which operation do you want to apply :")
        print("1-addition")
        print("2-subtraction")
        print("3-multipication")
        print("4-division")
        print('---------------------------')
        choice = int(input("enter your option:"))
        print('---------------------------')
        if choice == 1:
            addition(x, y)
        elif choice == 2:
            subtraction(x, y)
        elif choice == 3:
            multipicaton(x, y)
        elif choice == 4:
            if x >= y:
                division(x, y)
            else:
                print('Not possible try with another numbers?')
                print('x must be greater than y, inorder to perform the division')
        else:
            print("best of luck")
            print('========================')
        print('========================')
        print('')
        print('Do you want to try again: ')
        keep_going = input('enter y for Yes OR n for No')


def addition(x, y):
    add = x + y
    print(x, '+ ', y, ' =', add)


def subtraction(x, y):
    sub = x - y
    print(x, '- ', y, ' =', sub)


def multipicaton(x, y):
    mul = x * y
    print(x, 'x ', y, ' =', mul)


def division(x, y):
    div = x / y
    print(x, '/ ', y, ' =', div)


main()

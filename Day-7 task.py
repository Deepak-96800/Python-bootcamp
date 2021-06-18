def func(x, y):
    result = x+y
    print('Addition :', x, "+", y, "=", result)
    result1 = x-y
    print('Subtraction :', x, "-", y, "=", result1)
    result2 = x/y
    print("Division :", x, "/", y, "=", result2)
    result3 = x*y
    print('Multiplication :', x, "*", y, "=", result3)


n1 = int(input("Enter the first number : "))
n2 = int(input("Enter the second number : "))
func(n1, n2)


def covid(name, temp):
    print('Patient Name : ', name)
    if temp == '':
        print('Body Temperature : 98 degree')
    else:
        print("Body Temperature : ", temp, 'degree')


name = input("Enter Patient Name : ")
temp = input('Enter Body Temperature : ')
covid(name, temp)

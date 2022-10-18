#Functions
def add(x, y):
    result = x + y
    return result
print(add(1, 2))


def mutiply(x, y):
    result = x * y
    return result
print(mutiply(2, 10))


def greet(name):
    result = "Hi, " + name + ", nice to meet you"
    return result
print(greet('Jeff'))


def absolute_value(number):
    if number >= 0:
        return number
    else:
        return -number
print(absolute_value(-10))
print(absolute_value(50))
print(absolute_value(0))


#Arguments (當你定義函數(define function)的時候，用的是parameters，當你實際調用函數（call function）的時候，傳入的實際內容就是arguments)
    # 1. Default arguments
    # 2. Required arguments
    # 3. Keyword arguments
    # 4. Variable number of arguments (unkown number at time of definition)

def power(x, y=2): #(Defult Argument)
    result = x ** y
    return result
print(power(4))
print(power(5, 3))  # 更改function的設定（y由2改成3）


def divide(x, divisor): #（Required Argument）
    result = x / divisor
    return result
x = 100
print(divide(x, 10))
print(divide(10, x))


def divide(x, divisor): #（Keyword Argument）
    result = x / divisor
    return result
x = 60
print(divide(x=x, divisor=3))
print(divide(divisor=3, x=x))


def summation(*number): #重要！！！（variable number of Argument）
    total = 0
    for x in number:
        total += x
    return total
a = 2
b = 3
c = 4
d = 10
print(summation(a, b, c, d)) #若要在function中輸入多組資料，function內容設定要加*


#Understanding Scope (內函數和外函數) (global v.s local scope)
def my_function():
    number = 22
    print('Inside function number = ',number)
number = 44
my_function()
print('Outside function number = ', number)


#Anonymous Functions (用lambda簡化function??)
double = lambda x: x * 2
print(double(5))

sum = lambda x, y: x + y
print(sum(7,9))

number_list = [1,2,5,8,12,15,20,6]
filtered_list = list(filter(lambda x: x<10, number_list))
print(filtered_list)

number_list = [1,2,5,8,12,15,20,6] #用map函數去square數字(做平方)
squared_number = list(map(lambda x: x * x, number_list))
print(squared_number)
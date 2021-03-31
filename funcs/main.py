#
# def add(a, b):
#     return a + b
#
# def sec():
#     print(22323)
#
# def main():
#     print(123)
#     print('result:', add(4, 7))
#
# main()


# def count(a):
#     return a
# @
# def power(a, pow=2):
#
# def count_val(counter, *args):
#     print(counter)
#     print(args)
#
# count_val()

def my_shiny_new_decorator(function_to_decorate):
    # Внутри себя декоратор определяет функцию-"обёртку". Она будет обёрнута вокруг декорируемой,
    # получая возможность исполнять произвольный код до и после неё.
    def the_wrapper_around_the_original_function():
        print("Я - код, который отработает до вызова функции")
        function_to_decorate() # Сама функция
        print("А я - код, срабатывающий после")
    # Вернём эту функцию
    return the_wrapper_around_the_original_function

# Представим теперь, что у нас есть функция, которую мы не планируем больше трогать.
def stand_alone_function():
    print("Я простая одинокая функция, ты ведь не посмеешь меня изменять?")

stand_alone_function()
# Однако, чтобы изменить её поведение, мы можем декорировать её, то есть просто передать декоратору,
# который обернет исходную функцию в любой код, который нам потребуется, и вернёт новую,
# готовую к использованию функцию:
stand_alone_function_decorated = my_shiny_new_decorator(stand_alone_function)
stand_alone_function_decorated()
print('!!!!!!!!!!!!!!!!!!!!!')
stand_alone_function = my_shiny_new_decorator(stand_alone_function)
stand_alone_function()
print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')

@my_shiny_new_decorator
def another_stand_alone_function():
    print("Оставь меня в покое")
another_stand_alone_function()
print('33333434343434343434')

def bread(func):
    def wrapper():
        print()
        func()
        print("<\______/>")
    return wrapper

def ingredients(func):
    def wrapper():
        print("#помидоры#")
        func()
        print("~салат~")
    return wrapper

def sandwich(food="--ветчина--"):
    print(food)

sandwich()
sandwich = bread(ingredients(sandwich))
sandwich()
print('))))))))))))))))))(((((((((((((((((((((')

@bread
@ingredients
def sandwich(food="--ветчина--"):
    print(food)

sandwich()
# square_generator=(i*i for i in range(5))
# for i in square_generator:
#     print(i)
# def get_odd_generator():
#     n=1
#     n+=2
#     yield n
#     n+=2
#     yield n
#     n+=2
#     yield n
# numbers=get_odd_generator()
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))

# def make_pretty(func):
#     def inner():
#         print("I got decorted")
#         func()
#     return inner
# def ordinary():
#     print("I am ordinary")
# print(ordinary)
# pretty=make_pretty(ordinary)
# print(pretty())

def make_bold(func):
    def inner(text):
        result=func(text)
        return f"<b>{result}</b>"
    return inner
def greet(name):
    return f"Hello,{name}!"
decorated_greet=greet("John")
print(decorated_greet)
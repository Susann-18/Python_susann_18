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

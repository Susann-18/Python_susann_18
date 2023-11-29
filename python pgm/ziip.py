# mytuple=("apple","orange","cherry")
# x=iter(mytuple)
# print(next(x))
# print(next(x))
# print(next(x))
# mylist_1=[1,2,3]
# mylist_2=["one","two","three"]
# zip(mylist_1,mylist_2)
# data=[1,2,3,4,5]
# result=map(lambda x:x*2,data)
# print(result)
# print(list(result))
# result1=filter(lambda x:x%2==0,data)
# print(list(result1))
# from functools import reduce
# result3=reduce(lambda x,y:x*y,data)
# print(result3)
# number_list=range(-5,5)
# less_than_zero=list(filter(lambda x:x<=0,number_list))
# print(less_than_zero)
# x=lambda x:x*2
# print(x(5))



# def default_arg(id,name="spectrum"):
#    print("ID",id)
#    print("Name",name)
#    return
# default_arg(10)
# def required_arg(str):
#     print("input string",str)
#     return
# required_arg("spectrum")
# program to find sum of multiple numbers 

# def find_sum(*numbers):
#     result = 0
#     for num in numbers:
#         result = result + num
#     print("Sum = ", result)
# find_sum(1, 2, 3)
# find_sum(4, 9)
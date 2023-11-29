# 1
# y=(int(input("Enter a integer:")))
# def check_even_odd(number):
#     if number % 2 == 0:
#         print("It is an even number.")
#     else:
#         print("It is an odd number.")
# check_even_odd(y)
# 2
# def create_square_dict():
#     square_dict={}
#     for number in range(1,21):
#         square_dict[number]=number**2
#     return square_dict
# result_dict=create_square_dict()
# print(result_dict)
# 3
# x=(str(input("Enter  a string:")))
# def remove_vowels(string):
#     vowels=['a','e','i','o','u','A','E','I','O','U']
#     result=""
#     for char in string:
#         if char not in vowels:
#             result+=char
#             return result
# y=remove_vowels(x)
# print(y)
# 4
# num=10
# result=list(map(lambda x:2*x,range(num)))
# print("Power of 2:")
# for i in range(num):
#    print("2 raised to power",i,"is",result[i])
# 5
# def bubble_sort(arr):
#     n=len(arr)
#     for i in range(n):
#         for j in range(0,n-i-1):
#             if arr[j]>arr[j+1]:
#                 arr[j], arr[j+1]=arr[j+1],arr[j]
# arr=[60,30,20,10,5,78,100,95,102]
# print("orginial array:",arr)
# bubble_sort(arr)
# print("sorted array:",arr)
# 6
# def binarysearch(array,x,low,high):
#         while low<=high:
#             mid=low +(high-low)//2
#             if array[mid]==x:
#                 return mid
#             elif array[mid]<x:
#                 low=mid+1
#             else:
#                 high=mid-1
#         return -1
# array=[3,4,5,6,7,8,9]
# x=4
# result=binarysearch(array,x,0,len(array)-1)
# if result !=-1:
#     print("Element is present at index:"+str(result))
# else:
#     print("Not Found")
# 7
# def test(keys,values):
#     return dict(zip(keys,values))
# l1=['a','b','c','d','e','f']
# l2=[1,2,3,4,5]
# print("Original list:")
# print(l1)
# print(l2)
# print("\n Combine the value of the two list dictionary: ")
# print(test(l1,l2))
# 8
# n=10
# m1,m2=0,1
# print("fibonacci series:",m1,m2,end="")
# for i in range(2,n):
#     m3=m1+m2
#     m1=m2
#     m2=m3
#     print(m3,end="")
#     print()
# 9
# x=(int(input("Enter a number:")))
# num = 7
# factorial = 1
# if num < 0:
#    print("Sorry, factorial does not negative numbers")
# elif num == 0:
#    print("The factorial of 0 is 1")
# else:
#    for i in range(1,num + 1):
#        factorial = factorial*i
#    print("The factorial of",num,"is",factorial)


# 11
# n=(int(input("Enter a number:")))
# def generator_divide(n):
#     for num in range(n+1):
#         if num%5==0 and num%7==0:
#             yield num
# result_generator=generator_divide(n)
# result=','.join(map(str,result_generator))
# print(f"Numbers divide by 5 and 7 between 0 and {n}:{','.join(map(str,result))} ")
# 12
# n=(int(input("Enter a number:")))
# def even_number(n):
#     for num in range(n+1):
#         if num%2==0:
#             yield num
# result=even_number(n)
# print(f"Enter a even numbers between 0  {n}:{','.join(map(str,result))}")
# 13
# def insertionsort(array):
#     for i in range(1,len(array)):
#         key=array[i]
#         j=i-1
#         while j>=0 and key <array[j]:
#             array[j+1]=array[j]
#             j=j-1
#             array[j+1]=key
# y=[9,5,2,3,1,4,6,7]
# insertionsort(y)
# print('sorted Array in Ascending order:')
# print(y)
# 14
# def linear(array,n,x):
#     for i in range(0,n):
#         if (array[i]==x):
#             return i
#     return-1
# y=[2,3,4,1,0,5]
# x=5
# n=len(y)
# result=linear(y,n,x)
# if(result==-1):
#     print("Element not found")
# else:
#     print("Element found at index:",result)
# 15
# def selectionSort(array, size):
#     for step in range(size):
#         min_idx = step
#         for i in range(step + 1, size):
#             if array[i] < array[min_idx]:
#                 min_idx = i
#         (array[step], array[min_idx]) = (array[min_idx], array[step])
# y = [-2, 45,33, 0, 11, -9]
# size = len(y)
# selectionSort(y, size)
# print('Sorted Array in Ascending Order:')
# print(y)
# 16
# li=[]
# x=(int(input("Enter the number of elemnet:")))
# for i in range(1,x+1):
#     y=int(input("Enter the element:"))
#     li.append(y)
# li.sort()
# print("The sorted list:",li)
# print("The second smallest value of this list:",li[1])
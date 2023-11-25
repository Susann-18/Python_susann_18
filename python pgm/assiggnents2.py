# #  1positive or negative
# sum=(int(input("Enter a number:")))
# if sum>0:
#     print("positive")
# else:
#     print("negative")
# # 2swap varaibles
# x=10
# y=50
# temp=x
# x=y
# y=temp
# print("value of x:",x)
# print("value of y:",y)

# # 3year leap
# num=(int(input("Enter the is leap year")))
# if(num%4)==0:
#     if(num%100)==0:
#         if(num%400)==0:
#             print("the is leap year")
#         else:
#             print("the is not leap year")
#     else:
#         print("the is not leap year")
# else:
#     print("the is not leap year")
# # 4odd or even
# num=(int(input("Enter a  number:")))
# if num%2==-0:
#     print("even")
# else:
#     print("odd")

# 5fibonacci
# n=10
# m1,m2=0,1
# print("fibonacci series:",m1,m2,end="")
# for i in range(2,n):
#     m3=m1+m2
#     m1=m2
#     m2=m3
#     print(m3,end="")
#     print()
# # 6
# rows=5
# for i in range(0,rows):
#     for j in range(0,i+1):
#         print("*",end="")
#     print("\n")

# # 7 prime number
# lower=10
# upper=30
# print("prime numbers between",lower , upper)
# for num in range(lower, upper +1):
#    if num>1:
#        for i in range(2,num):
#            if (num % i)==0:
#                break
#        else:
#         print(num)

# # 8
# start=1
# end=50
# for sum in range(start,end+1):
#     if(sum%2)==0:
#         print(sum,end=" ")

# # 9
# sum=5
# def fact(m):
#     for i in range(2, m+1):
#         print("factorial of",sum ,"is")
#         fact(sum)

# # 10
# st = 'malayalam'
# j = -1
# flag = 0
# for i in st:
#     if i != st[j]:
#         flag = 1
#         break
#     j = j - 1
# if flag == 1:
#     print("NO")
# else:
#     print("Yes")

# # 11
# min_val=100
# max_val=200
# for num in range(min_val,max_val+1):
#     if num%2==0:
#         print(num, "is divisible by 7")

# # 12 multiplcation table
# # num=(int(input("Enter a number:")))
# # print("Multiplcation Table of",num)
# # for i in range(1,11):
# #     print(num,"X",i,"=",num*i)

# # 13
# l=int(input("Length : "))
# w=int(input("Width : "))
# area=l*w
# perimeter=2*(l+w)
# print("Area of Rectangle : ",area)
# print("Perimeter of Rectangle : ",perimeter)

# # 14
# num=2
# sum=(int(num*(num+1)/2))
# print(sum)

# # 15
# def is_armstrong(num):
#     num_str = str(num)
#     n = len(num_str)
#     sum = 0
#     for digit in num_str:
#         sum += int(digit)**n
#     if sum == num:
#         return True
#     else:
#         return False
# num=153
# print(is_armstrong(num))

# # 16
# num1=10
# num2=16
# num3=20
# if (num1 >= num2) and (num1 >= num3):
#    largest = num1
# elif (num2 >= num1) and (num2 >= num3):
#    largest = num2
# else:
#    largest = num3

# print("The largest number is", largest)
# # 17
# import string
# test_str = 'hii, is best: for the thanks ;'
# test_str = test_str.translate(str.maketrans('', '', string.punctuation))
# print(test_str)
# # 18
# rows = int(input("Enter number of rows: "))

# for i in range(rows+1):
#     for j in range(i):
#         print(i , end=" ")
#     print("\n")

# # 19
# import re
# string = "hii hello world"
# vowels = r'[hello world]'
# count = len(re.findall(vowels, string))
# print(count) 

# # 20
# def subComplex( z1, z2):
#     return z1-z2
# z1 = complex(2, 3)
# z2 = complex(1, 2)
# print( "complex is : ", subComplex(z1, z2))

# #  21 
# num_1=10
# num_2 = 11
# num3=num_1 % num_2
# num4=num_1-num_2
# num5=num_1 * num_2
# print(num3)
# print(num4)
# print(num5)

# # 22
# num_1=7
# num_2=6
# # num_3=num_1<num_2
# # num_4=num_1>num_2
# # num_5=num_1<=num_2
# # num_6=num_1>=num_2
# num_7=num_1=num_2
# # print(num_3)
# # print(num_4)
# # print(num_5)
# # print(num_6)
# print(num_7)

# # 23
# num_1=3
# num_2=4
# # num_3=(num_1<num_2)and(num_1!=num_2)
# # num_4=(num_2>=num_1)or(num_1>num_2)
# num_5=not(num_1==num_2)
# print(num_5)
# # print(num_4)
# print(num_3)

# # 24
# i=1
# while(i<6):
#     i=i+1
#     print(i)

# # 25
# customer_num=5
# invoice_num=1212
# print("Invoice No(s):")
# while(customer_num>0):
#     print("INV-",invoice_num)
#     invoice_num=invoice_num+3
#     customer_num=customer_num-1 
# # 26
# string=input(" Enter a String:")
# if len(string)<5:
#     print(string)
# elif string[-3:]=='ing':
#     print(string + 'php')
# else:
#     print(string + 'java')
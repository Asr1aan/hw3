# Salaries
# num_1 = int(input())
# num_2 = int(input())
# num_3 = int(input())
# l = [num_1, num_2, num_3]
# print(max(l) - min(l))

# Boring number
# num = set(input())
# if len(num) == 1:
#     print("Boring")
# else:
#     print("Interesting")

# Largest Number
# num = int(input())
# lst = []
# while num != 0:
#     a = num % 10
#     lst.append(a)
#     num //= 10
# lst.reverse()
# lst_sorted = lst.copy()
# lst_sorted.sort(reverse = True)
# if lst_sorted == lst:
#     print("No")
# else:
#     print("Yes")

# Line segment intersection
# a1 = float(input())
# b1 = float(input())
# a2 = float(input())
# b2 = float(input())
# if a1 > b1:
#     a1, b1 = b1, a1
# if a2 > b2:
#     a2, b2 = b2, a2
# if a2 > a1 and a2 < b1 and b2 > b1:
#     print(b1- a2)
# if a2 > a1 and a2 > b1:
#     print("0")
# if a2 > a1 and a2 < b1 and b2 > a1 and b2 < b1:
#     print(b2 - a2)

# Number of Divisors
# x = int(input())
# n = 0
# for a in range(1,x+1):
#     if x % a == 0:
#         n += 1
# print(n)

#Quadratic Equation

# from cmath import sqrt
# #bx = -c
# a = float(input())
# b = float(input())
# c = float(input())
# D = b * b - 4 * a * c
# armat = sqrt(D).real
# if a == 0 and b == 0 and c == 0:
#     print("Non-quadratic equation")
#     print("Infinite solutions")
# if a == 0 and b == 0 and c != 0:
#     print("Non-quadratic equation")
#     print("No solution")
# if a == 0 and b != 0:
#     x = -c / b
#     print("Non-quadratic equation")
#     print("One solution:", x)
# if a != 0:
#     print("Quadratic equation")
#     print("Discriminant:", D)
#     if int(armat) != 0:
#         if (armat // int(armat)) == 1.0:
#             x1 = -b + armat / (2 * a)
#             x2 = -b - armat / (2 * a)
#             print("Two solutions:", x1, x2)
#         else:
#             print("No solution")
#     else:
#         print("No solution")

# list1
# lst = ["a", "b", "c", "d"]
# print(lst[0] + lst[1] + lst[2] + lst[3]

#list2
# x = int(input())
# lst = []
# for _ in range(x):
#     lst.append(int(input()))
# lst = set(lst)
# lst.remove(min(lst))
# print(min(lst))

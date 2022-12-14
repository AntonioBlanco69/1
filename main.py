# a = int(input("Enter number:"))
# print("Choose operation (+,-,*,/)")
# b = input("Enter char:")
# c = int(input("Enter number:"))
# if b == "+":
#     r = a + c
#     print(a, b, c, "=", r)
# elif b == "-":
#     r = a - c
#     print(a, b, c, "=", r)
# elif b == "*":
#     r = a * c
#     print(a, b, c, "=", r)
# elif b == "/" and c != 0:
#     r = a / c
# elif c == 0:
#     print("you cant divide to 0")
#
# Task 1
# print("Choose the between 1 and 100")
# q = int(input("Number:"))
# if 1 < q < 100:
#     if q % 3 == 0:
#         print("Fizz")
#     elif q % 5 == 0:
#         print("Buzz")
#     elif q % 3 == 0 and q % 5 == 0:
#         print("Fizz Buzz")
# else:
#     print(q)
#     print("Choose the between 1 and 100")
#
# # Task 2
#
# m1 = int(input("Sales for 1st manager:"))
# if m1 < 500:
#     s1 = m1*0.03
# if 500 <= m1 < 1000:
#     s1 = m1*0.05
# if m1 <= 1000:
#     s1 = m1*0.08
# m2 = int(input("Sales for 2nd manager:"))
# if m2 < 500:
#     s2 = m2*0.03
# if 500 <= m2 < 1000:
#     s2 = m2*0.05
# if m2 <= 1000:
#     s2 = m2*0.08
# m3 = int(input("Sales for 3rd manager:"))
# if m3 < 500:
#     s3 = m3*0.03
# if 500 <= m1 < 1000:
#     s3 = m3*0.05
# if m3 <= 1000:
#     s3 = m3*0.08
#
# salary = 200
# premium = 200
#
#
# if m1 == m2 == m3:
#     print("Every manager get salary:", salary + m1 + premium, "$")
# else:
#     if m1 > m2 and m1 > m3:
#         print("1st manager gets salary:", salary + s1 + premium, "$")
#         print("2nd manager gets salary:", salary + s2, "$")
#         print("3rd manager gets salary:", salary + s3, "$")
#     if m2 > m1 and m2 > m3:
#         print("1st manager gets salary:", salary + s1, "$")
#         print("2nd manager gets salary:", salary + s2 + premium, "$")
#         print("3rd manager gets salary:", salary + s3, "$")
#     if m3 > m1 and m3 > m2:
#         print("1st manager gets salary:", salary + s1, "$")
#         print("2nd manager gets salary:", salary + s2, "$")
#         print("3rd manager gets salary:", salary + s3 + premium, "$")
#
# o = input("Which network operator do you use:")
# if o == "99":
#     x = 55
# if 0 == "51":
#     x = 50
# if 0 == "NAR" or "nar" or "Nar" or "N" or "n" or "077" or "77":
#     x == 77
#
# z = input("Which network operator do you call:")
# if z == "99":
#     y = 55
# if z == "Aze":
#     x = 50
# if z == "NAR" or "nar" or "Nar" or "N" or "n" or "077" or "77":
#     x == 77
#
#
# m = int(input("How much did you talk in seconds:"))
# if x == 55 and y == 55:
#     p = 0.03
# if x == 55 and y == 50:
#     p = 0.07
# if x == 55 and y == 77:
#     p = 0.05
#
# if x == 55 and y == 55:
#     p = 0.07
# if x == 50 and y == 50:
#     p = 0.03
# if x == 50 and y == 77:
#     p = 0.06
#
# if x == 77 and y == 55:
#     p = 0.05
# if x == 77 and y == 50:
#     p = 0.06
# if x == 77 and y == 77:
#     p = 0.03
#
# print("The price of call:", p * m, "AZN")


# try:
#     a = int(input())
#     b = int(input())
#
#     print(a / b)
#
# except ValueError:
#     print("error")
# except ZeroDivisionError:
#     print("error")
# except NameError:
#     print("error")
# Task 1
# try:
#     a = int(input("Enter number:"))
#     print("Choose operation (+,-,*,/,%,**,//)")
#     b = input("Enter char:")

#     c = int(input("Enter number:"))
#     if b == "+":
#         res = a + c
#     elif b == "-":
#         res = a - c
#     elif b == "*":
#         res = a * c
#     elif b == "/":
#         if c == 0:
#             res = "infinity"
#         else:
#             res = a / c
#     elif b == "**":
#         res = a ** c
#     elif b == "%":
#         res = a % c
#     elif b == "//":
#         res = a // c
#     elif b != "//" or "%" or "**" or "*" or "/" or "-" or "+":
#         print("error")
#     print(a, b, c, "=", res)


# except ValueError:
#     print("Error")
# except ZeroDivisionError:
#     print("Error")
# except NameError:
#     print("Error")

# # Task 2
# try:
#     num = int(input("Enter 6-digit number:"))
#     numm1 = num // 1000     # first three numbers
#     numm2 = num % 1000      # second three numbers
#     if 100000 <= num <= 999999:
#         num6 = numm1 // 100        # 1st digit
#         num5 = numm1 % 100 // 10   # 2nd digit
#         num4 = numm1 % 10          # 3rd digit
#         num3 = numm2 // 100        # 4th digit
#         num2 = numm2 % 100 // 10   # 5th digit
#         num1 = numm2 % 10          # 6th digit
#         if num6 + num5 + num4 == num3 + num2 + num1:
#             print(num6, "+", num5, "+", num4, "=", num3, "+", num2, "+", num1)
#             print("Your number is lucky")
#         else:
#             print(num6, "+", num5, "+", num4, "!=", num3, "+", num2, "+", num1)
#             print("Your number is not lucky")
#     else:
#         print("You printed the wrong number")

# except ValueError:
#     print("Error")
# except ZeroDivisionError:
#     print("Error")
# except NameError:
#     print("Error")

# # Task 3
# try:
#     month = int(input("Choose the number of month:"))
#     if 1 <= month <= 12:
#         if month == 1 or 2 or 12:
#             print("It is winter")
#         elif 3 <= month <= 5:
#             print("It is spring")
#         elif 6 <= month <= 8:
#             print("It is summer")
#         else:
#             print("It is autumn")
#     else:
#         print("Error: your choice is not correct")
# except ValueError:
#     print("Error")
# except ZeroDivisionError:
#     print("Error")
# except NameError:
#     print("Error")


#
# # Task 1
# try:
#     a = int(input("Enter number:"))
#     print("Choose operation (+,-,*,/,%,**,//)")
#     b = input("Enter char:")
#
#     c = int(input("Enter number:"))
#     if b == "+":
#         res = a + c
#     elif b == "-":
#         res = a - c
#     elif b == "*":
#         res = a * c
#     elif b == "/":
#         if c == 0:
#             res = "infinity"
#         else:
#             res = a / c
#     elif b == "**":
#         res = a ** c
#     elif b == "%":
#         res = a % c
#     elif b == "//":
#         res = a // c
#     elif b != "//" or "%" or "**" or "*" or "/" or "-" or "+":
#         print("error")
#     print(a, b, c, "=", res)
#
#
# except ValueError:
#     print("Error")
# except ZeroDivisionError:
#     print("Error")
# except NameError:
#     print("Error")
#
# # Task 2
# try:
#     num = int(input("Enter 6-digit number:"))
#     numm1 = num // 1000     # first three numbers
#     numm2 = num % 1000      # second three numbers
#     if 100000 <= num <= 999999:
#         num6 = numm1 // 100        # 1st digit
#         num5 = numm1 % 100 // 10   # 2nd digit
#         num4 = numm1 % 10          # 3rd digit
#         num3 = numm2 // 100        # 4th digit
#         num2 = numm2 % 100 // 10   # 5th digit
#         num1 = numm2 % 10          # 6th digit
#         if num6 + num5 + num4 == num3 + num2 + num1:
#             print(num6, "+", num5, "+", num4, "=", num3, "+", num2, "+", num1)
#             print("Your number is lucky")
#         else:
#             print(num6, "+", num5, "+", num4, "!=", num3, "+", num2, "+", num1)
#             print("Your number is not lucky")
#     else:
#         print("You printed the wrong number")
#
# except ValueError:
#     print("Error")
# except ZeroDivisionError:
#     print("Error")
# except NameError:
#     print("Error")
#
# # Task 3
# try:
#     month = int(input("Choose the number of month:"))
#     if 1 <= month <= 12:
#         if month == 1 or 2 or 12:
#             print("It is winter")
#         elif 3 <= month <= 5:
#             print("It is spring")
#         elif 6 <= month <= 8:
#             print("It is summer")
#         else:
#             print("It is autumn")
#     else:
#         print("Error: your choice is not correct")
# except ValueError:
#     print("Error")
# except ZeroDivisionError:
#     print("Error")
# except NameError:
#     print("Error")
# while True:
#
#     a = int(input())
#     op = input()
#     b = int(input())
#
#     result = None
#
#     if op == "+":
#         result = a + b
#
#
# count = 1
# x = 0
# while count < 10001:
#     if count % 100 == 0:
#         print(count)
# #    x = x + count
#     count += 1
#
# print(x)

# p = int(input("Enter the number: "))
# l = int(input("Enter the number: "))
# while p <= l:
#     if p % 2 == 1:
#         print(p)
#         p += 2
#
#     else:
#         p += 1
#         print(p)
#         p += 2
#
# t = int(input("Enter the number: "))
# s = int(input("Enter the number: "))
# while t <= s:
#     if t % 2 == 0:
#         print(t)
#         t += 2
#     else:
#         t += 1
#         print(t)
#         t += 2
#
# a = int(input("Enter the number: "))
# b = int(input("Enter the number: "))
# w = q = x = a
# n = c = y = b
# count = 0
# while w <= n:
#     while count == 0 and a <= b:
#         print(a)
#         a += 1
#     print()
#     print(n)
#     n -= 1
#
#
#
# print()
# print("Numbers that divides to 7:")
# while x <= y:
#     if y % 7 == 0:
#         print(y)
#     y -= 1
#
# print("Count of numbers that divides to 5:")
# count1 = 0
# while q <= c:
#     if c % 5 == 0:
#         count1 += 1
#     c -= 1
#
# print(count1)

# base_id = 0
# max_id = 12000
# target_id = int(input())
#
# user_found = False
#
# while base_id <= max_id:
#     if base_id == target_id:
#         print("User found with id", base_id)
#         user_found = True
#         break
#     # else:
#     #     print("User not found")
#     base_id += 1
#
# if user_found:
#     print("User found")
# else:
#     print("User not found")

# x = False
# if not x:
#     print("OK")

# import random
#
# base_id = 0
# max_id = 12
#
# while base_id < max_id:
#     random_age = random.randint(6, 100)
#     print("User age:", random_age)
#     base_id += 1
#     if random_age < 18:
#         print("Not allowed")
#         continue

# Task 1
# sum = 0
#
# while True:
#     try:
#         num1 = int(input("Enter the number:"))
#         sum += num1
#         if num1 == 0:
#             print("Sum = ", sum)
#             break
#     except ValueError:
#         print("Error")
#     except ZeroDivisionError:
#         print("Error")
#     except NameError:
#         print("Error")
# print()
# Task 2
# while True:
#     try:
#         num2 = int(input("Enter the number:"))
#         if num2 >= 30 or num2 < 0:
#             print("Enter the number between 0-30")
#             print("if you want to exit print 0")
#             continue
#         if num2 == 0:
#             break
#         if num2 % 3 == 0:
#             print(num2, "is divisible to 3")
#     except ValueError:
#         print("Error")
#     except ZeroDivisionError:
#         print("Error")
#     except NameError:
#         print("Error")

# Task 3
import random
count = 0
border1 = int(input("Enter the MIN number:"))
border2 = int(input("Enter the MAX number:"))
num4 = random.randint(border1, border2)
level = int(input("Choose the level (1),(2),(3):"))
while True:
    try:
        num3 = int(input("Enter the number:"))
        count += 1
        if num3 == 0:
            break
        if level == 1:
            if num3 == num4:
                print("You found the number:", num3)
                print("It took you", count, "choices")
            if num3 < num4:
                print("Higher")
            if num3 > num4:
                print("Lower")
        if level == 2:
            if count <= 25:
                if num3 == num4:
                    print("You found the number:", num3)
                    print("It took you", count, "choices")
                if num3 < num4:
                    if num4 - num3 > 100000:
                        print("Higher to 100000")
                    elif num4 - num3 > 10000:
                        print("Higher to 10000")
                    elif num4 - num3 > 1000:
                        print("Higher to 1000")
                    elif num4 - num3 > 100:
                        print("Higher to 100")
                    elif num4 - num3 > 10:
                        print("Higher to 10")
                    elif num4 - num3 > 0:
                        print("Higher")
                if num3 > num4:
                    if num3 - num4 > 100000:
                        print("Lower to 100000")
                    elif num3 - num4 > 10000:
                        print("Lower to 10000")
                    elif num3 - num4 > 1000:
                        print("Lower to 1000")
                    elif num3 - num4 > 100:
                        print("Lower to 100")
                    elif num3 - num4 > 10:
                        print("Lower to 10")
                    elif num3 - num4 > 0:
                        print("Lower")
            else:
                print("You lost")
                break
        if level == 3:
            if count <= 10:
                if num3 == num4:
                    print("You found the number:", num3)
                    print("It took you", count, "choices")
                if num3 < num4:
                    if num4 - num3 > 100000:
                        print("Higher to 100000")
                    elif num4 - num3 > 10000:
                        print("Higher to 10000")
                    elif num4 - num3 > 1000:
                        print("Higher to 1000")
                    elif num4 - num3 > 100:
                        print("Higher to 100")
                    elif num4 - num3 > 10:
                        print("Higher to 10")
                    elif num4 - num3 > 0:
                        print("Higher")
                if num3 > num4:
                    if num3 - num4 > 100000:
                        print("Lower to 100000")
                    elif num3 - num4 > 10000:
                        print("Lower to 10000")
                    elif num3 - num4 > 1000:
                        print("Lower to 1000")
                    elif num3 - num4 > 100:
                        print("Lower to 100")
                    elif num3 - num4 > 10:
                        print("Lower to 10")
                    elif num3 - num4 > 0:
                        print("Lower")
            else:
                print("You lost")
                break

        if num3 >= border2 or num3 < border1:
            print("Enter the number between ", border1, "-", border2)
            print("if you want to exit print 0")
            continue
    except ValueError:
        print("Error")
    except ZeroDivisionError:
        print("Error")
    except NameError:
        print("Error")











































































# //////////////
# Zad 1
# def numbers(i: int) ->None:
#
#     if i<0:
#         return;
#     print(i);
#     numbers(i-1);
#
#
#
# numbers(100);


# Zad 2
#
# def fib(n: int)->int:
#     if(n==0):
#         return 0;
#     if(n==1):
#         return 1;
#     if(n>=2):
#         wynik = fib(n - 1) + fib(n - 2);
#         return wynik;
#
#
# print(fib(3));

# Zad 3
# def power(number: int, n: int) -> int:
#     i=0;
#     wynik=1;
#     if n==0:
#         return 1;
#     if(n==1):
#         return number
#     if (n>=2):
#         return power(number,n-1)*number;
#
#
#
#
#
# print(power(4,4));

# Zad 4
# def reverse(txt:str)->str:
#
#     if txt == "":
#         return txt
#     else:
#         return reverse(txt[1:]) + txt[0]
#

# string="koniak"
# print(string[len(string)::-1])


# print(reverse("koniak"))

# Zad 5
# def factorial(n: int) -> int:
#    if(n==0):
#        return 1
#    else:
#        return factorial(n-1) * n
#
# print(factorial(5))
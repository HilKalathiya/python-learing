# factorial
n = int(input("Enter The Number For Factorial:"))

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
facto = factorial(n)
print("factorial:",facto)

# fibonachis series
def fibonachi(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonachi(n-1)+fibonachi(n-2)
fibo = fibonachi(n)
print("Sum:",fibo)

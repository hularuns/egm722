def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        return 55#can put a print here to say invalid error, or return 'None'

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(6))
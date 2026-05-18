try:
    x = 10/2
    y = x.upper()
# except ZeroDivisionError:
#     print('Number should be greater than 0')
# except TypeError:
#     print('Type should be aimiler')
except Exception as e:
    print(e)
else:
    print(f'Operation compleated, result is {y}')
finally:
    print('Block ended')
print('code ended')
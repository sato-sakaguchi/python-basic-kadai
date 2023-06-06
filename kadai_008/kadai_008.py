import random
var = random.randint(1,101)
# var = int(var)
print(var)
#変数varの値を出力：確認用

if var % 3 == 0 and var % 5 ==0:
    print("FizzBuzz")

elif var % 5 == 0:
    print("Buzz")

elif var % 3 == 0:
    print("Fizz")

else:
    print(var)

# for var in range(1,101):
#     if var % 3 == 0 and var % 5 ==0:
#         print("FizzBuzz")

#     elif var % 5 == 0:
#         print("Buzz")

#     elif var % 3 == 0:
#         print("Fizz")

#     else:
#         print(var)
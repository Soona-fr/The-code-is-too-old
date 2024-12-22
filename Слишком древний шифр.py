import random

list_ = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

n = random.choice(list_)
print('Первая вставка: ', n)
def get_password(num):
    password = ''
    for i in range(1, num):
        for j in range(2, num):
            if j <= i:
                continue
            if num % (i + j) == 0:
                password += str(i) + str(j)
    return password


result = get_password(n)
print('Пароль:', result)


lst=[int(i) for i in input('Введите числа через пробел: ').split()]
print('список, который ввел пользователь: ',lst)
temp=0
for index in range(len(lst)):
    for i in range(len(lst)-1):
        if lst[i]>lst[i+1]:
            temp=lst[i]
            lst[i]=lst[i+1]
            lst[i+1]=temp
print('Список по возростанию', lst)
print('Список по убыванию: ', lst[::-1])

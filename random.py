#создание массива из случайных чисел
#сортировка массива

import random
#print (random.random())
a = [random.randint(0, 100) for i in range(1,11)]
print('mass {0}'.format(len(a)),a)

def q_sort(array):
    if len(array)<2:
        return array
    else:
        pivot   =   array[0]
        less    =   [i for i in array[1:] if i<=pivot]
        greater =   [i for i in array[1:] if i>pivot]
        return q_sort(less) + [pivot] + q_sort(greater)

a=q_sort(a)
print('mass {0}'.format(len(a)),a)


#https://github.com/legavaz/binsearch
import os

os.system('CLS')

start_vol   =   1
end_vol     =   101
print('Загадайте число от {0} до {1}'.format(start_vol,end_vol))
input('Для продолжения нажмите Enter:')

rez_false   =   False
count       =   0
while rez_false!=True:
    count   +=   1
    seredina =   (end_vol +   start_vol)//2
    print('{0} число : {1}'.format(count,seredina))
    side_vol        =     int(input('0 - угадали, 1-меньше, 3-больше: '))
    
    if side_vol    ==   0:
       rez_false    =   True
    elif side_vol   ==   1:
        end_vol     =   seredina
    elif side_vol   ==   3:
        start_vol   =   seredina   
         

print('*'*20)
print('Загаданное число: {0} отгадано с {1} попытки'.format(seredina,count))
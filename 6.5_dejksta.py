
from table import Table
import os
os.system('CLS')

tab = Table(3, 3)

# заполнение 1 колонки
tab.set_value(0, 0, 'вершина 1')
tab.set_value(1, 0, 'вершина 2')
tab.set_value(2, 0, 'вершина 3')

# заполнение 2 колонки
tab.set_value(0, 1, 'ab')
tab.set_value(1, 1, 'de')
tab.set_value(2, 1, 'mk')

# заполнение 3 колонки
tab.set_value(0, 2, 10)
tab.set_value(1, 2, 15)
tab.set_value(2, 2, 2)



tab.print_value()

# input('для продолжения Enter')
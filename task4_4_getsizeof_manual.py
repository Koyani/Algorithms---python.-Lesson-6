#task_4
#Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
#Количество элементов (n) вводится с клавиатуры.
import sys
def sum_of_seq(n):
    summa_2 = 1 * (1 - (-0.5) ** n) / (1 - (-0.5))
    print(f'Total memory: {sys.getsizeof(n) + sys.getsizeof(summa_2)}')
    print(summa_2)
    return summa_2

sum_of_seq(10)

'''
task_4_getsizeof_manual.py
0.666015625
104

task_4_getsizeof_cycle.py
0.666015625
Size of the supporting variable "size" is 24.
Variable name: size, variable value: 0, variable type: <class 'int'>, variable size: 24
28
Variable name: i, variable value: 9, variable type: <class 'int'>, variable size: 28
28
Variable name: element, variable value: 0.0009765625, variable type: <class 'float'>, variable size: 24
28
Variable name: summ, variable value: 0.666015625, variable type: <class 'float'>, variable size: 24
28
Variable name: n, variable value: 10, variable type: <class 'int'>, variable size: 28
28
Total size (without variable "size"):  104

task4_4_getsizeof_manual.py
Total memory: 52
0.666015625

task4_4_getsizeof_cycle.py
Size of the supporting variable "size" is 24.
Variable name: size, variable value: 0, variable type: <class 'int'>, variable size: 24.
Variable name: summa_2, variable value: 0.666015625, variable type: <class 'float'>, variable size: 24.
Variable name: n, variable value: 10, variable type: <class 'int'>, variable size: 28.
Total size (without variable "size"):  52
0.666015625
'''
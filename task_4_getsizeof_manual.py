#task_4
#Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
#Количество элементов (n) вводится с клавиатуры.
import sys
def sum_of_seq(n):
    summ = 0
    element = 1
    for i in range(n):
        summ += element
        element/= -2
    print(summ)
    print(sys.getsizeof(n) + sys.getsizeof(i) + sys.getsizeof(summ) + sys.getsizeof(element))
    return summ
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


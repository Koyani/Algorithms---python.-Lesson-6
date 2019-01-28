#task_3
#Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. 
#Например, если введено число 3486, то надо вывести число 6843.
import sys
def rever2(n):
    n1 = str(n)
    result = n1[::-1]
    print(f'Total memory: {sys.getsizeof(n) + sys.getsizeof(n1) + sys.getsizeof(result)}')
    print(result)
    return result

rever2(123456789)

'''
task_3.1_getsizeof_manual.py
Total memory: 52
987654321

task_3.1_getsizeof_cycle.py
Size of the supporting variable "size" is 24.
Variable name: size, variable value: 0, variable type: <class 'int'>, variable size: 24.
Variable name: palindrome, variable value: 987654321, variable type: <class 'int'>, variable size: 28.
Variable name: n, variable value: 0, variable type: <class 'int'>, variable size: 24.
Total size (without variable "size"):  52
987654321

task_3.2_getsizeof_manual.py
Total memory: 136
987654321

task_3.2_getsizeof_cycle.py
Size of the supporting variable "size" is 24.
Variable name: size, variable value: 0, variable type: <class 'int'>, variable size: 24.
Variable name: i, variable value: 9, variable type: <class 'str'>, variable size: 50.
Variable name: result, variable value: 987654321, variable type: <class 'str'>, variable size: 58.
Variable name: n, variable value: 123456789, variable type: <class 'int'>, variable size: 28.
Total size (without variable "size"):  136
987654321

task_3.3_getsizeof_manual.py
Total memory: 144
987654321

task_3.3_getsizeof_cycle.py
Size of the supporting variable "size" is 24.
Variable name: size, variable value: 0, variable type: <class 'int'>, variable size: 24.
Variable name: result, variable value: 987654321, variable type: <class 'str'>, variable size: 58.
Variable name: n1, variable value: 123456789, variable type: <class 'str'>, variable size: 58.
Variable name: n, variable value: 123456789, variable type: <class 'int'>, variable size: 28.
Total size (without variable "size"):  144
987654321

'''
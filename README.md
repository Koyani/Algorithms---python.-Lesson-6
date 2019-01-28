Для вычисления общего объема памяти, занятой всеми переменными, было выбрано два подхода. В первом случае (файлы task_х_getsizeof_manual.py) в ручном режиме отыскивались все переменные и их размер суммировался ("школьный" способ); во втором случае использовался (task_х_getsizeof_cycle.py) цикл 
for obj in locals().values():
    print sys.getsizeof(obj) 
для подсчёта суммы из памяти, занятой каждой переменной. В обоих алгоритмах результаты подсчёта памяти, занятой всеми переменными, совпал. В случае задачи 4 в разных её исполнениях, task_4 и task_4_4, общий объём памяти всех переменных различался в 2 раза, 104 для task_4 и 52 для task_4_4, т.к. использовалось  в 2 раза меньше переменных в task_4_4. Таким образом, с точки зрения занимаемой переменными памяти алгоритм task_4_4 является более предпочтительным, чем task_4.

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

Задание 3 было выполнено в трёх алгоритмах: task_3.1, task_3.2, task_3.3. При этом занятая всеми переменными память убывает в ряду task_3.1 < task_3.2 < task_3.3.
 
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


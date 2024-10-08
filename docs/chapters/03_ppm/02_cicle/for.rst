Цикл for
~~~~~~~~~

Очень часто одно и то же действие надо выполнить для набора однотипных данных. Например, преобразовать все строки в списке в верхний регистр. Для выполнения таких действий в Python используется цикл for.

Цикл for перебирает по одному элементы указанной последовательности и выполняет действия, которые указаны в блоке for, для каждого элемента.

Примеры последовательностей элементов, по которым может проходиться цикл for:

- строка
- список
- словарь
- Функция range
- любой итерируемый объект

Для понимания может помочь проект pythontutor . Там имеется визуализация кода, позволяющая увидеть, что происходит на каждом этапе выполнения кода. На сайте pythontutor можно загружать свой код.
Цикл for может работать с любой последовательностью элементов. Например, выше использовался список и цикл перебирал элементы списка. Аналогичным образом for работает с кортежами.

Напечатать элементы списка

Без цикла:

.. code:: python

	fruits = ["apple", "banana", "cherry"]
	print(fruits[0])
	print(fruits[1])
	print(fruits[2])

	apple
	banana
	cherry
	
Можно копировать и вставлять, но если строк будет 1000, 10000, 1000000 ...

С использованием цикла:

.. code:: python

	fruits = ["apple", "banana", "cherry"]
	for x in fruits:
	  print(x)

	apple
	banana
	cherry

Можно прочитать это следующим образом: "Для каждого элемента x списка fruits применить операцию print(x)".

Сначала x принимает значение apple, потом banana и так далее.

Напечатать каждый символ строки отдельно

.. code:: python

	for x in "banana":
	  print(x)

	b
	a
	n
	a
	n
	a

.. code:: python

	for x in "banana":
	  # вывод каждого символа строки с разделителем +
	  print(x, end = '+')

	b+a+n+a+n+a+

Преобразовать первый символ каждой строки в верхний регистр. Преобразованный список сохранить отдельно

.. code:: python

	# исходный список
	words = ['иванов','петров','сидоров']
	# новый список
	new_words = []
	​
	# Для (for) каждого элемента (el) списка words 
	for el in words:
		# Выполнить операции:
		# Преобразовать первую букву в верхний регистр 
		new_words.append(el.capitalize())
	​
	print(words)
	print(new_words)
	​
	​
	['иванов', 'петров', 'сидоров']
	['Иванов', 'Петров', 'Сидоров']

Вывести список каждого отдела организации

.. code:: python

	# Словарь с фамилиями сотрудников отделов
	dict_staff = {'Отдел сбыта': ['Ильина', 
								  'Куликов',
								  'Сергиенко',
								  'Корепин', 
								  'Климов', 
								  'Попкова'],
				 'Вице-президенты':['Гладких'],
				 'Начальники отделов':['Новиков'],
				 'Координаторы':['Ожогина']}
	# Проход по словарю (по ключам)
	for key in dict_staff:
		# Печать ключа словаря (отдел)
		print(key)
		# Разделитель
		print('-' * 10)
		# Печать значения по ключу (список отдела)
		print(dict_staff[key])
		# Пустая строка
		print()


	

Метод items позволяет проходиться в цикле сразу по паре ключ-значение:

.. code:: python

	# Словарь с фамилиями сотрудников отделов
	dict_staff = {'Отдел сбыта': ['Ильина', 
								  'Куликов',
								  'Сергиенко',
								  'Корепин', 
								  'Климов', 
								  'Попкова'],
				 'Вице-президенты':['Гладких'],
				 'Начальники отделов':['Новиков'],
				 'Координаторы':['Ожогина']}
	# Проход по словарю (по ключам)
	for key,value in dict_staff.items():
		# Печать ключа словаря (отдел)
		print(key)
		# Разделитель
		print('-' * 10)
		# Печать значения по ключу (список отдела)
		print(value)
		# Пустая строка
		print()

	Отдел сбыта
	----------
	['Ильина', 'Куликов', 'Сергиенко', 'Корепин', 'Климов', 'Попкова']

	Вице-президенты
	----------
	['Гладких']

	Начальники отделов
	----------
	['Новиков']

	Координаторы
	----------
	['Ожогина']

Функция range
```````````````

Возвращает числовой диапазон

Синтаксис:

range(start,end,step)

start - начальное значение диапазона

end - конечное значение диапазона. В диапазон не включается

step - шаг изменнения (по-умолчанию 1)

Формируется диапазон от значения start до значения end-1.

Используется, когда необходимо цикл for применить к числовому промежутку.

.. code:: python

	range(9)

	range(0, 9)


	# За начальное значение диапазона берется 0
	for i in range(3):
		print(i)
	​
	0
	1
	2
	for i in range(23, 26):
		print(i)

	23
	24
	25
	# Печать диапазона с шагом 2
	for i in range(1, 10, 2):
		print(i, end=' ')

	1 3 5 7 9 

**Примеры использования range**

При использовании оператора in в цикле мы можем работать только с тем экземпляром итерируемого объекта, на который он указывает. А если необходимо использовать индексы, то нужно брать range.

Напечатать индексы четных элементов

.. code:: pythonv

	# Исходный список
	df = [1, 4, 5, 7, 9, 8, 2, 4]
	# Пустой список для четных индексов
	even_indexes = []
	for index in range(len(df)):
		# У четного числа остаток от деления на 0 равен 0 (% остаток от деления)
		if index % 2 == 0:
			even_indexes.append(index)
	print(f'Исходный список: {df}')
	print(f'Индексы четных элементов: {even_indexes}')

	# Исходный список
	df = [1, 4, 5, 7, 9, 8, 2, 4]
	# Пустой список для четных индексов
	even_indexes = []
	for index in range(len(df)):
		# У четного числа остаток от деления на 0 равен 0 (% остаток от деления)
		if index % 2 == 0:
			even_indexes.append(index)

	print(f'Исходный список: {df}')
	print(f'Индексы четных элементов: {even_indexes}')
	​
	Исходный список: [1, 4, 5, 7, 9, 8, 2, 4]
	Индексы четных элементов: [0, 2, 4, 6]

Из заданной строки сформировать новую, где каждый символ есть максимальный символ среди соседей символа в исходной строке.

Вход: ромашка Выход: ррошшшк

.. code:: python

	input_string = input('Введите строку: ')
	# Длина строки
	count_chars = len(input_string)
	output_string = ''
	# Цикл для диапазона индексов от 0 до длина строки-1
	for index in range(0,count_chars):
		# Если индекс от 1 до предпоследнего
		if index > 0 and index < count_chars-1:
			# Вычислить максимальный среди окружающих
			s = max(input_string[index],input_string[index-1],input_string[index+1])
			output_string += s
		# Если индекс равен 0, то сравниваем с соседом справа
		elif index == 0:
			s = max(input_string[index],input_string[index+1])
			output_string += s
		else:
			# Иначе сравниваем с соседом слева
			s = max(input_string[index],input_string[index-1])
			output_string += s
		print(output_string)
	
	Введите строку: ромашка
	ррошшшк
	
Вложенные циклы
```````````````````

Вложенный цикл - это цикл внутри цикла.

"Внутренний цикл" будет выполняться один раз для каждой итерации "внешнего цикла".:

.. code:: python

	adj = ["красный", "большой", "вкусный"]
	fruits = ["яблоко", "банан", "вишня"]
	​
	for a in adj:
		for f in fruits:
			print(a,' ', f)
	​
	красный   яблоко
	красный   банан
	красный   вишня
	большой   яблоко
	большой   банан
	большой   вишня
	вкусный   яблоко
	вкусный   банан
	вкусный   вишня
	
Напечатать таблицу умножения для чисел от 2 до 5

.. code:: python

	for x in range (2,6):
		for y in range(2,6): 
			print(f'{x} * {y} = {x*y}')   # относится к циклу по y
		print('-'*10)                     # относится к циклу по x
		
		
	2 * 1 = 2
	2 * 2 = 4
	2 * 3 = 6
	2 * 4 = 8
	2 * 5 = 10
	2 * 6 = 12
	2 * 7 = 14
	2 * 8 = 16
	2 * 9 = 18
	----------
	3 * 1 = 3
	3 * 2 = 6
	3 * 3 = 9
	3 * 4 = 12
	3 * 5 = 15
	3 * 6 = 18
	3 * 7 = 21
	3 * 8 = 24
	3 * 9 = 27
	----------
	4 * 1 = 4
	4 * 2 = 8
	4 * 3 = 12
	4 * 4 = 16
	4 * 5 = 20
	4 * 6 = 24
	4 * 7 = 28
	4 * 8 = 32
	4 * 9 = 36
	----------
	5 * 1 = 5
	5 * 2 = 10
	5 * 3 = 15
	5 * 4 = 20
	5 * 5 = 25
	5 * 6 = 30
	5 * 7 = 35
	5 * 8 = 40
	5 * 9 = 45
	----------
​

Прерывание цикла: break
````````````````````````

Используется в случае принудительного выхода из цикла

.. code:: python

	fruits = ["apple", "banana", "cherry"]
	for x in fruits:
	  # Если элемент равен 'banana', то прервать цикл
	  if x == "banana":
		break
	  print(x)  
	
	print('Game over')
	
	
	fruits = ["apple", "banana", "cherry"]
	for x in fruits:
	  # Если элемент равен 'banana', то прервать цикл
	  if x == "banana":
		break
	  print(x)  
	print('Game over')
	
	apple
	Game over

Пропуск части цикла: continue
````````````````````````````````

Используется в случае необходимости принудительно начать следующий шаг цикла, пропустив часть строк в его теле. 
а перейти к обработке следующего элемента

.. code:: python

	fruits = ["apple", "banana", "cherry"]
	for x in fruits:
		# Если элемент равен 'banana', то не выполнять дальнейшие инструкции цикла, 
		# а перейти к обработке следующего элемента
		if x == "banana":
			continue
		print(x)
	
	apple
	cherry
	
	Из диапазона от 1 до 10 включительно вывести только те числа, которые не делятся ни на 2, ни на 3.

	Пояснение: В данном примере надо пропускать числа, которые делятся на 2 и 3

.. code:: python

	for i in range(1, 11):
		if i%2 == 0 or i%3 == 0:
			continue
		print(i)
	
	1
	5
	7

else в цикле
```````````````

else-код выполнится после того, как пройдут все витки цикла

.. code:: python

	fruits = ["apple", "cherry","orange"]
	for x in fruits:
		# Если элемент равен 'banana', то прервать цикл
		if x == "banana":
			break
		print(x)
	else:
		print('Успешное окончание цикла. Все итерации выполнены')
	print('Программа окончена')
	
	apple
	cherry
	orange
	Успешное окончание цикла. Все итерации выполнены
	Программа окончена

В данном примере break не выполнился, поэтому ветка else выполнилась. В случае срабатывания break, else не выполняется.

.. code:: python

	fruits = ["apple", "cherry", "banana", "orange"]
	for x in fruits:
		# Если элемент равен 'banana', то прервать цикл
		if x == "banana":
			break
		print(x)
	else:
		print('Успешное окончание цикла. Все итерации выполнены')
	print('Программа окончена')
	
	apple
	cherry
	Программа окончена

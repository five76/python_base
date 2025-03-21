Модули
~~~~~~

Модуль в языке Python – самой крупная организационной программной единицы, которая вмещает в себя программный код и данные, готовые для многократного использования. 
Модули в языке Python обычно соответствуют файлам программ (или расширениям, написанным на других языках программирования, таких как C, Java или C#). 
Каждый файл – это отдельный модуль, и модули могут импортировать другие модули для доступа к именам, которые в них определены.

Рассмотренные ранее программы имели линейную структуру, то есть инструкции программы выполнялись последовательно друг за другом в том порядке, в котором они записаны в файле. 
Данная структура подходит для простых программ. Если в процессе выполнения необходимо проверить ошибки, принять решение, выполнить части кода несколько раз и так  далее, то в 
этом случае необходмо прибегать к более сложным структурам **ветвлению** и **циклической организации действий (циклам)**.

В этом разделе рассматриваются возможности Python в управлении потоком выполнения программы:

- ветвление в ходе программы с помощью конструкции if/elif/else
- повторение действий в цикле с помощью конструкций for и while
- обработка ошибок с помощью конструкции try/except

.. toctree::
   :maxdepth: 4
   :caption: Оглавление

   01_modules/01_modules
   02_os_modules/index
   pep8_modules
   examples/modules_examples
   
   

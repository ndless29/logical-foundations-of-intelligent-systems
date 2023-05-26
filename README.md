# logical-foundations-of-intelligent-systems

Цель: Реализовать процедурную программу, решающую задачу обработки формул языка логики высказываний.
Задание: Проверить является ли формула ДНФ.

Формула - правильный текст на языке логики высказываний.
Подформула - подстрока формулы, являющаяся формулой. Формула считается подстрокой/подформулой самой себя. 
Атомарная формула - формула, которая не содержит логических связок; не содержит подформул отличных от себя.
Дизъюнктивная нормальная форма (ДНФ) - дизъюнкция простых конъюнкций.
Простая конъюнкция - конъюнкция одной или нескольких переменных, и каждая переменная входит не более одного раза.
Литерал – запись в исходном коде компьютерной программы, представляющая собой фиксированное значение. Литералами так же называют представление значения некоторого типа данных.

Грамматика языка логики высказываний.
<константа> ::=1|0
<символ> ::=A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z
<отрицание> ::=!
<конъюнкция> ::=/\
<дизъюнкция> ::=\/
<импликация> ::=->
<эквиваленция> ::=~
<открывающая скобка> ::=(
<закрывающая скобка> ::=)
<бинарная связка> ::=<конъюнкция>|<дизъюнкция>|<импликация>|<эквиваленция>
<атом> ::=<символ>
<унарная сложная формула>
::=<открывающая скобка><отрицание><формула><закрывающая скобка>
<бинарная сложная формула>
::=<открывающая скобка><формула><бинарная связка><формула><закрывающая скобка>
<формула>
::=<константа>|<атом>|<унарная сложная формула>|<бинарная сложная формула>



Алгоритм:
1.	Ввод формулы;
2.	Заменяются все, если такие есть, конъюнкции вида (L1/\L2), (BF/\L2), (L1/\BF), где L1 и L2 некоторые литералы или BF, на сокращение BF, означающее бинарную формулу;
3.	Проверка, изменилась ли формула после замены? Если да, то повторить 2 пункт. Если нет:
4.	Заменить, все, если такие есть, дизъюнкции вида (L1\/L2), (BF/\L2), (L1/\BF), где L1 и L2 некоторые литералы или BF, на сокращение BF, означающее бинарную формулу;
5.	Проверка, изменилась ли формула после замены? Если - да, то повторить 4 пункт. Если - нет:
6.	Проверка, входная формула после всех замен конъюнкций равна BF?
7.	Если - да, то выводится сообщение о том, что введенная формула не ДНФ;
8.	Если - нет, то производится проверка, входная формула после всех замен дизъюнкций равна BF?
9.	 Если - нет, то выводится сообщение о том, что введенная формула не ДНФ;
10.	 Если - да, то производится проверка, являются ли все конъюнкции в формуле простыми?
11.	 Если - нет, то выводится сообщение о том, что введенная формула не ДНФ;
12.	 Если - да, то выводится сообщение о том, что введенная формула ДНФ;
13.	Завершение работы.


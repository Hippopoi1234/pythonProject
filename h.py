"""
Вам дан массив в описанном формате, без пробелов и переводов строки. Ваша задача —отформатировать его следующим образом:

Каждая строка и каждая фигурная скобка должны находиться в отдельной строке.
Запятые находятся на той же строке, что и элемент (строка или фигурная скобка) перед ней.
После открывающейся фигурной скобки отступ увеличивается на 2 пробела.
Перед закрывающейся фигурной скобки отступ уменьшается на 2 пробела.
Изучите примеры, чтобы лучше понять, как должен выглядеть отформатированный массив.

Входные данные
Первая строка ввода содержит строку s, представляющую собой описание массива. Длина строки не превышает 1000 символов.

Выходные данные
Выведите отформатированный массив.

Примеры
входные данныеСкопировать
{odin,dva,tri}
выходные данныеСкопировать
{
  odin,
  dva,
  tri
}
входные данныеСкопировать
{}
выходные данныеСкопировать
{
}
входные данныеСкопировать
{stroka}
выходные данныеСкопировать
{
  stroka
}
входные данныеСкопировать
{a,b,{c,d},e,{}}
выходные данныеСкопировать
{
  a,
  b,
  {
    c,
    d
  },
  e,
  {
  }
}
"""
s = '{a,b,{{{e,k}},{c,d,e},{}}}'
spaces = 0
r = ''
eol = False
for c in s:
    if c == '{':
        r += '{\n'
        eol = True
        spaces += 2
        r += spaces * ' '
    elif c == '}':
        r += '\n'
        spaces -= 2
        r += spaces * ' '
        r += '}'
    elif c == ',':
        r += ',\n'
        r += spaces * ' '
    else:
        r += c
pr = r.split('\n')
for i in pr:
    if i.lstrip() == '':
        pr.remove(i)
print('\n'.join(pr))

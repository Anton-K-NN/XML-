'''
Вам дано описание пирамиды из кубиков в формате XML.
Кубики могут быть трех цветов: красный (red), зеленый (green) и синий (blue﻿).
Для каждого кубика известны его цвет, и известны кубики, расположенные прямо под ним.

Пример:

<cube color="blue">
  <cube color="red">
    <cube color="green">
    </cube>
  </cube>
  <cube color="red">
  </cube>
</cube>

Введем понятие ценности для кубиков. Самый верхний кубик, соответствующий корню XML документа имеет ценность 1. Кубики, расположенные прямо под ним, имеют ценность 2. Кубики, расположенные прямо под нижележащими кубиками, имеют ценность 3. И т. д.

Ценность цвета равна сумме ценностей всех кубиков этого цвета.

Выведите через пробел три числа: ценности красного, зеленого и синего цветов.
Sample Input:

<cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>
Sample Output:

4 3 1

<cube color="blue"><cube color="red"><cube color="green"></cube><cube color="blue"></cube></cube><cube color="red"></cube></cube>
'''

from xml.etree import ElementTree

red=0
green=0
blue=0

root=ElementTree.fromstring(input())
if root.attrib['color'] == 'red':
    red = red+1
if root.attrib['color'] == 'green':
    green += 1
if root.attrib['color'] == 'blue':
    blue += 1
k=1

def ch(r,x):
    global red
    global green
    global blue
    x+=1
    for child in r.findall("cube"):
        if child.attrib['color']=='red':
           red=red+x
        if child.attrib['color']=='green':
            green+=x
        if child.attrib['color']=='blue':
            blue+=x
        ch(child,x)

ch(root,k)
print(red,' ',green,' ',blue)

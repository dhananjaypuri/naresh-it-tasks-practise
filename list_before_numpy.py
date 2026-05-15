
#Q1

l = [10, 15,19,24,41,42,46,51,60];

print(l[3]);
print(l[4]);
print(l[6]);

#Q2
l = [10, 15,19,24,41,42,46,51,60];

print(l[1:6]);

#Q3

l = [10, 15,19,24,41,42,46,51,60];

even = [];

for i in l:
  if i % 2 == 0:
    even.append(i);

print(even);

#Q4

l = [10, 15,19,24,41,42,46,51,60];

l.append(90);

print(l);

#Q5

l = [10, 15,19,24,41,42,46,51,60];

l2 = [90,100];

l.extend(l2);

print(l);

#Q6

l = [10, 15,19,24,41,42,46,51,60];

print(l[1]);

l[1] = 25;

print(l);

#Q7

l = [10, 15,19,24,41,42,46,51,60];

for i in range(1,6):
  l[i] = 25;

print(l);

#Q8

l = [10, 15,19,24,41,42,46,51,60];

ind = [1,4,6];

for i in ind:
  l[i] = 25;

print(l);

#Q9

l = [10, 15,19,24,41,42,46,51,60];

l[1] = 25;
l[4] = 35;
l[6] = 45;

print(l);

#Q10

l = [10, 15,19,24,41,42,46,51,60];

print(l[4]);

l.pop(4);

print(l);

#Q11

l = [10, 15,19,24,41,42,46,51,60];

print(l);

for i in l[1:5]:
  l.remove(i);

print(l);

#Q12

l = [10, 15,19,24,41,42,46,51,60];

print(l);

ind = [1,4,6];

ind.sort(reverse=True);

for i in ind:
  l.pop(i);

print(l);

#Q13

num = 10;

l = [10, 15,19,24,41,42,46,51,60];

print(l);

new_l = [];

for i in l:
  new_l.append(i+num);

print(new_l);

#Q14

from math import sqrt

l = [10, 15,19,24,41,42,46,51,60];

new_l = [];

for i in l:
  new_l.append(sqrt(i));

print(new_l);

#Q15

from math import log

l = [10, 15,19,24,41,42,46,51,60];

new_l = [];

for i in l:
  new_l.append(log(i));

print(new_l);

#Q16

l1 = [1,2,3];

l2 = [4,5,6];

new_l = [];

if len(l1) == len(l2):
  i = 0;

  while i < len(l1):
    new_l.append(l1[i]+l2[i]);
    i += 1;
else:

  print("Both the list must have same lenght");

print(new_l);

#Q17

l = [10, 15,19,24,41,42,46,51,60];

new_l = [];

for i in l:
  if i == 10:
    new_l.append(True);
  else:
    new_l.append(False);

print(new_l);


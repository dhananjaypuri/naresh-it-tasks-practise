
import numpy as np

#Q1

l = [1,2,3,4,5];

arr = np.array(l)

arr

#Q2

arr = np.zeros(10);

arr

#Q3

arr = np.arange(10,51);

arr

#Q4

arr = np.array([10,20,30,40,50]);

print(arr[0]);
print(arr[-1])

#Q5

a1 = np.array([1,2,3]);
a2 = np.array([4,5,6]);

print(a1+a2);

#Q6

a1=np.array([1,2]);
a2=np.array([3,4]);

ml = a1*a2;

sum = ml.sum();

print(sum);

#Q7

a1 = np.array([10,20,30,40,50]);

print(a1[1:4]);

#Q8

a1 = np.array([10,20,30,40,50]);

print(a1[::-1]);

#Q9

a1 = np.array([10,20,30,40,50]);

a1[a1>25] = 0;

print(a1);

#Q10

a1 = np.array([1,2,3,4,5,6,7,8,9]);

a1[a1%2==1] = -1

print(a1);

#Q11

a1 = np.array([1,2,3,4,5,6,7,8,9]);

sqrt = np.sqrt(a1);

print(sqrt);

#Q12

a1 = np.array([3,5,1,2,4]);
print(a1.max());
print(a1.min());
print(a1.argmax());
print(a1.argmin());

#Q13

a1 = np.array([10,15,20,25,30]);

print(a1[a1>20]);

#Q14

a1 = np.array([10,15,20,25,30]);

print(a1[(a1>10)&(a1<25)]);

#Q15

a1 = np.array([4,6,8,10,12]);

i = 0;
ind = [];

for item in a1:
  if item>8:
    ind.append(i);
  i += 1;

print(ind);

#Q16

np.random.seed(1);

np.random.randint(1,10,10)

#Q17

a1 = np.array([1,2,3]);
a2 = np.array([4,5,6]);

print(a1.mean());
print(a1.std());

print(a2.mean());
print(a2.std());

#Q18

a1 = np.array([1,2,3,4,5]);
a2 = np.array([4,5,6,7,8]);

intersec = np.intersect1d(a1,a2);

print(intersec);

union = np.union1d(a1,a2);

print(union);

#Q19

a1 = np.array([10,20,30,40,50]);

print(a1.max());
print(a1.min());
print(a1.mean());

#Q19

a1 = np.array([10,20,30,40,50]);

print(a1.argmax());
print(a1.argmin());


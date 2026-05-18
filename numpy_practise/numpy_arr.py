import numpy as np

"""Numpy Array Creation"""

# From our own data

l = 1;

arr_zerod = np.array(l);
print(arr_zerod);
print(type(arr_zerod));
print(arr_zerod.ndim);

print("========================");
#### 1D Array

l = [1,2,34,5];

arr_oned = np.array(l);

print(arr_oned);
print(type(arr_oned));
print(arr_oned.ndim);

print("========================");

#### 2D Array

l = [[1,2], [3,4], (5,6)];

arr_twod = np.array(l);
print(arr_twod);
print(type(arr_twod));
print(arr_twod.ndim);


l = [[1,2], [3,4], list({5,6})]; # In order to use a set to convert into Array (convert set to list)

arr = np.array(l)

print(arr)
print(arr.ndim)

#### Convert from zeroes

arr_zeroes = np.zeros(5);

print(arr_zeroes);
print(id(arr_zeroes))

arr_zeroes= arr_zeroes + 5; ## Create new Array

print(arr_zeroes);
print(id(arr_zeroes))


arr_zeroes += 1; ## In place

print(arr_zeroes);
print(id(arr_zeroes))

## Create 2d array from zeroes

arr_zeroes2d = np.zeros((2,3), dtype=int);

arr_zeroes2d += 1;

print(arr_zeroes2d);

## Create using random (Start included and End excluded)

arr_rand_oned = np.random.randint(1,10); #1d

print(arr_rand_oned);

arr_rand_oned = np.random.randint(1,10, size=2); #1d

print(arr_rand_oned);

arr_rand_twod = np.random.randint(1,10, size=(2,3)); #2d

print(arr_rand_twod);

## Create using sequence

arr_arange = np.arange(10); #1d

print(arr_arange);

arr_arange = np.arange(2,3); #1d

print(arr_arange);


arr_arange = np.arange(1,10,2); #1d

print(arr_arange);

arr_arange = np.arange(11,1,-1); #1d

print(arr_arange);

print(len(arr_arange))

print(arr_arange.reshape(2,5)); ## Reshape into 2d array


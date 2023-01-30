def pigeonhole_sort(a):
    minimum = min(a)
    maximum = max(a)
    s = maximum - minimum + 1
    h = [0] * s #holes
    for x in a:
        assert type(x) is int, "integers only please"
        h[x - minimum] += 1
    i = 0
    for c in range(s):
        while h[c] > 0:
            h[c] -= 1
            a[i] = c + minimum
            i += 1
 
# driver code
array = [9, 7, 2, 3, 4, 8, 6]
print("The original array is: ", array)
print("The Sorted order is : ", end = ' ')
pigeonhole_sort(array)      
for i in range(0, len(array)):
    print(array[i], end = ' ')

import timeit

a = timeit.timeit('"-".join(str(n) for n in range(100))',number = 10000)
b = timeit.timeit('"-".join([str(n) for n in range(100)])',number=10000)
c = timeit.timeit('"-".join(map(str,range(100)))', number = 10000)

#Longest
print(a,'      the time of solution a')
print(b,'      the time of solution b')
#Shortest
print(c,'      the time of solution c')

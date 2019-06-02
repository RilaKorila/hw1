import numpy, sys, time
import matplotlib.pyplot as plt

n = 10
nList = []
exeTime = []

while n<200:

    if (len(sys.argv) != 2):
        #print("usage: python %s N" % sys.argv[0])
        #quit()

        #n = int(sys.argv[1])
        a = numpy.zeros((n, n)) # Matrix A
        b = numpy.zeros((n, n)) # Matrix B
        c = numpy.zeros((n, n)) # Matrix C

        # Initialize the matrices to some values.
        for i in range(n):
            for j in range(n):
                a[i, j] = i * n + j
                b[i, j] = j * n + i
                c[i, j] = 0

        begin = time.time()

        #C = A * B
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    c[i, j] += a[i, k] * b[k, j]

        end = time.time()

        exeTime.append(end - begin)
        print("time: %.6f sec" % (end - begin))

        # Print C for debugging. Comment out the print before measuring the execution time.
        total = 0
        for i in range(n):
            for j in range(n):
                # print c[i, j]
                total += c[i, j]

        # Print out the sum of all values in C.
        # This should be 450 for N=3, 3680 for N=4, and 18250 for N=5.
        print("sum: %.6f" % total)

        nList.append(n)
        n += 20
#----------------- while -----------------------------------

#show the graph
x = nList
y = exeTime

print(x)
print(y)

plt.plot(x, y)
plt.title("the relationship between N and the execute time")
plt.show()

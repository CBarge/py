import numpy
import scipy

a = numpy.matrix('1 2 3 4 5; 1 2 3 4 5; 1 2 3 4 5; 1 2 3 4 5; 1 2 3 4 5')

print(numpy.linalg.matrix_power(a,3))

a = numpy.matrix('2 4 5; 2 6 1; -2 9 15; 12 0 15; 3 34 -52')

b = numpy.matrix('2 4 5 4; 2 6 1 4; -2 9 15 4')

print(numpy.transpose(numpy.matmul(a, b)))

m = numpy.matrix('2 4 5; 2 6 1; -2 9 15; 12 0 15; 3 34 -52')

print(numpy.linalg.matrix_rank(m))

m = numpy.matrix('1 0 1 3; 2 3 4 7; -1 -3 -3 -4')
import numpy

inp_arr = numpy.array(raw_input().split(), float)
out_arr = numpy.zeros(len(inp_arr))

for i in range(len(inp_arr)):
    out_arr[i] = inp_arr[-(i+1)]

print out_arr

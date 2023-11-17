def hash(message):
    def cnot(x,y):
        return str((int(x)) ^ int(y))
    
    result = list(message)
    result[0] = cnot(result[4], result[0])
    result[2] = cnot(result[0], result[2])
    result[3] = cnot(result[1], result[3])
    result[1] = cnot(result[5], result[1])
    return ''.join(result[0:4])

for x in range(0,64):
    input = "{0:b}".format(x).zfill(6)
    if(hash(input)=='1111'):
        print(input, ':' ,hash(input), 'x')
    else:
        print(input, ':' ,hash(input))
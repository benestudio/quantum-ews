import random

def hash(message):
    def cnot(x,y):
        return str(int(bool(int(x))) ^ bool(int(y)))
    
    result = list(message)
    result[0] = cnot(result[4], result[0])
    result[2] = cnot(result[0], result[2])
    result[3] = cnot(result[1], result[3])
    result[1] = cnot(result[5], result[1])
    return ''.join(result[0:4])

counter=0
found=False

while not found:    
  counter=counter+1
  input = input = "{0:b}".format(random.choice(range(0,63))).zfill(6)
  print(input)
  if(hash(input)=='1111'):
     found=True
  
print('Hash found at step', counter)
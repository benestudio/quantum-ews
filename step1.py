from braket.circuits import Circuit
from braket.devices import LocalSimulator

circ=Circuit()
device = LocalSimulator()

circ.i([0,1,2,3,4,5]).x([0,2,3])
print(circ)

task = device.run(circ, shots=1)
result = task.result()

print(result)
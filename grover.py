import numpy as np
from braket.circuits import Circuit
from braket.devices import LocalSimulator
from braket.aws import AwsDevice

device = LocalSimulator()
#device = AwsDevice('arn:aws:braket:us-east-1::device/qpu/ionq/Harmony')

circ=Circuit()

def ccnot():
  return Circuit().h(2).cnot(1,2).ti(2).cnot(0,2).t(2).cnot(1,2).ti(2).cnot(0,2).t([1,2]).cnot(0,1).h(2).t(0).ti(1).cnot(0,1)

def cz():
  return Circuit().h(1).cnot(0,1).h(1)

def amplification():
  return Circuit().h([0,1]).x([0,1]).add(cz()).x([0,1]).h([0,1])

def oracle(target):
  targetBits = list(target)
  circ = Circuit()
  if(targetBits[0]=='0'):
    circ.x(0)
  if(targetBits[1]=='0'):
    circ.x(1)
  circ.add(ccnot())
  if(targetBits[0]=='0'):
    circ.x(0)
  if(targetBits[1]=='0'):
    circ.x(1)
  return circ


circ.x(2).h([0,1,2])
circ.add(oracle('00'))
circ.add(amplification())

print(circ)

task = device.run(circ, shots=1)
measurement = task.result().measurements

print(measurement)
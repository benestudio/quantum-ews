# quantum-ews

Bene:Studio Quantum Computing workshop examples

## Requirements

- Python > 3.7
- pip

## Install and run

- ```pip install -r requirements.txt```
- ```python step1.py```

## Branches

- step_1: playing with Braket's Circuit and LocalSimulator
- step_2: hash searching with Grover's algorithm

## Configure and Run on AWS Braket device (optional)

- create your AWS account
- create your user at IAM console. Copy your user credentials
- ```pip install awscli```
- ```aws configure```
- give your user credentials. Set up your defaul region where Braket is available (e.g. us-east-1)
- find your preferred device arn (e.g. arn:aws:braket:us-east-1::device/qpu/ionq/Harmony)
- Change LocalSimulator() to AwsDevice(arn) in your code
- When running first time, follow the command line instructions to enable Braket. 
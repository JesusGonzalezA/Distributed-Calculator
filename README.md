# Distributed-Calculator
UGR project. Distributed calculator using apache thrift technologies

## Description
Calculator using thrift tech. It is implemented in Java and Python.
The calculator is a distributed calculator using RPC middleware. The architecture consists in a client-server architecture.
You can use two types of calculators:
- Simple: to make simple operations (+,-,*,/)
- Complex: to make those simple operations using vectors and matrixes.

## Documentation
[See here](https://github.com/JesusGonzalezA/Distributed-Calculator/tree/master/doc)

## Execution
### Java
```shell
cd exe
java -jar server.jar
java -jar client.jar
```

### Python
You can use my virtual environment (venv directory) if you don't want to install python3 and thrift library.

```shell
python3 server.py
python3 client.py
```

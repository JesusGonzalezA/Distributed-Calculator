import glob
import sys

from calculator import CalculatorComplex
from calculator import ttypes

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

import logging

logging.basicConfig(level=logging.DEBUG)


class CalculadoraHandler:
    def __init__(self):
        self.log = {}

    def add(self, operands):
        if ( len(operands.complexOperand1) != len(operands.complexOperand2) ):
            raise ttypes.InvalidOperation("Los tamaños deben de ser iguales")
        result = []
        for i in range(0, len(operands.complexOperand1)):
            result.append(operands.complexOperand1[i] + operands.complexOperand2[i])
        return result

    def multiply(self, operands):
        if ( len(operands.complexOperand1) != len(operands.complexOperand2) ):
            raise ttypes.InvalidOperation("Los tamaños deben de ser iguales")
        return operands.complexOperand1

    def subtract(self, operands):
        if ( len(operands.complexOperand1) != len(operands.complexOperand2) ):
            raise ttypes.InvalidOperation("Los tamaños deben de ser iguales")
        result = []
        for i in range(0, len(operands.complexOperand1)):
            result.append(operands.complexOperand1[i] - operands.complexOperand2[i])
        return result


if __name__ == "__main__":
    handler = CalculadoraHandler()
    processor = CalculatorComplex.Processor(handler)
    transport = TSocket.TServerSocket(host="127.0.0.1", port=9090)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

    print("iniciando servidor complejo...")
    server.serve()
    print("fin")

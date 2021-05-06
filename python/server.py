import glob
import sys

from calculator import Calculator
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
        return operands.operand1 + operands.operand2

    def multiply(self, operands):
        return operands.operand1 * operands.operand2

    def divide(self, operands):
        if (operands.operand2 == float(0)):
            raise ttypes.InvalidOperation("No se puede dividir por 0")

        return operands.operand1 / operands.operand2

    def subtract(self, operands):
        return operands.operand1 - operands.operand2


if __name__ == "__main__":
    handler = CalculadoraHandler()
    processor = Calculator.Processor(handler)
    transport = TSocket.TServerSocket(host="127.0.0.1", port=9090)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

    print("iniciando servidor...")
    try:
        server.serve()
    except:
        transport.close()
    print("fin")

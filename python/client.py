from calculator import Calculator
from thrift import Thrift
from thrift . transport import TSocket
from thrift . transport import TTransport
from thrift . protocol import TBinaryProtocol
from calculator import ttypes

#-------------------------------------------------------------------------------------

def trydivide(client, operands):
    try:
        return client.divide(operands)
    except:
        print("Hubo un error")

def operate(operator, client, operands):
    switcher =  {
        '+': lambda : client.add(operands),
        'x': lambda : client.multiply(operands),
        '*': lambda : client.multiply(operands),
        '-': lambda : client.subtract(operands),
        '/': lambda : trydivide(client, operands),
        ':': lambda : client.divide(operands)
    }
    return switcher.get(operator, lambda : print("Error al pasar los argumentos"))()

#-------------------------------------------------------------------------------------
# Variables
operands = ttypes.Operands()
operator = ""

# Endpoint variables
port = 9090
server = "localhost"
#-------------------------------------------------------------------------------------
# Initialize transport
transport = TSocket . TSocket (server, port)
transport = TTransport . TBufferedTransport ( transport )
protocol = TBinaryProtocol . TBinaryProtocol ( transport )

# Create the client
client = Calculator . Client ( protocol )
#-------------------------------------------------------------------------------------
# Read the operation
print("¡Bienvenido a la calculadora distribuida de Jesús!")
print("Atención: se usará como separador de decimales el punto ('.') ")

# Set the operands
print("Operando 1: ", end='')
operands.operand1 = float(input())

print("Operador (+ - / * : x): ", end='')
operator = input()

print("Operando 2: ", end='')
operands.operand2 = float(input())
#------------------------------------------------------------------------------------

# Operate
transport.open()
resultado = operate(operator, client, operands)
transport.close()

# Print the result
print( str(operands.operand1) + " " + str(operator) + " " + str(operands.operand2) + " = " + str(resultado) )

from calculator import CalculatorComplex
from thrift import Thrift
from thrift . transport import TSocket
from thrift . transport import TTransport
from thrift . protocol import TBinaryProtocol
from calculator import ttypes

#-------------------------------------------------------------------------------------

def tryadd(client, operands):
    try:
        return client.add(operands)
    except:
        print("Hubo un error")

def trymultiply(client, operands):
    try:
        return client.multiply(operands)
    except:
        print("Hubo un error")

def trysubtract(client, operands):
    try:
        return client.subtract(operands)
    except:
        print("Hubo un error")


def operate(operator, client, operands):
    switcher =  {
        '+': lambda : tryadd(client, operands),
        'x': lambda : trymultiply(client, operands),
        '*': lambda : trymultiply(client, operands),
        '-': lambda : trysubtract(client, operands)
    }
    return switcher.get(operator, lambda : print("Error al pasar los argumentos"))()

#-------------------------------------------------------------------------------------
# Variables
operands = ttypes.ComplexOperands()
operands.complexOperand1 = []
operands.complexOperand2 = []

# Endpoint variables
port = 9090
server = "localhost"
#-------------------------------------------------------------------------------------
# Initialize transport
transport = TSocket . TSocket (server, port)
transport = TTransport . TBufferedTransport ( transport )
protocol = TBinaryProtocol . TBinaryProtocol ( transport )

# Create the client
client = CalculatorComplex . Client ( protocol )
#-------------------------------------------------------------------------------------
# Read the operation
print("¡Bienvenido a la calculadora distribuida de Jesús!")
print("Atención: se usará como separador de decimales el punto ('.') ")

# Set the operands
print("Leyendo los vectores:")
print("Primer vector:")
n = int(input("Introduzca el tamaño del vector: "))
for i in range(0, n):
    print("Elemento ", i, ": ", end='')
    operands.complexOperand1.append( float(input()) )

print("Segundo vector:")
n = int(input("Introduzca el tamaño del vector: "))
for i in range(0, n):
    print("Elemento ", i, ": ", end='')
    operands.complexOperand2.append(float(input()))

# Read the operation
print("Introduzca la operación que desea realizar (+ - * x) : ", end='')
operator = input()
#------------------------------------------------------------------------------------

# Operate
transport.open()
resultado = operate(operator, client, operands)
transport.close()

# Print the result
print("Resultado: ", resultado)

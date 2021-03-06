#
# Autogenerated by Thrift Compiler (0.14.1)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
from thrift.TRecursive import fix_spec

import sys

from thrift.transport import TTransport
all_structs = []


class Operands(object):
    """
    Interfaz de calculadora.
    Permite realizar las siguientes operaciones:
         - Suma
         - Resta
         - División
         - Multiplicación

    Attributes:
     - operand1
     - operand2

    """


    def __init__(self, operand1=None, operand2=None,):
        self.operand1 = operand1
        self.operand2 = operand2

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.DOUBLE:
                    self.operand1 = iprot.readDouble()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.DOUBLE:
                    self.operand2 = iprot.readDouble()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('Operands')
        if self.operand1 is not None:
            oprot.writeFieldBegin('operand1', TType.DOUBLE, 1)
            oprot.writeDouble(self.operand1)
            oprot.writeFieldEnd()
        if self.operand2 is not None:
            oprot.writeFieldBegin('operand2', TType.DOUBLE, 2)
            oprot.writeDouble(self.operand2)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.operand1 is None:
            raise TProtocolException(message='Required field operand1 is unset!')
        if self.operand2 is None:
            raise TProtocolException(message='Required field operand2 is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class ComplexOperands(object):
    """
    Attributes:
     - complexOperand1
     - complexOperand2

    """


    def __init__(self, complexOperand1=None, complexOperand2=None,):
        self.complexOperand1 = complexOperand1
        self.complexOperand2 = complexOperand2

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.LIST:
                    self.complexOperand1 = []
                    (_etype3, _size0) = iprot.readListBegin()
                    for _i4 in range(_size0):
                        _elem5 = iprot.readDouble()
                        self.complexOperand1.append(_elem5)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.complexOperand2 = []
                    (_etype9, _size6) = iprot.readListBegin()
                    for _i10 in range(_size6):
                        _elem11 = iprot.readDouble()
                        self.complexOperand2.append(_elem11)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('ComplexOperands')
        if self.complexOperand1 is not None:
            oprot.writeFieldBegin('complexOperand1', TType.LIST, 1)
            oprot.writeListBegin(TType.DOUBLE, len(self.complexOperand1))
            for iter12 in self.complexOperand1:
                oprot.writeDouble(iter12)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.complexOperand2 is not None:
            oprot.writeFieldBegin('complexOperand2', TType.LIST, 2)
            oprot.writeListBegin(TType.DOUBLE, len(self.complexOperand2))
            for iter13 in self.complexOperand2:
                oprot.writeDouble(iter13)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.complexOperand1 is None:
            raise TProtocolException(message='Required field complexOperand1 is unset!')
        if self.complexOperand2 is None:
            raise TProtocolException(message='Required field complexOperand2 is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class InvalidOperation(TException):
    """
    Attributes:
     - error_message

    """


    def __init__(self, error_message=None,):
        super(InvalidOperation, self).__setattr__('error_message', error_message)

    def __setattr__(self, *args):
        raise TypeError("can't modify immutable instance")

    def __delattr__(self, *args):
        raise TypeError("can't modify immutable instance")

    def __hash__(self):
        return hash(self.__class__) ^ hash((self.error_message, ))

    @classmethod
    def read(cls, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and cls.thrift_spec is not None:
            return iprot._fast_decode(None, iprot, [cls, cls.thrift_spec])
        iprot.readStructBegin()
        error_message = None
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    error_message = iprot.readString().decode('utf-8', errors='replace') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()
        return cls(
            error_message=error_message,
        )

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('InvalidOperation')
        if self.error_message is not None:
            oprot.writeFieldBegin('error_message', TType.STRING, 1)
            oprot.writeString(self.error_message.encode('utf-8') if sys.version_info[0] == 2 else self.error_message)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __str__(self):
        return repr(self)

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(Operands)
Operands.thrift_spec = (
    None,  # 0
    (1, TType.DOUBLE, 'operand1', None, None, ),  # 1
    (2, TType.DOUBLE, 'operand2', None, None, ),  # 2
)
all_structs.append(ComplexOperands)
ComplexOperands.thrift_spec = (
    None,  # 0
    (1, TType.LIST, 'complexOperand1', (TType.DOUBLE, None, False), None, ),  # 1
    (2, TType.LIST, 'complexOperand2', (TType.DOUBLE, None, False), None, ),  # 2
)
all_structs.append(InvalidOperation)
InvalidOperation.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'error_message', 'UTF8', None, ),  # 1
)
fix_spec(all_structs)
del all_structs

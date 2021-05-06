import org.apache.thrift.TException;
import org.apache.thrift.server.TServer;
import org.apache.thrift.server.TSimpleServer;
import org.apache.thrift.transport.TServerSocket;
import org.apache.thrift.transport.TServerTransport;

import java.util.ArrayList;
import java.util.List;

public class ComplexCalculatorHandler implements CalculatorComplex.Iface {

    public ComplexCalculatorHandler () {

    }

    @Override
    public List<Double> add(ComplexOperands operands) throws InvalidOperation {
        if (operands.getComplexOperand1Size() != operands.getComplexOperand2Size()){
            throw new InvalidOperation("Los vectores deben de tener el mismo tamaño");
        }
        int tam = operands.getComplexOperand1Size();
        ArrayList<Double> result = new ArrayList<Double>();

        for (int i=0; i<tam; ++i)
            result.add(operands.complexOperand1.get(i) + operands.complexOperand2.get(i));

        return result;
    }

    @Override
    public List<Double> subtract(ComplexOperands operands) throws InvalidOperation {
        if (operands.getComplexOperand1Size() != operands.getComplexOperand2Size()){
            throw new InvalidOperation("Los vectores deben de tener el mismo tamaño");
        }
        int tam = operands.getComplexOperand1Size();
        ArrayList<Double> result = new ArrayList<Double>();

        for (int i=0; i<tam; ++i)
            result.add(operands.complexOperand1.get(i) - operands.complexOperand2.get(i));

        return result;
    }

    @Override
    public List<Double> multiply(ComplexOperands operands) throws InvalidOperation {
        if (operands.getComplexOperand1Size() != operands.getComplexOperand2Size()){
            throw new InvalidOperation("Los vectores deben de tener el mismo tamaño");
        }
        int tam = operands.getComplexOperand1Size();
        ArrayList<Double> result = new ArrayList<Double>();

        for (int i=0; i<tam; ++i)
            result.add(operands.complexOperand1.get(i) * operands.complexOperand2.get(i));

        return result;
    }
}
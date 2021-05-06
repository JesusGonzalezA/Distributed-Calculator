import org.apache.thrift.TException;
import org.apache.thrift.server.TServer;
import org.apache.thrift.server.TSimpleServer;
import org.apache.thrift.transport.TServerSocket;
import org.apache.thrift.transport.TServerTransport;

public class CalculatorHandler implements Calculator.Iface {

    public CalculatorHandler () {

    }

    @Override
    public double add(Operands operands) {
        return operands.getOperand1() + operands.getOperand2();
    }

    @Override
    public double subtract(Operands operands) {
        return operands.getOperand1() - operands.getOperand2();
    }

    @Override
    public double divide(Operands operands) throws InvalidOperation {

        if (operands.getOperand2() == new Double(0)){
            throw new InvalidOperation("El denominador no puede ser 0");
        }
        return operands.getOperand1() / operands.getOperand2();
    }

    @Override
    public double multiply(Operands operands) {
        return operands.getOperand1() * operands.getOperand2();
    }
}
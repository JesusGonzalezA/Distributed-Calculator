import org.apache.thrift.TException;
import org.apache.thrift.transport.TSSLTransportFactory;
import org.apache.thrift.transport.TTransport;
import org.apache.thrift.transport.TSocket;
import org.apache.thrift.transport.TSSLTransportFactory.TSSLTransportParameters;
import org.apache.thrift.protocol.TBinaryProtocol;
import org.apache.thrift.protocol.TProtocol;

import java.util.Scanner;

public class Client {
    public static void main(String [] args) {

        try {
            // Set the client up
            TTransport transport = new TSocket("localhost", 9090);
            transport.open();

            TProtocol protocol = new  TBinaryProtocol(transport);
            Calculator.Client client = new Calculator.Client(protocol);

            // Operate
            perform(client);

            // Close connection
            transport.close();

        } catch (TException x) {
            x.printStackTrace();
        }
    }

    private static void perform(Calculator.Client client) throws TException
    {
        // Variables
        Scanner scanInput = new Scanner(System.in);
        String operator;
        Operands operands = new Operands();
        double result = 0;
        boolean error = false;

        // Read operation
        System.out.println("\u001B[35m" + "¡Bienvenido a la calculadora distribuida de Jesús!");
        System.out.println("\u001B[33m" + "Se utiliza la coma (',') como separador de decimales." + "\u001B[0m");
        System.out.print("Operando 1: ");
        operands.setOperand1( scanInput.nextDouble() );

        System.out.print("Operador (+ - / : x *): ");
        operator = scanInput.next();

        System.out.print("Operando 2: ");
        operands.setOperand2( scanInput.nextDouble() );

        // Operate
        switch (operator){
            case "+":
                result = client.add(operands);
                break;
            case "-":
                result = client.subtract(operands);
                break;
            case ":":
            case "/":
                try{
                    result = client.divide(operands);
                }catch(InvalidOperation err){
                    System.out.println("Hubo un error");
                }
                break;
            case "*":
            case "x":
                result = client.multiply(operands);
                break;
            default:
                error = true;
                break;
        }

        // Print result
        if (error){
            System.out.println("\u001B[31m" + "Ha habido un error pasando los argumentos");
        }
        else {
            System.out.println("\u001B[32m" + operands.getOperand1() + " " + operator + " " + operands.getOperand2()
                    + " = " + result );
        }

    }
}

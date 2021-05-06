import org.apache.thrift.TException;
import org.apache.thrift.transport.TSSLTransportFactory;
import org.apache.thrift.transport.TTransport;
import org.apache.thrift.transport.TSocket;
import org.apache.thrift.transport.TSSLTransportFactory.TSSLTransportParameters;
import org.apache.thrift.protocol.TBinaryProtocol;
import org.apache.thrift.protocol.TProtocol;

import java.util.ArrayList;
import java.util.Scanner;

public class ComplexClient {
    public static void main(String [] args) {

        try {
            // Set the client up
            TTransport transport = new TSocket("localhost", 9090);
            transport.open();

            TProtocol protocol = new  TBinaryProtocol(transport);
            CalculatorComplex.Client client = new CalculatorComplex.Client(protocol);

            // Operate
            perform(client);

            // Close connection
            transport.close();

        } catch (TException x) {
            x.printStackTrace();
        }
    }

    private static void perform(CalculatorComplex.Client client) throws TException
    {
        // Variables
        Scanner scanInput = new Scanner(System.in);
        String operator;
        ComplexOperands operands = new ComplexOperands();
        ArrayList<Double> result = new ArrayList<>();
        boolean error = false;
        int tam = 0;

        // Read operation
        System.out.println("\u001B[35m" + "¡Bienvenido a la calculadora distribuida de Jesús!");
        System.out.println("\u001B[33m" + "Se utiliza la coma (',') como separador de decimales." + "\u001B[0m");

        System.out.print("Introduzca el tamano del primer vector: ");
        tam = scanInput.nextInt();
        operands.complexOperand1 = new ArrayList<Double>(tam);

        for (int i=0; i<tam; ++i) {
            System.out.print("Elemento " + i + ": ");
            operands.getComplexOperand1().add( scanInput.nextDouble() );
        }

        System.out.print("Operador (+ - / : x *): ");
        operator = scanInput.next();

        System.out.print("Introduzca el tamano del segundo vector: ");
        tam = scanInput.nextInt();
        operands.complexOperand2 = new ArrayList<Double>(tam);

        for (int i=0; i<tam; ++i) {
            System.out.print("Elemento " + i + ": ");
            operands.complexOperand2.add( scanInput.nextDouble() );
        }

        // Operate
        switch (operator){
            case "+":
                try{
                    result = new ArrayList<Double>(client.add(operands));
                }catch(InvalidOperation err){
                    System.out.println("Hubo un error");
                }
                break;
            case "-":
                try{
                    result = new ArrayList<Double>(client.subtract(operands));
                }catch(InvalidOperation err){
                    System.out.println("Hubo un error");
                }
                break;
            case "*":
            case "x":
                try{
                    result = new ArrayList<Double>(client.multiply(operands));
                }catch(InvalidOperation err){
                    System.out.println("Hubo un error");
                }
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
            System.out.println("\u001B[32m" + result.toString() );
        }

    }
}

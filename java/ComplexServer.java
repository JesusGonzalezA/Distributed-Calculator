
import org.apache.thrift.server.TServer;
import org.apache.thrift.server.TServer.Args;
import org.apache.thrift.server.TSimpleServer;
import org.apache.thrift.transport.TServerSocket;
import org.apache.thrift.transport.TServerTransport;

public class ComplexServer {
    public static ComplexCalculatorHandler handler;
    public static CalculatorComplex.Processor processor;

    public static void main(String [] args) {
        try {
            handler = new ComplexCalculatorHandler();
            processor = new CalculatorComplex.Processor(handler);

            Runnable simple = new Runnable() {
                public void run() {
                    simple(processor);
                }
            };

            new Thread(simple).start();
        } catch (Exception x) {
            x.printStackTrace();
        }
    }

    public static void simple(CalculatorComplex.Processor processor) {
        try {
            TServerTransport serverTransport = new TServerSocket(9090);
            TServer server = new TSimpleServer(new Args(serverTransport).processor(processor));

            System.out.println("Starting the complex server...");
            server.serve();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

}

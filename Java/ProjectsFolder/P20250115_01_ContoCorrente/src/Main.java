import java.io.*;

public class Main {
	public static void main(String[] args) throws InterruptedException, IOException {
	String filePath = "db.txt";
	
	Contocorrente conto = new Contocorrente(filePath);
	
	ClientSync c1 = new ClientSync("Mario", 20, conto);
	ClientNonSync c3 = new ClientNonSync("Marco", 40, conto);
	
	c1.start();
	c3.start();
	c1.join();
	c3.join();
	
		}
	}
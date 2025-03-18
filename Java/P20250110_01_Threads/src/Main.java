
public class Main {

	public static void main(String[] args) {

		Thread t5 = new Thread(new Thread5('A'));
		t5.start();
		Thread t5a = new Thread(new Thread5('B'));
		t5a.start();
	}

}


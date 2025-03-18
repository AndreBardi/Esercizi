
public class Thread3 implements Runnable {

	@Override
	public void run() {
	    int counter = 0;

	    for (int i = 0; i < 5; i++) { 
	      counter++;
	      printMsg(counter); //recalls the print inside the function
	      
	    }
	}

	private void printMsg(int counter) {
		System.out.println("Your counter value is: " + counter);
		
	}
}

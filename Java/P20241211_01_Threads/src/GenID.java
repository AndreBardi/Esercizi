
public class GenID extends Thread{
	static long ID = 0;
	
	public void run() {
        while (true) {
            System.out.println(ID);
            try {
                Thread.sleep(500);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            ID = ID + 1;
        }
	}
}
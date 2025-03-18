
public class Thread4 implements Runnable {

    @Override
    public void run() {
        for (int i = 1; i <= 5; i++) {
            System.out.println("Your counter value prints: " + i);
            try {
                Thread.sleep(1000); // 1 second delay
            } catch (InterruptedException e) {
                System.out.println("Your counter value was interrupted.");
            }
        }
    }
}
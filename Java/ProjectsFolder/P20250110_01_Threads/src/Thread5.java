
public class Thread5 extends Thread{

	char ch;
    int i = 1, j = 100;

    public Thread5(char c) {
        ch = c;
    }
    public void run() {
        if (ch == 'A')
            while (true) {
                System.out.println(" A = " + i);
                i++;
                try {
                    Thread.sleep(500);
                } catch (InterruptedException e) {
                }
                if (i > 10)
                    break;
            }
        else
            while (true) {
                System.out.println(" B = " + j);
                j--;
                try {
                    Thread.sleep(500);
                } catch (InterruptedException e) {
                }
                if (j < 90)
                    break;
            }
    }
}

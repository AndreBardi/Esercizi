
public class Lettore extends Thread {
    private CasellaPosta casella;

    public Lettore(CasellaPosta casella) {
        this.casella = casella;
    }

    @Override
    public void run() {
        while (true) {
            casella.leggi();
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}

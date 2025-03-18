
public class Scrittore extends Thread {
    private CasellaPosta casella;

    public Scrittore(CasellaPosta casella) {
        this.casella = casella;
    }

    @Override
    public void run() {
        int contatore = 1;
        while (true) {
            casella.scrivi("Messaggio " + contatore);
            contatore++;
            try {
                Thread.sleep(500);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}

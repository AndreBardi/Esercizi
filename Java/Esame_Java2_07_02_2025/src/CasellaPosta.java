import java.util.LinkedList;
import java.util.Queue;

public class CasellaPosta {
    private final int CAPACITA_MAX = 10;
    private Queue<String> messaggi = new LinkedList<>();

    public synchronized void scrivi(String messaggio) {
        while (messaggi.size() == CAPACITA_MAX) {
            try {
                wait();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        messaggi.add(messaggio);
        System.out.println("Scrittore: " + messaggio);
        notify();
    }

    public synchronized String leggi() {
        while (messaggi.isEmpty()) {
            try {
                wait();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        String messaggio = messaggi.poll();
        System.out.println("Lettore: " + messaggio);
        notify();
        return messaggio;
    }
}

import java.util.*;

public class SetteMezzo {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Mazzo mazzo = new Mazzo();
        mazzo.mescola();

        double punteggioGiocatore = 0;
        boolean continua = true;

        System.out.println("Benvenuto a 7 e mezzo!");

        while (continua) {
            Carta carta = mazzo.pescaCarta();
            punteggioGiocatore += carta.getPunteggio();
            System.out.println("Hai pescato: " + carta);
            System.out.println("Punteggio attuale: " + punteggioGiocatore);

            if (punteggioGiocatore > 7.5) {
                System.out.println("Hai sballato! Hai perso.");
                return;
            }

            System.out.print("Vuoi pescare un'altra carta? (s/n): ");
            String risposta = scanner.nextLine();
            if (!risposta.equalsIgnoreCase("s")) {
                continua = false;
            }
        }

        double punteggioBanco = 0;
        while (punteggioBanco < 5.5) {
            Carta cartaBanco = mazzo.pescaCarta();
            punteggioBanco += cartaBanco.getPunteggio();
        }

        System.out.println("Il banco ha totalizzato: " + punteggioBanco);

        if (punteggioBanco > 7.5 || punteggioGiocatore > punteggioBanco) {
            System.out.println("Complimenti, hai vinto!");
        } else if (punteggioGiocatore == punteggioBanco) {
            System.out.println("Pareggio!");
        } else {
            System.out.println("Mi dispiace, il banco ha vinto.");
        }

        scanner.close();
    }
}

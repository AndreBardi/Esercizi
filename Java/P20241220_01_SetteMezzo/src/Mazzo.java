import java.util.*;

class Mazzo {
    private List<Carta> carte;

    public Mazzo() {
        carte = new ArrayList<>();
        String[] semi = {"Cuori", "Quadri", "Fiori", "Picche"};
        String[] valori = {"Asso", "2", "3", "4", "5", "6", "7", "Fante", "Cavallo", "Re"};
        double[] punteggi = {1, 2, 3, 4, 5, 6, 7, 0.5, 0.5, 0.5};

        for (String seme : semi) {
            for (int i = 0; i < valori.length; i++) {
                carte.add(new Carta(seme, valori[i], punteggi[i]));
            }
        }
    }

    public void mescola() {
        Collections.shuffle(carte);
    }

    public Carta pescaCarta() {
        return carte.remove(0);
    }
}
import java.util.List;

public class Televisore extends Prodotto {
    private int pollici; 
    private String qualita;

    public Televisore(int idProdotto, String nome, String descrizione, double prezzo, List<String> negozi, 
    				  int pollici, String qualita) {
        super(idProdotto, nome, descrizione, prezzo, negozi);
        this.pollici = pollici;
        this.qualita = qualita;
    }

    @Override
    public String toString() {
        return super.toString() + " - Pollici: " + pollici + "\", Qualità: " + qualita;
    }

    // Getters and Setters
    public int getPollici() {
        return pollici;
    }

    public String getQualita() {
        return qualita;
    }
}

import java.util.List;

public class Aspirapolvere extends Prodotto {
    private int potenza; 
    private String tipoAspirapolvere;
    public Aspirapolvere(int idProdotto, String nome, String descrizione, double prezzo, List<String> negozi, int potenza, String tipoAspirapolvere) {
        super(idProdotto, nome, descrizione, prezzo, negozi);
        this.potenza = potenza;
        this.tipoAspirapolvere = tipoAspirapolvere;
    }

    @Override
    public String toString() {
        return super.toString() + " - Potenza: " + potenza + "W, Tipo: " + tipoAspirapolvere + "\n";
    }

    public int getPotenza() {
        return potenza;
    }
    public String getTipoAspirapolvere() {
        return tipoAspirapolvere;
    }
}

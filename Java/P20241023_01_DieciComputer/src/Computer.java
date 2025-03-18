import java.util.Random;

public class Computer {
    // Attributi
    private double prezzo;
    private double peso;
    private double larghezza;
    private double altezza;
    private double profondita;
    private String produttore;
    private int annoProduzione;

    private static int numeroComputerCreati = 0;
    
    private static final String[] produttori = {"Dell", "HP", "Apple", "Lenovo", "Acer", "Asus", "Samsung"};
    

    // Costruttore
	public Computer(double prezzo, double peso, double larghezza, double altezza, double profondita, String produttore,
			int annoDiProduzione) {
		super();
		this.prezzo = prezzo;
		this.peso = peso;
		this.larghezza = larghezza;
		this.altezza = altezza;
		this.profondita = profondita;
		this.produttore = produttore;
		this.annoProduzione = annoDiProduzione;
		this.numeroComputerCreati ++;
	}


    // Getter e Setter
    public double getPrezzo() {
        return prezzo;
    }

    public void setPrezzo(double prezzo) {
        this.prezzo = prezzo;
    }

    public double getPeso() {
        return peso;
    }

    public void setPeso(double peso) {
        this.peso = peso;
    }

    public double getLarghezza() {
        return larghezza;
    }

    public void setLarghezza(double larghezza) {
        this.larghezza = larghezza;
    }

    public double getAltezza() {
        return altezza;
    }

    public void setAltezza(double altezza) {
        this.altezza = altezza;
    }

    public double getProfondita() {
        return profondita;
    }

    public void setProfondita(double profondita) {
        this.profondita = profondita;
    }

    public String getProduttore() {
        return produttore;
    }

    public void setProduttore(String produttore) {
        this.produttore = produttore;
    }

    public int getAnnoProduzione() {
        return annoProduzione;
    }

    public void setAnnoProduzione(int annoProduzione) {
        this.annoProduzione = annoProduzione;
    }

    // Metodo per stampare il numero di Computer creati
    public static int getNumeroComputerCreati() {
        return numeroComputerCreati;
    }

	public static Computer casuale() {
		Random random = new Random();
		double prezzo = 500 + (2000 - 500) * random.nextDouble();
		double peso = 0.7 +(5.0 - 0.7) * random.nextDouble();
		double larghezza = 30 +(50 - 30) * random.nextDouble();
		double altezza = 20 +(30 - 20) * random.nextDouble();
		double profondita = 1 +(5 - 1) * random.nextDouble();
		String produttore = produttori[random.nextInt(produttori.length)];
		int annoDiProduzione = 2015 + random.nextInt(10);
		return new Computer(prezzo, peso, larghezza, altezza, profondita, produttore, annoDiProduzione);
	}
    @Override
    public String toString() {
        return "Computer [prezzo=" + prezzo + ", peso=" + peso + ", larghezza=" + larghezza + 
               ", altezza=" + altezza + ", profondita=" + profondita + 
               ", produttore=" + produttore + ", annoProduzione=" + annoProduzione + "]";
    }
    
    public void stampaConCornice() {
        String[] informazioni = {
            "Produttore: " + produttore,
            "Prezzo: €" + String.format("%.2f", prezzo),
            "Peso: " + String.format("%.2f", peso) + " kg",
            "Dimensioni (L x A x P): " + String.format("%.2f", larghezza) + " cm x " +
            String.format("%.2f", altezza) + " cm x " + String.format("%.2f", profondita) + " cm",
            "Anno di produzione: " + annoProduzione
        };

        // Stampa della cornice superiore
        System.out.print("+");
        for (int i = 0; i < 55; i++) {
            System.out.print("-");
        }
        System.out.println("+");

        // Stampa delle informazioni allineate
        for (String info : informazioni) {
            System.out.print("| ");
            System.out.print(info);
            for (int i = info.length(); i < 53; i++) {
                System.out.print(" ");  // Aggiungi spazi per l'allineamento
            }
            System.out.println(" |");
        }

        // Stampa della cornice inferiore
        System.out.print("+");
        for (int i = 0; i < 55; i++) {
            System.out.print("-");
        }
        System.out.println("+");
    }


}

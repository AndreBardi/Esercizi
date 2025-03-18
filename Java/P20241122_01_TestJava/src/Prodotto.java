public abstract class Prodotto {

    private String name;
    private double price;
    private String categoria;

    public Prodotto(String name, double price, String categoria) {
        this.name = name;
        this.price = price;
        this.categoria = categoria;
    }

    public String getName() {
        return name;
    }

    public double getPrice() {
        return price;
    }

    public String getCategoria() {
        return categoria;
    }

    public abstract double calculateDiscount();

    public String displayOriginal() {
        double sconto = calculateDiscount();
        return String.format("Nome: %s, Prezzo originale: %.2f, Categoria: %s, Sconto: %.2f", 
                              name, price, categoria, sconto);
    }
    
    @Override
    public String toString() {
        double sconto = calculateDiscount();
        double prezzoFinale = price - sconto;
        return String.format("Nome: %s, Prezzo scontato: %.2f, Categoria: %s, Sconto: %.2f", 
                              name, prezzoFinale, categoria, sconto);
    }
}

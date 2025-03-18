import java.util.Arrays;

public class Test {
    public static void main(String[] args) {
        Prodotto aspirapolvere = new Aspirapolvere(1, "Dyson V11", "Aspirapolvere senza fili potente", 599.99, Arrays.asList("Mediaworld", "Euronics"), 550, "Portatile");
        Prodotto televisore = new Televisore(2, "Samsung QLED", "TV con qualità eccezionale", 799.99, Arrays.asList("Trony", ""), 55, "4K");

        Cliente cliente1 = new Cliente(1, "Marco", "Rossi", "marco.rossi@example.com", "password123");
        Cliente cliente2 = new Cliente(2, "Laura", "Bianchi", "laura.bianchi@example.com", "password456");

        cliente1.acquistaProdotto(aspirapolvere);
        cliente2.acquistaProdotto(televisore);
    }
}

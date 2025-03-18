import java.util.Comparator;
import java.util.LinkedList;

public class ProductManager implements Ordinabile {
    LinkedList<Prodotto> prodotti;

    public ProductManager() {
        prodotti = new LinkedList<>();
    }

    public void addProduct(Prodotto prodotto) {
        prodotti.add(prodotto);
    }

    public void displayProducts() {
        prodotti.forEach(System.out::println);
    }

    @Override
    public LinkedList<Prodotto> sortByPrice(LinkedList<Prodotto> prodotti) {
        prodotti.sort(Comparator.comparingDouble(Prodotto::getPrice));
        return prodotti;
    }
}

public class ProductApp {
    public static void main(String[] args) {
        ProductManager manager = new ProductManager();

        manager.addProduct(new Elettronica("Laptop", 800, "Tecnologia"));
        manager.addProduct(new Elettronica("Telefono", 300, "Tecnologia"));
        manager.addProduct(new Abbigliamento("Giacca", 120, "Abbigliamento invernale"));
        manager.addProduct(new Abbigliamento("T-Shirt", 20, "Abbigliamento estivo"));

        System.out.println("Prodotti prima dell'ordinamento:");
        for (Prodotto prodotto : manager.prodotti) {
            System.out.println(prodotto.displayOriginal());
        }

        manager.sortByPrice(manager.prodotti);

        System.out.println("\nProdotti dopo l'ordinamento:");
        manager.displayProducts();
    }
}

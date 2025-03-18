
class Abbigliamento extends Prodotto {
	
    public Abbigliamento(String name, double price, String categoria) {
        super(name, price, categoria);
    }

    @Override
    public double calculateDiscount() {
    	
		if (getCategoria().equalsIgnoreCase("Abbigliamento Invernale")) {
			return getPrice() * 0.15;
			
		} else {
			
			return getPrice()*0;
		}
    	
    }
    
}



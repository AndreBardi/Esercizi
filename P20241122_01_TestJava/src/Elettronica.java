
class Elettronica extends Prodotto {
	
    public Elettronica(String name, double price, String categoria) {
        super(name, price, categoria);
    }

    @Override
    public double calculateDiscount() {
    	
        if (getPrice() > 500) {
        	
            return getPrice() * 0.1;
        } else {
        	
            return getPrice()*0;
        }
    }

}
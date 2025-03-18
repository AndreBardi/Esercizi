
public class Main {

	public static void main(String[] args) {
		/*
         * Realizzare una classe Computer con i seguenti attributi
         * - Prezzo
         * - Peso
         * - Dimensioni (larghezza, altezza, profondità)
         * - Produttore
         * - Anno di produzione
         * 
         * Nel main creare degli oggetti di tipo Computer
         * e stampare il loro contenuto
         * 
         * NB: ricordate di utilizzare getter, setter e costruttore
         * generati da eclipse
         * 
         * Bonus: aggiungere un metodo alla classe Computer 
         * che stampi quanti oggetti (di tipo Computer) sono stati creati
         */
		
		Computer com1 = new Computer();
		com1.setAltezza(1.5);
		com1.setAnnoDiProduzione(2023);
		com1.setLarghezza(35.0);
		com1.setPeso(4.5);
		com1.setPrezzo(4500.0);
		com1.setProduttore("archer");
		com1.setProfondità(25.0);
		
		Computer com2 = new Computer(9875., 7.2, 60., 5., 40., "IBM", 1990);
		
		Computer com3 = new Computer(9875., 7.2, 60., 5., 40., "IBM", 1990);
		com3.setAltezza(1.5);
		com3.setAnnoDiProduzione(2023);
		com3.setLarghezza(35.0);
		com3.setPeso(4.5);
		com3.setPrezzo(4500.0);
		com3.setProduttore("archer");
		com3.setProfondità(25.0);
		
		
		System.out.println("Ciao");
		

	}

}

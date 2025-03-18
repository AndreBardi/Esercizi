public class Main {
   
	public static void main(String[] args) {

        // Creazione e stampa di 10 computer con valori casuali
        for (int i = 1; i <= 10; i++) {
            Computer computer = Computer.casuale();
            System.out.println("Computer #" + i);
            computer.stampaConCornice();
        }

        // Stampa del numero di computer creati
        System.out.println("Numero totale di computer creati: " + Computer.getNumeroComputerCreati());
   
	}

}

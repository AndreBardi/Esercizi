
public class Calcolatrice {

	public static void main(String[] args) {
		Calcolatrice c  =new Calcolatrice();
		System.out.println("La somma è " + c.somma(3, 2));
		System.out.println("La differenza è " + c.sottrazione(3, 2));
		System.out.println("La moltiplicazione è " + c.moltiplicazione(3, 2));
		System.out.println("La divisione è " + c.divisione(4, 2));

	}
	public int somma (int a, int b) {
		return a + b;
	}
	public int sottrazione (int a, int b) {
		return a - b;
	}
	public int moltiplicazione (int a, int b) {
		return a * b;
	}
	public int divisione (int a, int b) {
		return a / b;
	}
	

}


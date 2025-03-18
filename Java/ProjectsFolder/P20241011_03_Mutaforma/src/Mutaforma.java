
public class Mutaforma {

	public static void main(String[] args) {
		int a = Somma(10, 20);
		System.out.println(a);
		
		double b = Somma(10.1, 20.0);
		
		String s = Somma("buona","sera"); 
		
		System.out.println("Ciao");
		System.out.println(1);
		System.out.println(2.5);
	}

	private static String Somma(String string, String string2) {
		return string+string2;
	}
	
	private static double Somma(double d, double e) {
		return d+e;
	}	

	private static int Somma(int i, int j) {
		return i+j;
	}
	
}

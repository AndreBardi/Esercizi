
public class Pitagora {

	public static void main(String[] args) {
		// Definire misure cateti
		
		double cat1 = 45.3;
		double cat2 = 67.2;
		
		// 1) Calcolo ipotenusa con Teorema di Pitagora
		double ipotenusa = Math.sqrt((cat1 * cat1) + (cat2 * cat2));
		System.out.println("L'ipotenusa misura  " + ipotenusa + " metri");
		
		// 2) Calcolo area triangolo rettangolo
		double areaTriangolo = (cat1 + cat2) /2;
		System.out.println("L'area del triangolo misura " + areaTriangolo + " metri quadrati");
		
		// 3) Calcolo perimetro del triangolo rettangolo
		double perimetro = cat1 + cat2 + ipotenusa;
		System.out.println("Il perimetro del triangolo misura " + perimetro + " metri");
		
		// 4) Calcolo raggio del cerchio
		double raggio = (3.0 / 4.0) * ipotenusa;
		System.out.println("Il raggio misura " + raggio + " metri");
		
		// 5) Calcolo circonferenza del cerchio
		double circonferenza = 2 * Math.PI * raggio;
		System.out.println("La circonferenza misura " + circonferenza + " metri");
		
		// 6) Calcolo area del cerchio
		double areaCerchio = Math.PI * raggio * raggio;
		System.out.println("L'area del cerchio misura " + areaCerchio + " metri quadrati");
		
		
		TriangoloRettangolo tr = new TriangoloRettangolo(3,4);
		System.out.println("Ipotenusa: " + tr.getHyp());
		System.out.println("Area: " + tr.getArea());
		
		tr.setCat1(6);
		System.out.println("Ipotenusa: " + tr.getHyp());
		System.out.println("Area: " + tr.getArea());
		
	}

}

import java.util.*;
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		
		//I set
		HashSet<Prova> hsp = new HashSet<Prova>();
		TreeSet<Prova> tsp = new TreeSet<Prova>();
		
		HashMap<Prova, Integer> hsm = new HashMap<Prova, Integer>();
		TreeMap<Prova, Integer> tsm = new TreeMap<Prova, Integer>();
		
		for (int i=0; i<100; i++) {
			hsp.add(new Prova(i));
			
			System.out.println(hsp.contains(new Prova(10)));
			
		Prova unaProva = new Prova(987);
		hsp.add(unaProva);
		System.out.println(unaProva());
			
		}
	}

}

class Prova {
	public String uno;
	public Integer due;
	public Prova(int n) {
		uno = "UNO";
		due = n;
	}
	public String toString() {
		return ""+due;
	}
}
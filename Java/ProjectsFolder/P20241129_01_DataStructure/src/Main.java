import java.util.*;
import java.time.LocalTime;

public class Main {

	public static void main(String[] args) {
		// Set, Map, Queue, Stack, Array, List
		// var now = System.nanoTime();
		
		//calcolare il tempo che ci vuole
		//per inserire 1000000 di numeri interi
		//sequenziali in testa a una LinkedList
		final Integer N=1000000;
		long inizio, fine;
		
		//Test LinkedList
		
		inizio = System.nanoTime();
		AddToLinkedList(N);
		fine = System.nanoTime();
		System.out.println("LinkedList: Per inserire "+ 
		N + " elementi in coda: " + (fine-inizio)/1000000000.0 + " sec. ");
		
		
		inizio = System.nanoTime();
		AddFirstLinkedList(N);
		fine = System.nanoTime();
		System.out.println("LinkedList: Per inserire "+ 
		N + " elementi in coda: " + (fine-inizio)/1000000000.0 + " sec. ");
		
		
		inizio = System.nanoTime();
		AddToArrayList(N);
		fine = System.nanoTime();
		System.out.println("LinkedList: Per inserire "+ 
		N + " elementi in coda: " + (fine-inizio)/1000000000.0 + " sec. ");
		
		inizio = System.nanoTime();
		AddFirstArrayList(N);
		fine = System.nanoTime();
		System.out.println("LinkedList: Per inserire "+ 
		N + " elementi in coda: " + (fine-inizio)/1000000000.0 + " sec. ");
		
	}
	private static LinkedList<Integer> AddToLinkedList(Integer n) {
        LinkedList<Integer> lli = new LinkedList<Integer>();
        while (n > 0) {
            lli.add(n--);
        }
        return lli;
    }
    private static ArrayList<Integer> AddToArrayList(Integer n) {
        ArrayList<Integer> lli = new ArrayList<Integer>();
        while (n > 0) {
            lli.add(n--);
        }
        return lli;
    }
    private static LinkedList<Integer> AddFirstLinkedList(Integer n) {
        LinkedList<Integer> lli = new LinkedList<Integer>();
        while (n > 0) {
            lli.addFirst(n--);
        }
		return lli;
    }
    private static ArrayList<Integer> AddFirstArrayList(Integer n) {
        ArrayList<Integer> lli = new ArrayList<Integer>();
        while (n > 0) {
            lli.addFirst(n--);
        }
        return lli;
    }
    private static NostraLL<Integer> AddFirst(Integer n) {
    	NostraLL<Integer> l = new NostraLL<Integer>(); 
    	
    	
    }
}
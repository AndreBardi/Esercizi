import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		Scanner rd = new Scanner(System.in);
		while(true) {
			System.out.print("A che piano deve andare? [0,1,2,3]");
			int piano = rd.nextInt();
			Macchina(piano);
		}

	}
	
	static int[][] fsm = { { 0, 1, 2, 3 }, {-1, 0, 1, 2 }, {-2, -1, 0, 1 }, { -3, -2, -1, 0 } 
	static in stato = 0; //sono al piano terra
	
	///La macchina si deve muovere al piano indicato come parametro
	private static void Macchina(int piano) {
		
	}
	
	
		};
	}
	

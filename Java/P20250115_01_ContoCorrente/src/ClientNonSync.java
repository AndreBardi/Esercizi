
public class ClientNonSync extends Thread {
	private final String nome;
	private final double somma;
	private final Contocorrente conto;
	
	public ClientNonSync(String nome, double somma, Contocorrente conto) {
	super();
	this.nome = nome;
	this.somma = somma;
	this.conto = conto;
	}
	
	@Override
	public void run() {
	try {
	System.out.println(nome + " - Saldo iniziale: " + conto.getSaldo());
	conto.prelievoNonSynch(somma);
	System.out.println(nome + " - Prelievo effettuato. Saldo attuale: " + conto.getSaldo());
	} catch (Exception e) {
	System.out.println(nome + " - Errore: " + e.getMessage());
			}
		}
	
	}
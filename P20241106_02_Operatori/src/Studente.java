
public class Studente extends Persona{
	private String corso;
	private int annoDiFondazione;
	public Studente(String nome, int eta, String corso, int annoDiFondazione) {
		super(nome, eta);
		this.corso = corso;
		this.annoDiFondazione = annoDiFondazione;
	}
	
	
}

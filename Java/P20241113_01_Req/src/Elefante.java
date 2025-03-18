
public class Elefante extends Mammifero implements Must, Req, Comparable<Elefamte> {
	
	private Double peso;

	public Double getPeso() {
		return peso;
	}


	public void setPeso(Double peso) {
		this.peso = peso;
	}

	public Elefante(Integer freqResp, Integer freqCardio, Double peso) {
		super(freqResp, freqCardio);
		this.peso = peso;
	}
	
	@Override
	public String toString() {
		return "Elefante [peso=" + peso + ", Verso()=" + Verso() + "]";
	}


	public Elefante() {
		super();
		// TODO Auto-generated constructor stub
	}
	
	
	
	

}

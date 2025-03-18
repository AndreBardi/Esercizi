import java.util.List;

public class Prodotto {
	
	private Integer id;
	private String nome;
	private String descrizione;
	private Double prezzo;
	private List<String> negozio;
	
	
	public Prodotto(Integer id, String nome, String descrizione, Double prezzo, List<String> negozio) {
		super();
		this.id = id;
		this.nome = nome;
		this.descrizione = descrizione;
		this.prezzo = prezzo;
		this.negozio = negozio;
		}
	

	@Override
	public String toString() {
		return "\nProdotto [ID: " + id + ", \nNome: " + nome + ", \nDescrizione: " + descrizione + 
				", \nPrezzo: " + prezzo + "€" 
				+ ", \nNegozio: " + negozio + "]\n";
	}

	public Integer getId() {
		return id;
	}
	public String getNome() {
		return nome;
	}
	public String getDescrizione() {
		return descrizione;
	}
	public Double getPrezzo() {
		return prezzo;
	}
	public List<String> getNegozio() {
		return negozio;
	}
	

}

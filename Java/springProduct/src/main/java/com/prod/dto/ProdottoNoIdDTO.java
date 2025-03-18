package com.prod.dto;

public class ProdottoNoIdDTO {
	private String marca, modello, descrizione;
	private double prezzo_cons, prezzo_max;
	private int quantita;
	private String categoria;

	public ProdottoNoIdDTO() {
	}
	
	public ProdottoNoIdDTO(String marca, String modello, String descrizione, double prezzo_cons, double prezzo_max,
			int quantita, String categoria) {
		super();
		this.marca = marca;
		this.modello = modello;
		this.descrizione = descrizione;
		this.prezzo_cons = prezzo_cons;
		this.prezzo_max = prezzo_max;
		this.quantita = quantita;
		this.categoria = categoria;
	}
	
	public String getMarca() {
		return marca;
	}
	public void setMarca(String marca) {
		this.marca = marca;
	}
	public String getModello() {
		return modello;
	}
	public void setModello(String modello) {
		this.modello = modello;
	}
	public String getDescrizione() {
		return descrizione;
	}
	public void setDescrizione(String descrizione) {
		this.descrizione = descrizione;
	}
	public double getPrezzo_cons() {
		return prezzo_cons;
	}
	public void setPrezzo_cons(double prezzo_cons) {
		this.prezzo_cons = prezzo_cons;
	}
	public double getPrezzo_max() {
		return prezzo_max;
	}
	public void setPrezzo_max(double prezzo_max) {
		this.prezzo_max = prezzo_max;
	}
	public int getQuantita() {
		return quantita;
	}
	public void setQuantita(int quantita) {
		this.quantita = quantita;
	}
	public String getCategoria() {
		return categoria;
	}
	public void setCategoria(String categoria) {
		this.categoria = categoria;
	}

	@Override
	public String toString() {
		return "Prodotto [marca=" + marca + ", modello=" + modello + ", descrizione=" + descrizione
				+ ", prezzo_cons=" + prezzo_cons + ", prezzo_max=" + prezzo_max + ", quantita=" + quantita
				+ ", categoria=" + categoria + "]";
	}

}

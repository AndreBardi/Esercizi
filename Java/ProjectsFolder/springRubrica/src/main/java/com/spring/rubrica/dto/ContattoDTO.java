package com.spring.rubrica.dto;

import java.sql.Date;

public class ContattoDTO {
	private int id ;
	private String nome, cognome;
	private int numero;
	private Date anno_nascita;
	private String gruppo = "default";
	private boolean preferito = false;
	
	public ContattoDTO() {
	}

	public ContattoDTO(int id,String nome, String cognome, int numero, Date anno_nascita, String gruppo,
			boolean preferito) {
		super();
		this.id = id;
		this.nome = nome;
		this.cognome = cognome;
		this.numero = numero;
		this.anno_nascita = anno_nascita;
		this.gruppo = gruppo;
		this.preferito = preferito;
	}

	
	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public String getCognome() {
		return cognome;
	}

	public void setCognome(String cognome) {
		this.cognome = cognome;
	}

	public int getNumero() {
		return numero;
	}

	public void setNumero(int numero) {
		this.numero = numero;
	}

	public Date getAnno_nascita() {
		return anno_nascita;
	}

	public void setAnno_nascita(Date anno_nascita) {
		this.anno_nascita = anno_nascita;
	}

	public String getGruppo() {
		return gruppo;
	}

	public void setGruppo(String gruppo) {
		this.gruppo = gruppo;
	}

	public boolean isPreferito() {
		return preferito;
	}

	public void setPreferito(boolean preferito) {
		this.preferito = preferito;
	}

	@Override
	public String toString() {
		return "ContattoTelefonico [nome=" + nome + ", cognome=" + cognome + ", numero=" + numero + ", anno_nascita="
				+ anno_nascita + ", gruppo=" + gruppo + ", preferito=" + preferito + "]";
	}

}

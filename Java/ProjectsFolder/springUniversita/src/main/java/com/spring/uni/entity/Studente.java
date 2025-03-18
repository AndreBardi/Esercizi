package com.spring.uni.entity;

public class Studente {

	private int matricola, anno_nascita, iscrizione;
	private String nome, cognome, indirizzo;

	public Studente(int matricola, int anno_nascita, int iscrizione, String nome, String cognome, String indirizzo) {
		super();
		this.matricola = matricola;
		this.anno_nascita = anno_nascita;
		this.iscrizione = iscrizione;
		this.nome = nome;
		this.cognome = cognome;
		this.indirizzo = indirizzo;
	}

	public int getMatricola() {
		return matricola;
	}

	public void setMatricola(int matricola) {
		this.matricola = matricola;
	}

	public int getAnno_nascita() {
		return anno_nascita;
	}

	public void setAnno_nascita(int anno_nascita) {
		this.anno_nascita = anno_nascita;
	}

	public int getIscrizione() {
		return iscrizione;
	}

	public void setIscrizione(int iscrizione) {
		this.iscrizione = iscrizione;
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

	public String getIndirizzo() {
		return indirizzo;
	}

	public void setIndirizzo(String indirizzo) {
		this.indirizzo = indirizzo;
	}

	@Override
	public String toString() {
		return "Studente [matricola=" + matricola + ", anno_nascita=" + anno_nascita + ", iscrizione=" + iscrizione
				+ ", nome=" + nome + ", cognome=" + cognome + ", indirizzo=" + indirizzo + "]";
	}

}

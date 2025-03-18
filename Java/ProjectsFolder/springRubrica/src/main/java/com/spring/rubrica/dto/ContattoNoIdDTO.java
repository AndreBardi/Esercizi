package com.spring.rubrica.dto;

import java.sql.Date;

public class ContattoNoIdDTO {
	private String nome, cognome;
	private Date anno_nascita;
	private int numero;
	private String gruppo = "default";
	private boolean preferito = false;

	public ContattoNoIdDTO() {
		super();
	}

	public ContattoNoIdDTO(String nome, String cognome, int numero, String gruppo, Date anno_nascita,
			boolean preferito) {
		super();
		this.nome = nome;
		this.cognome = cognome;
		this.numero = numero;
		this.gruppo = gruppo;
		this.anno_nascita = anno_nascita;
		this.preferito = preferito;
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

}
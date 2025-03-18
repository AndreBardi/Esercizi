package com.spring.rubrica.dto;

import java.util.HashMap;
import java.util.Map;

public class RubricaDTO {
	private int id;
	private String proprietario;
	int anno_creazione;
	Map<Integer, ContattoDTO> contatti = new HashMap<Integer, ContattoDTO>();

	public RubricaDTO() {
	}

	public RubricaDTO(int id, String proprietario, int anno_creazione, Map<Integer, ContattoDTO> contatti) {
		super();
		this.id = id;
		this.proprietario = proprietario;
		this.anno_creazione = anno_creazione;
		this.contatti = contatti;
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getProprietario() {
		return proprietario;
	}

	public void setProprietario(String proprietario) {
		this.proprietario = proprietario;
	}

	public int getAnno_creazione() {
		return anno_creazione;
	}

	public void setAnno_creazione(int anno) {
		this.anno_creazione = anno;
	}

	public Map<Integer, ContattoDTO> getContatti() {
		return contatti;
	}

	public void setContatti(Map<Integer, ContattoDTO> contatti) {
		this.contatti = contatti;
	}

	@Override
	public String toString() {
		return "RubricaDTO [id=" + id + ", proprietario=" + proprietario + ", anno_creazione=" + anno_creazione
				+ ", contatti=" + contatti + "]";
	}

}

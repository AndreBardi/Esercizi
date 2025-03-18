package com.spring.rubrica.dto;

public class RubricaProprietario_AnnoCreazioneDTO {

	private String proprietario;
	private int anno_creazione;
	
	public RubricaProprietario_AnnoCreazioneDTO(String proprietario, int anno_creazione) {
		super();
		this.proprietario = proprietario;
		this.anno_creazione = anno_creazione;
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

	public void setAnno_creazione(int anno_creazione) {
		this.anno_creazione = anno_creazione;
	}

	@Override
	public String toString() {
		return "Proprietario_AnnoCreazioneDTO [proprietario=" + proprietario + ", anno_creazione=" + anno_creazione
				+ "]";
	}
	
	
}

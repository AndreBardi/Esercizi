package com.prod.dto;

import java.util.List;
import java.util.Map;

public class ReportDTO {
	private List<String> descrizioneProdotti;
	private int quantitàTotali;
	private int prodottiNonDisponibili;
	private double mediaPrezzo;
	private List<String> NomeProdottiNonDisp;
	private Map<String, List<Integer>> idProdotti;

	public ReportDTO() {
		
	}

	public ReportDTO(List<String> descrizioneProdotti, int quantitàTotali, int prodottiNonDisponibili,
			double mediaPrezzo, List<String> nomeProdottiNonDisp, Map<String, List<Integer>> idProdotti) {
		super();
		this.descrizioneProdotti = descrizioneProdotti;
		this.quantitàTotali = quantitàTotali;
		this.prodottiNonDisponibili = prodottiNonDisponibili;
		this.mediaPrezzo = mediaPrezzo;
		NomeProdottiNonDisp = nomeProdottiNonDisp;
		this.idProdotti = idProdotti;
	}

	public List<String> getDescrizioneProdotti() {
		return descrizioneProdotti;
	}

	public void setDescrizioneProdotti(List<String> descrizioneProdotti) {
		this.descrizioneProdotti = descrizioneProdotti;
	}

	public int getQuantitàTotali() {
		return quantitàTotali;
	}

	public void setQuantitàTotali(int quantitàTotali) {
		this.quantitàTotali = quantitàTotali;
	}

	public int getProdottiNonDisponibili() {
		return prodottiNonDisponibili;
	}

	public void setProdottiNonDisponibili(int prodottiNonDisponibili) {
		this.prodottiNonDisponibili = prodottiNonDisponibili;
	}

	public double getMediaPrezzo() {
		return mediaPrezzo;
	}

	public void setMediaPrezzo(double mediaPrezzo) {
		this.mediaPrezzo = mediaPrezzo;
	}

	public List<String> getNomeProdottiNonDisp() {
		return NomeProdottiNonDisp;
	}

	public void setNomeProdottiNonDisp(List<String> nomeProdottiNonDisp) {
		NomeProdottiNonDisp = nomeProdottiNonDisp;
	}

	public Map<String, List<Integer>> getIdProdotti() {
		return idProdotti;
	}

	public void setIdProdotti(Map<String, List<Integer>> idProdotti) {
		this.idProdotti = idProdotti;
	}

	@Override
	public String toString() {
		return "Prodotto [descrizioneProdotti=" + descrizioneProdotti + ", quantitàTotali=" + quantitàTotali
				+ ", prodottiNonDisponibili=" + prodottiNonDisponibili + ", mediaPrezzo=" + mediaPrezzo
				+ ", NomeProdottiNonDisp=" + NomeProdottiNonDisp + ", idProdotti=" + idProdotti + "]";
	}

}
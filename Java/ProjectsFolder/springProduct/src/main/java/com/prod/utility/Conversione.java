package com.prod.utility;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

import com.prod.dto.ProdottoDTO;
import com.prod.dto.ReportDTO;
import com.prod.entity.Prodotto;

public class Conversione {

	public static Prodotto daProdottoDTOAProdotto(ProdottoDTO dto) {
		return new Prodotto(dto.getId(), dto.getMarca(), dto.getModello(), dto.getDescrizione(),
				dto.getPrezzo_cons(), dto.getPrezzo_max(), dto.getQuantita(), dto.getCategoria());
	}

	public static ProdottoDTO daProdottoAProdottoDTO(Prodotto entity) {
		return new ProdottoDTO(entity.getId(), entity.getMarca(), entity.getModello(), entity.getDescrizione(),
				entity.getPrezzo_cons(), entity.getPrezzo_max(), entity.getQuantita(), entity.getCategoria());
	}

	public static ReportDTO generaReportDaProdotti(Collection<Prodotto> prodotti) {
		
		ReportDTO reportDTO = new ReportDTO();
		List<String> descrizione = new ArrayList<>();
		List<String> nomiProdottiNonDisponibili = new ArrayList<>();
		int i = 0;
		int prodNonDisp = 0;
		double mediaPrez = 0;
		for (Prodotto p : prodotti) {
			descrizione.add(p.getDescrizione());
			i += p.getQuantita();

			if (p.getQuantita() == 0) {
				prodNonDisp++;
				nomiProdottiNonDisponibili.add(p.getMarca() + " " + p.getModello()); 
			}

			mediaPrez += p.getPrezzo_cons();
		}
		mediaPrez=mediaPrez/prodotti.size();
		// inserimento descrizioni
		reportDTO.setDescrizioneProdotti(descrizione);
		reportDTO.setQuantitàTotali(i);
		reportDTO.setMediaPrezzo(mediaPrez);
		reportDTO.setNomeProdottiNonDisp(nomiProdottiNonDisponibili);
		reportDTO.setProdottiNonDisponibili(prodNonDisp);
		reportDTO.setIdProdotti(null);

		// inserimento della somma dei pezzi prodotti

		return reportDTO;
	}

}
package com.prod.service;

import java.util.ArrayList;
import java.util.List;

import com.prod.dao.ProdottoDAO;
import com.prod.dto.ProdottoDTO;
import com.prod.dto.ReportDTO;
import com.prod.entity.Prodotto;
import com.prod.utility.Conversione;

public class ProdottoService {
	
private ProdottoDAO dao = new ProdottoDAO();
	
	public boolean caricaProd(ProdottoDTO dto) {
		Prodotto entity = Conversione.daProdottoDTOAProdotto(dto);
		
		return dao.insert(entity);
	}

	public ProdottoDTO cercaPerId(int id) {
		Prodotto utente = dao.selectById(id);
		
		if(utente != null) {
			ProdottoDTO dto = Conversione.daProdottoAProdottoDTO(utente);
			return dto;
		}
		return null;
	}

	public List<ProdottoDTO> mostraTutti() {
		List<Prodotto> lista = dao.selectAll();
		List<ProdottoDTO> listaDto = new ArrayList<>();
		for (int i=0;i<lista.size();i++) {
			listaDto.add(Conversione.daProdottoAProdottoDTO(lista.get(i)));
		}
		return listaDto;
	}

	public ReportDTO getReport() {
		return Conversione.generaReportDaProdotti(dao.selectAll());
	}
	
	

}

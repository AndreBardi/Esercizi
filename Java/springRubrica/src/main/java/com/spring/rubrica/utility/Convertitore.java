package com.spring.rubrica.utility;

import java.util.HashMap;
import java.util.Map;

import com.spring.rubrica.dto.ContattoDTO;
import com.spring.rubrica.dto.RubricaDTO;
import com.spring.rubrica.entity.Contatto;
import com.spring.rubrica.entity.Rubrica;

public class Convertitore {

	public static Contatto DaContattoDTOAContatto(ContattoDTO dto) {
		return new Contatto(dto.getId(), dto.getNome(), dto.getCognome(), dto.getNumero(), dto.getAnno_nascita(),
				dto.getGruppo(), dto.isPreferito());
	}

	public static ContattoDTO DaContattoAContattoDTO(Contatto entity) {
		return new ContattoDTO(entity.getId(), entity.getNome(), entity.getCognome(), entity.getNumero(),
				entity.getAnno_nascita(), entity.getGruppo(), entity.isPreferito());
	}

	public static Rubrica DaRubricaDTOARubrica(RubricaDTO dto) {
		Map<Integer, Contatto> contatti = new HashMap<Integer, Contatto>();
		for (ContattoDTO c : dto.getContatti().values()) {
			Contatto contatto = DaContattoDTOAContatto(c);
			contatti.put(c.getId(), contatto);

		}
		return new Rubrica(dto.getId(), dto.getProprietario(), dto.getAnno_creazione(), contatti);

	}

	public static RubricaDTO DaRubricaARubricaDTO(Rubrica entity) {
		Map<Integer, ContattoDTO> contatti = new HashMap<Integer, ContattoDTO>();
		for (Contatto c : entity.getContatti().values()) {
			contatti.put(c.getId(), DaContattoAContattoDTO(c));

		}
		return new RubricaDTO(entity.getId(), entity.getProprietario(), entity.getAnno_creazione(), contatti);
	}

}

package com.spring.rubrica.service;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import org.springframework.stereotype.Service;

import com.spring.rubrica.dao.RubricaDAO;
import com.spring.rubrica.dto.RubricaProprietario_AnnoCreazioneDTO;
import com.spring.rubrica.dto.NumeroContattiDiRubricaDTO;
import com.spring.rubrica.dto.RubricaDTO;
import com.spring.rubrica.dto.RubricaListaProprietariDTO;
import com.spring.rubrica.entity.Rubrica;
import com.spring.rubrica.utility.Convertitore;

@Service
public class RubricaServiceImpl implements RubricaService {

	private RubricaDAO dao;

	public boolean inserisciRubrica(RubricaDTO dto) {
		Rubrica entity = Convertitore.DaRubricaDTOARubrica(dto);
		return dao.insert(entity);
	}

	public RubricaDTO visualizzaPerId(int id) {
		Rubrica rubrica = dao.selectById(id);
		if (rubrica != null) {
			RubricaDTO dto = Convertitore.DaRubricaARubricaDTO(rubrica);
			return dto;
		}
		return null;
	}

	public List<RubricaDTO> VisualizzaRubriche() {
		List<Rubrica> rubriche = dao.selectAll();
		List<RubricaDTO> rubricheDTO = new ArrayList<RubricaDTO>();
		for (Rubrica rub : rubriche) {
			RubricaDTO dto = Convertitore.DaRubricaARubricaDTO(rub);
			rubricheDTO.add(dto);
		}
		return rubricheDTO;

	}

	public RubricaDTO cancellaRubrica(int id) {
		Rubrica rubrica = dao.selectById(id);
		if (rubrica != null) {
			RubricaDTO dto = Convertitore.DaRubricaARubricaDTO(rubrica);
			dao.delete(id);
			return dto;
		}
		return null;
	}

	public RubricaProprietario_AnnoCreazioneDTO visualizzaRubrica(int id) {
		Rubrica rubrica = dao.selectById(id);
		if (rubrica != null) {
			RubricaDTO dto = Convertitore.DaRubricaARubricaDTO(rubrica);
			return new RubricaProprietario_AnnoCreazioneDTO(dto.getProprietario(), dto.getAnno_creazione());
		}
		return null;
	}

	public RubricaDTO ModificaProprietario(int id, String nuovoPropietario) {
		Rubrica rubrica = dao.selectById(id);
		RubricaDTO dto = Convertitore.DaRubricaARubricaDTO(rubrica);
		dto.setProprietario(nuovoPropietario);
		return dto;
	}

	public RubricaDTO ModificaAnnoCreazione(int id, int anno) {
		Rubrica rubrica = dao.selectById(id);
		RubricaDTO dto = Convertitore.DaRubricaARubricaDTO(rubrica);
		dto.setAnno_creazione(anno);
		return null;

	}
	
	public RubricaListaProprietariDTO VisualizzaProprietari() {
		ArrayList<String> propietariDTO = new ArrayList<String>();
		ArrayList<Rubrica> rubriche = new ArrayList<Rubrica>(dao.selectAll());
		int numero_totale = 0;
		for (Rubrica rubrica : rubriche) {
			RubricaDTO dto = Convertitore.DaRubricaARubricaDTO(rubrica);
			propietariDTO.add(dto.getProprietario());
			numero_totale++;
		}
		return new RubricaListaProprietariDTO(propietariDTO, numero_totale);
	}
	
	public RubricaProprietario_AnnoCreazioneDTO RubricaPiuVecchia() {
		ArrayList<Rubrica> rubriche = new ArrayList<>(dao.selectAll());
		ArrayList<Integer> anni_creazioni = new ArrayList<Integer>();

		for (Rubrica rubrica : rubriche) {
			anni_creazioni.add(rubrica.getAnno_creazione());
			int max = Collections.max(anni_creazioni);

			return new RubricaProprietario_AnnoCreazioneDTO(rubrica.getProprietario(), max);
		}
		return null;

	}

	public List<Integer> ListaAnniCreazione(){
		ArrayList<Integer> annicreazione = new ArrayList<Integer>();
		ArrayList<Rubrica> rubriche = new ArrayList<>(dao.selectAll());
		for(Rubrica rubrica: rubriche) {
			annicreazione.add(rubrica.getAnno_creazione());
		}
		Collections.sort(annicreazione);
		return  annicreazione;
	}
	
	public NumeroContattiDiRubricaDTO NumeroContattiInRubrica(int id) {
		Rubrica rubrica = dao.selectById(id);
		RubricaDTO dto = Convertitore.DaRubricaARubricaDTO(rubrica);
		return new NumeroContattiDiRubricaDTO(dto.getProprietario(),dto.getContatti().size());
	}

}
package com.spring.rubrica.service;

import java.util.ArrayList;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.spring.rubrica.dao.RubricaDAO;
import com.spring.rubrica.dto.ContattoDTO;
import com.spring.rubrica.dto.ContattoNomeCognomeDTO;
import com.spring.rubrica.dto.ContattoNoIdDTO;
import com.spring.rubrica.entity.Contatto;
import com.spring.rubrica.entity.Rubrica;
import com.spring.rubrica.utility.Convertitore;

@Service
public class ContattoServiceImpl implements ContattoService {

	@Autowired
	RubricaDAO dao;

	public boolean inserisciContatto(int idRubrica, ContattoDTO dto) {
		Rubrica rubrica = dao.selectById(idRubrica);
		Contatto contatto = Convertitore.DaContattoDTOAContatto(dto);
		if (rubrica.getContatti().containsKey(contatto.getId())) {
			throw new RuntimeException("Contatto già esistente.");
		}
		rubrica.getContatti().put(contatto.getId(), contatto);
		return true;
	}

	public ContattoDTO visualizzaContatto(int idRubrica, int id) {
		Rubrica rubrica = dao.selectById(idRubrica);
		ContattoDTO dto = new ContattoDTO();
		if (rubrica != null) {
			Contatto contatto = rubrica.getContatti().get(id);
			if (contatto != null) {
				dto = Convertitore.DaContattoAContattoDTO(contatto);

			} else {
				throw new RuntimeException("Impossibile visualizzare il contatto.Id contatto non trovato");
			}
		}
		return dto;
	}

	public ContattoDTO modifica(int idRubrica, int id, ContattoNoIdDTO dto) {
		Rubrica rubrica = dao.selectById(idRubrica);
		ContattoDTO dtoo = new ContattoDTO();
		if (rubrica != null) {
			Contatto contatto = rubrica.getContatti().get(id);
			if (contatto != null) {
				contatto.setNome(dto.getNome());
				contatto.setCognome(dto.getCognome());
				contatto.setNumero(dto.getNumero());
				contatto.setGruppo(dto.getGruppo());
				contatto.setAnno_nascita(dto.getAnno_nascita());
				contatto.setPreferito(dto.isPreferito());

				rubrica.getContatti().put(id, contatto);
				dtoo = Convertitore.DaContattoAContattoDTO(contatto);
			} else {
				throw new RuntimeException("Impossibile modificare il contatto.Id contatto non trovato");
			}
		}
		return dtoo;
	}

	public ContattoDTO cancella(int idRubrica, int id) {
		Rubrica rubrica = dao.selectById(idRubrica);
		ContattoDTO dto = null;
		if (rubrica != null) {
			Contatto contatto = rubrica.getContatti().get(id);
			if (contatto != null) {
				rubrica.getContatti().remove(id, contatto);
				dto = Convertitore.DaContattoAContattoDTO(contatto);

			} else {
				throw new RuntimeException("Impossibile eliminare il contatto .Id non trovato");
			}
		}
		return dto;
	}

	public List<ContattoDTO> listaContatti(int idRubrica) {
		Rubrica rubrica = dao.selectById(idRubrica);
		ArrayList<ContattoDTO> contattiDto = new ArrayList<>();
		ArrayList<Contatto> contatti = new ArrayList<>(rubrica.getContatti().values());
		if (rubrica != null) {
			for (Contatto contatto : contatti) {
				ContattoDTO dto = Convertitore.DaContattoAContattoDTO(contatto);
					contattiDto.add(dto);
				}
			
		} if(contattiDto.size() != 0) {
			return contattiDto;
		} else {
			throw new RuntimeException("La rubrica è vuota.");
		}
	}

	public Integer NumeroContatti(int idRubrica) {
		Rubrica rubrica = dao.selectById(idRubrica);
		int dimensione = 0;
		if (rubrica != null) {
			dimensione = rubrica.getContatti().size();
		} if(dimensione != 0) {
			return dimensione;
		} else {
			throw new RuntimeException("La rubrica è vuota. Il numero di contatti è 0");
		}
		
	}

	public ContattoDTO VisualizzaConNumero(int idRubrica, int numero) {
		Rubrica rubrica = dao.selectById(idRubrica);
		ContattoDTO dto = new ContattoDTO();
		if (rubrica != null) {
			for (Contatto contatto : rubrica.getContatti().values()) {
					if (contatto.getNumero() == numero) {
						dto = Convertitore.DaContattoAContattoDTO(contatto);
					} else {
						throw new RuntimeException("Numero errato.Contatto non trovato.");
					}
				}
			}
		return dto;
	}

	public List<ContattoNomeCognomeDTO> VisualizzaConGruppo(int idRubrica, String gruppo) {
		Rubrica rubrica = dao.selectById(idRubrica);
		ArrayList<ContattoNomeCognomeDTO> contatti = new ArrayList<ContattoNomeCognomeDTO>();
		if (rubrica != null) {
			for (Contatto contatto : rubrica.getContatti().values()) {
					if (contatto.getGruppo().equals(gruppo)) {
						ContattoDTO dto = Convertitore.DaContattoAContattoDTO(contatto);
						contatti.add(new ContattoNomeCognomeDTO(dto.getNome(), dto.getCognome()));
					}
			}
		} if(contatti.size() != 0) {
			return contatti;
		} else {
			throw new RuntimeException("Lista vuota.Contatti non trovati dentro il gruppo di appartenenza.");
		}
		
	}

	public Integer NumeroContattiGruppo(int idRubrica, String gruppo) {
		ArrayList<Contatto> contatti = new ArrayList<Contatto>();
		Rubrica rubrica = dao.selectById(idRubrica);
		if (rubrica != null) {
			for (Contatto contatto : rubrica.getContatti().values()) {
				if (contatto.getGruppo().equals(gruppo)) {
					contatti.add(contatto);
				}
			}
		}if(contatti.size() != 0) {
			return contatti.size();
		}else {
			throw new RuntimeException("Impossibile eliminare i contatti.Contatti non trovati dentro il gruppo di appartenenza.");
		}
	}

	public List<ContattoDTO> CancellaGruppoContatti(int idRubrica, String gruppo) {
		ArrayList<ContattoDTO> contatti = new ArrayList<ContattoDTO>();
		Rubrica rubrica = dao.selectById(idRubrica);
		if (rubrica != null) {
			for (Contatto contatto : rubrica.getContatti().values()) {
					if (contatto.getGruppo().equals(gruppo)) {
						ContattoDTO dto = Convertitore.DaContattoAContattoDTO(contatto);
						rubrica.getContatti().remove(contatto.getId(), contatto);
						contatti.add(dto);
					}
				} 
		} if(contatti.size() != 0) {
			return contatti;
		}else {
			throw new RuntimeException("Impossibile eliminare i contatti.Contatti non trovati dentro il gruppo di appartenenza.");
		}

	}

	public ContattoDTO modificaStatoPreferito(int idRubrica, int id) {
		Rubrica rubrica = dao.selectById(idRubrica);
		ContattoDTO dto = new ContattoDTO();
		if (rubrica != null) {
			Contatto contatto = rubrica.getContatti().get(id);
			if (contatto != null) {
				contatto.setPreferito(true);
				dto = Convertitore.DaContattoAContattoDTO(contatto);
			} else {
				throw new RuntimeException("Impossibile modificare lo stato preferito del contatto.Contatto non trovato");
			}
		}
		return dto;

	}

	public List<ContattoDTO> ContattiPreferiti(int idRubrica) {
		ArrayList<ContattoDTO> preferiti = new ArrayList<ContattoDTO>();
		Rubrica rubrica = dao.selectById(idRubrica);
		if (rubrica != null) {
			for (Contatto contatto : rubrica.getContatti().values()) {
				ContattoDTO dto = Convertitore.DaContattoAContattoDTO(contatto);
				if (dto.isPreferito() == true) {
					preferiti.add(dto);
				}
			}
		}if (preferiti.size() != 0) {
			return preferiti;
		}else {
			throw new RuntimeException("Lista di contatti preferiti vuota.");
		}
		
	}

}
package com.spring.uni.service;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.spring.uni.dao.StudentiDAO;
import com.spring.uni.dto.CognomeNascitaDTO;
import com.spring.uni.dto.ProfessoriDTO;
import com.spring.uni.dto.StudenteDTO;
import com.spring.uni.entity.Studente;
import com.spring.uni.utility.Convertitore;

@Service
public class StudentiServiceImpl implements StudentiService {
	
	@Autowired
	private StudentiDAO dao;
	
	public boolean registra(StudenteDTO dto) {
		Studente entity = Convertitore.daStudenteDTOAStudente(dto);
		return dao.insert(entity);
	}
	
	public StudenteDTO cercaStudente(int matricola) {
		Studente studente = dao.selectByMatricola(matricola);
		if(studente!=null) {
			StudenteDTO dto = Convertitore.daStudenteAStudenteDTO(studente);
			return dto;
		}
		return null;
		}
	
	public List<StudenteDTO> mostraStudenti(){
		List<Studente> studenti = dao.selectAll();
		List<StudenteDTO> studentiDTO = new ArrayList<>();
		for(Studente studente:studenti) {
			StudenteDTO dto = Convertitore.daStudenteAStudenteDTO(studente);
			studentiDTO.add(dto);
		}
		return studentiDTO;
		}
	
	public StudenteDTO eliminaStudente(int matricola) {
		Studente studente = dao.selectByMatricola(matricola);
		if(studente!=null) {
			StudenteDTO dto = Convertitore.daStudenteAStudenteDTO(studente);
			dao.delete(matricola);
			return dto;
		}
		return null;
	}
	
	public StudenteDTO modificaStudente(int matricola, String indirizzo) {
		Studente studente = dao.selectByMatricola(matricola);
		if(studente!=null) {
			dao.update(matricola, indirizzo);
			StudenteDTO dto = Convertitore.daStudenteAStudenteDTO(studente);
			return dto;
		}
		return null;
	}
	
	public List<String> mostraNomi(){
		List<Studente> studenti = dao.selectAll();
		List<String> nomi = new ArrayList<>();
		for(Studente studente : studenti) {
			StudenteDTO dto = Convertitore.daStudenteAStudenteDTO(studente);
			String nome = dto.getNome();
			nomi.add(nome);
		}
		return nomi;
	}
	
}


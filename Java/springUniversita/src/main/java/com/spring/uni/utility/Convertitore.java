package com.spring.uni.utility;

import com.spring.uni.dto.ProfessoriDTO;
import com.spring.uni.dto.StudenteDTO;
import com.spring.uni.entity.Professore;
import com.spring.uni.entity.Studente;

public class Convertitore {
	
	public static Studente daStudenteDTOAStudente(StudenteDTO dto) {
		return new Studente(dto.getMatricola(), dto.getAnno_nascita(), dto.getAnno_immatricolazione(), dto.getNome(), dto.getCognome(), dto.getIndirizzo());
	}
	
	public static StudenteDTO daStudenteAStudenteDTO(Studente entity) {
		return new StudenteDTO(entity.getMatricola(), entity.getNome(), entity.getCognome(), entity.getIndirizzo(), entity.getAnno_nascita(), entity.getIscrizione());
	}
	
	public static Professore daProfessoreDTOAProfessore(ProfessoriDTO dto) {
		return new Professore(dto.getId(), dto.getNome(), dto.getCognome(), dto.getMateria());
	}
	
	public static ProfessoriDTO daProfessoreAProfessoreDTO(Professore entity) {
		return new ProfessoriDTO(entity.getId(), entity.getNome(), entity.getCognome(), entity.getMateria());
	}
}
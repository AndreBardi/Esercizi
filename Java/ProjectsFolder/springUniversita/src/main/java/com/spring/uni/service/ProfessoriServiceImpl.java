package com.spring.uni.service;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.spring.uni.dao.ProfessoriDAO;
import com.spring.uni.dto.ProfessoriDTO;
import com.spring.uni.dto.StudenteDTO;
import com.spring.uni.entity.Professore;
import com.spring.uni.entity.Studente;
import com.spring.uni.utility.Convertitore;

@Service
public class ProfessoriServiceImpl implements ProfessoriService {
	
	@Autowired
	private ProfessoriDAO dao;;
	
	public boolean registra(ProfessoriDTO dto) {
		Professore entity = Convertitore.daProfessoreDTOAProfessore(dto);
		return dao.insert(entity);
	}
	
	public ProfessoriDTO cercaProfessore(int id) {
		Professore professore = dao.selectById(id);
		if(professore!=null) {
			ProfessoriDTO dto = Convertitore.daProfessoreAProfessoreDTO(professore);
			return dto;
		}
		return null;
	}
	
	public List<ProfessoriDTO> mostraProfessori(){
		List<Professore> professori = dao.selectAll();
		List<ProfessoriDTO> professoriDTO = new ArrayList<>();
		for(Professore professore:professori) {
			ProfessoriDTO dto = Convertitore.daProfessoreAProfessoreDTO(professore);
			professoriDTO.add(dto);
		}
		return professoriDTO;
	}
	
	public ProfessoriDTO eliminaProfessore(int id) {
		Professore professore = dao.selectById(id);
		if(professore!=null) {
			ProfessoriDTO dto = Convertitore.daProfessoreAProfessoreDTO(professore);
			dao.delete(id);
			return dto;
		}
		return null;
	}
	
	public ProfessoriDTO modificaProfessore(int id, String materia) {
		Professore professore = dao.selectById(id);
		if(professore!=null) {
			dao.update(id, materia);
			ProfessoriDTO dto = Convertitore.daProfessoreAProfessoreDTO(professore);
			return dto;
		}
		return null;
	}
	
    public List<ProfessoriDTO> materiaProf(String materia){
    	List<Professore>professori = dao.selectAll();
    	List<ProfessoriDTO> profMateria = new ArrayList<>();
    	for(Professore professore: professori) {
    		ProfessoriDTO dto = Convertitore.daProfessoreAProfessoreDTO(professore);
    		if(dto.getMateria().equals(materia)) {
    			profMateria.add(dto);
    		}
    	}
    	return profMateria;
    }
    
    public List<ProfessoriDTO> orderByCognome(){
    	List<Professore>professori = dao.selectAll();
    	List<ProfessoriDTO> profMateria = new ArrayList<>();
    	for(Professore professore: professori) {
    		ProfessoriDTO dto = Convertitore.daProfessoreAProfessoreDTO(professore);
    		profMateria.add(dto);
    		profMateria.sort(Comparator.comparing(ProfessoriDTO::getCognome));
    	}
    	return profMateria;
    }
    
    public List<String> materie(){
    	List<Professore>professori = dao.selectAll();
    	List<String> materie = new ArrayList<>();
    	for(Professore professore:professori) {
    		ProfessoriDTO dto = Convertitore	.daProfessoreAProfessoreDTO(professore);
    		String materia = dto.getMateria();
    		if(!materie.contains(materia)) {
    			materie.add(materia);
    		}
    	}
    	return materie;
    }
}
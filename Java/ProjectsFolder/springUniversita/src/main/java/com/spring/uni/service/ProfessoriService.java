package com.spring.uni.service;

import java.util.List;

import com.spring.uni.dto.ProfessoriDTO;

public interface ProfessoriService {
	
	public boolean registra(ProfessoriDTO dto);
	public ProfessoriDTO cercaProfessore(int id);
	public List<ProfessoriDTO> mostraProfessori();
	public ProfessoriDTO eliminaProfessore(int id);
	public ProfessoriDTO modificaProfessore(int id, String materia);
	public List<ProfessoriDTO> materiaProf(String materia);
	public List<ProfessoriDTO> orderByCognome();
	public List<String> materie();
}

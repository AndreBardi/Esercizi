package com.spring.uni.dao;

import java.util.List;

import com.spring.uni.entity.Professore;

public interface ProfessoriDAO {
	
	public boolean insert(Professore professore);
	public Professore selectById(int id);
	public List<Professore> selectAll();
	public Professore delete(int id);
	public Professore update(int id, String materia);

}
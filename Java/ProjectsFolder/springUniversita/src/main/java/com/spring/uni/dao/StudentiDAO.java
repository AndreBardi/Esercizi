package com.spring.uni.dao;

import java.util.List;

import com.spring.uni.entity.Studente;

public interface StudentiDAO {
	
	public boolean insert(Studente studente);
	public Studente selectByMatricola(int matricola);
	public List<Studente> selectAll();
	public Studente delete(int matricola);
	public Studente update(int matricola, String indirizzo);
}
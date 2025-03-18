package com.prod.dao;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import com.prod.entity.Prodotto;

public class ProdottoDAO {
	
	private Map<Integer, Prodotto> mappa = new HashMap<>();

	public boolean insert(Prodotto utente) {
		if(mappa.containsKey(utente.getId()))
			return false;
		
		mappa.put(utente.getId(), utente);
		return true;

	}
	public List<Prodotto> selectAll(){
		return new ArrayList<>(mappa.values());
	}

	public Prodotto selectById(Integer idUtente) {
		return mappa.get(idUtente);
	}
	
	public boolean delete(Integer idUtente) {
		Prodotto utente = mappa.remove(idUtente);
		return utente!=null;
	}
	
	

}

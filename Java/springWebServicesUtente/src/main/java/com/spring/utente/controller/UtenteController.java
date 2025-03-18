package com.spring.utente.controller;

import java.util.List;

import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.spring.utente.dto.NomeCognomeDTO;
import com.spring.utente.dto.UtenteDTO;
import com.spring.utente.service.UtenteService;

@RestController
@RequestMapping(path="/utenti")
public class UtenteController {
	
	private UtenteService service = new UtenteService();

	@GetMapping(path="/registra", consumes = "application/json")
	public boolean registra(@RequestBody  UtenteDTO dto) {
		// fake
		//System.out.println("ho registrato l'utente: "  + utente);
		//return true;
		
		return service.registra(dto);
		
	}
		
	@GetMapping(path="/cerca/{id}", produces = "application/json")
	public UtenteDTO cercaPerId(@PathVariable  int id) {
		// fake
		//return new Utente(id, "mario", "rossi", "mario", "red");
		
		return service.cercaPerId(id);
	}
	
	@GetMapping(path="/mostraTutti", produces = "application/json")
	public List<UtenteDTO> mostraTutti(){
		return service.mostraTutti();
	}
	
	@GetMapping(path="/modificaPassword/{idUtente}/{password}", produces = "application/json")
	public UtenteDTO modificaMail(@PathVariable int idUtente, @PathVariable String password) {
		return service.updatePassword(idUtente, password);
	}
	
	@GetMapping(path="/cancella/{idUtente}", produces = MediaType.APPLICATION_JSON_VALUE)
	public UtenteDTO cancellaUtente(@PathVariable int idUtente) {
		return service.cancella(idUtente);
	}

	@GetMapping(path="/nomeCognome/{id}", produces = MediaType.APPLICATION_JSON_VALUE)
	public NomeCognomeDTO getNomeCognome(@PathVariable int id) {
		return service.getNomeCognome(id);
	}
	
}
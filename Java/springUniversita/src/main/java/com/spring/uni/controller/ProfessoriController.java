package com.spring.uni.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.spring.uni.dto.ProfessoriDTO;
import com.spring.uni.service.ProfessoriService;

@RestController
@RequestMapping(path = "/professori")
public class ProfessoriController {

	@Autowired
	private ProfessoriService service;

	@GetMapping(path = "/registra", consumes = "application/json")
	public boolean registra(@RequestBody ProfessoriDTO dto) {
		return service.registra(dto);
	}

	@GetMapping(path = "/cercaProfessore/{id}", produces = "application/json")
	public ProfessoriDTO cerca(@PathVariable int id) {
		return service.cercaProfessore(id);
	}

	@GetMapping(path = "/mostraProfessori", produces = "application/json")
	public List<ProfessoriDTO> visualizza() {
		return service.mostraProfessori();
	}

	@GetMapping(path = "/eliminaProfessore/{id}", produces = "application/json")
	public ProfessoriDTO elimina(@PathVariable int id) {
		return service.eliminaProfessore(id);
	}

	@GetMapping(path = "/modificaProfessore/{id}/{materia}", produces = "application/json")
	public ProfessoriDTO modifica(@PathVariable int id, @PathVariable String materia) {
	    return service.modificaProfessore(id, materia);
	}				

	@GetMapping(path = "/mostraProfessoriMateria/{materia}", produces = "application/json")
	public List<ProfessoriDTO> mostra(@PathVariable String materia) {
		return service.materiaProf(materia);
	}

	@GetMapping(path = "/professoriOrdinati", produces = "application/json")
	public List<ProfessoriDTO> ordina() {
		return service.orderByCognome();
	}

	@GetMapping(path = "/mostraMaterie", produces = "application/json")
	public List<String> materie() {
		return service.materie();
	}

}

package com.spring.utente.controller;

import 	java.util.ArrayList;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import com.spring.utente.service.UtenteService;


@RestController
public class UtenteController {

	@Autowired
	private UtenteService service;
	
	@GetMapping(path="/registra", consumes = "application/json")
	public boolean registra(@RequestBody UtenteDTO dto) {
		
	}
}

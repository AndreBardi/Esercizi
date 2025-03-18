package com.prod.controller;

import java.util.List;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.prod.service.ProdottoService;
import com.prod.dto.ProdottoDTO;
import com.prod.dto.ProdottoNoIdDTO;
import com.prod.dto.ReportDTO;
import com.prod.entity.Prodotto;


@RestController
@RequestMapping(path="/prodotti")
public class ControllerProdotto {
	private ProdottoService service = new ProdottoService();
	
	
	@GetMapping(path="/carica", consumes = "application/json")
	public boolean caricaProdotto(@RequestBody ProdottoDTO dto) {
		return service.caricaProd(dto);
	}
	
	@GetMapping(path="/mostraId/{id}", produces = "application/json")
	public ProdottoDTO mostraId(@PathVariable int id){
		return service.cercaPerId(id);
	}
	
	 @GetMapping(path="mostraTutti", produces = "application/json")
	public List<ProdottoDTO> mostraTutti(){
		 return service.mostraTutti();
	 }
	 
	 @GetMapping(path="report", produces = "application/json")
	 public ReportDTO Report() {
		 return service.getReport();
	}
	 
	 
}
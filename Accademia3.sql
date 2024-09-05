CREATE DATABASE Accademia3:

CREATE TYPE Strutturato AS ENUM (
    'Ricercatore', 'Professore Associato', 'Professore Ordinario');
	
CREATE TYPE LavoroProgetto AS ENUM (
    'Ricerca e Sviluppo', 'Dimostrazione', 'Management', 'Altro');
	
CREATE TYPE LavoroNonProgettuale as ENUM ('Didattica', 'Ricerca', 'Missione', 'Incontro Dipartimentale', 'Incontro 					 
	Accademico', 'Altro');
	
CREATE TYPE CausaAssenza as ENUM (
    'Chiusura Universitaria', 'Maternità', 'Malattia');
	
CREATE DOMAIN PosInteger as Integer
	default 0
	check (value >= 0)
	
CREATE TYPE StringaM as String
	varchar(100)
	
CREATE DOMAIN NumeroOre as Integer
	default 0
	check (value >= 0 and value <= 8)

CREATE DOMAIN DENARO AS Real
    default 0
    check (value >= 0)
	
	
	
create TABLE Persona (
    id NOT NULL,
    nome NOT NULL,
    cognome NOT NULL,
    posizione Strutturato,
    stipendio DENARO
);
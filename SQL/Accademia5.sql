--QUERY 1
SELECT w.nome, w.inizio, w.fine
FROM WP AS w, Progetto AS pr
WHERE w.progetto = pr.id 
AND pr.nome = 'Pegasus';

--QUERY 2
SELECT distinct pe.nome, pe.cognome, pe.posizione
FROM Persona AS pe, AttivitaProgetto AS a, Progetto AS pr
WHERE pe.id = a.persona
AND pr.nome = 'Pegasus'
AND pr.id = a.progetto 
order by cognome desc ;

--QUERY 3
SELECT distinct pe.nome, pe.cognome, pe.posizione
FROM Persona AS pe, AttivitaProgetto AS a, AttivitaProgetto AS a1, Progetto AS pr
WHERE pe.id = a.persona
AND pr.nome = 'Pegasus'
AND pr.id = a.progetto 
AND a.persona = a1.persona
AND a.id <> a1.id;

--QUERY 4
SELECT distinct nome ,cognome, posizione
FROM Persona AS p, assenza AS a
WHERE p.id = a.persona
AND p.posizione = 'Professore Ordinario'
AND a.tipo = 'Malattia';

--QUERY 5
SELECT distinct nome ,cognome, posizione
FROM Persona AS p, assenza AS a, assenza AS a1
WHERE p.id = a.persona
AND p.posizione = 'Professore Ordinario'
AND a.tipo = 'Malattia'
AND a.persona = a1.persona
AND a.id <> a1.id ;

--QUERY 6
SELECT distinct nome,cognome,posizione
FROM Persona AS p, AttivitaNonProgettuale AS a
WHERE p.id = a.persona
AND p.posizione = 'Ricercatore'
AND a.tipo = 'Didattica';

--QUERY 7
SELECT distinct nome, cognome, posizione
FROM Persona AS p, AttivitaNonProgettuale AS a, AttivitaNonProgettuale AS a1
WHERE p.id = a.persona
AND p.posizione = 'Ricercatore'
AND a.tipo = 'Didattica'
AND a.persona = a.persona
AND a.id <> a1.id ;

--QUERY 8
SELECT  nome, cognome, posizione
FROM Persona AS p, AttivitaNonProgettuale AS anp, AttivitaProgetto AS ap
WHERE p.id = anp.persona
AND anp.persona = ap.persona
AND anp.giorno = ap.giorno ;

--QUERY 9
SELECT p.nome, p.cognome, ap.giorno, pr.nome AS att_prj, ap.OreDurata AS h_prj, anp.tipo AS att_noprj, anp.OreDurata AS h_noprj
FROM Persona AS p, AttivitaProgetto AS ap, AttivitaNonProgettuale AS anp, Progetto AS pr
WHERE p.id = anp.persona
AND anp.persona = ap.persona
AND anp.giorno = ap.giorno
AND ap.progetto = pr.id ;

--QUERY 10
SELECT nome , cognome 
FROM Persona AS p , assenza AS a , AttivitaProgetto AS ap
WHERE p.id = a.persona
AND a.giorno = ap.giorno ;

--QUERY 11
SELECT p.nome , p.cognome , a.giorno , a.tipo AS causa_ass ,pr.nome AS progetto,ap.OreDurata AS ore_att_prj
FROM Persona AS p , assenza AS a , AttivitaProgetto AS ap , Progetto AS pr
WHERE p.id = a.persona
AND a.giorno = ap.giorno
AND ap.progetto = pr.id ;

--QUERY 12
SELECT  distinct w1.nome
FROM WP AS w1 , WP AS w2
WHERE w1.nome = w2.nome
AND w1.progetto <> w2.progetto ;
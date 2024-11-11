--query 1

SELECT distinct p.id , p.nome , p.cognome
FROM persona AS p
JOIN Assenza  AS ass
on ass.persona = p.id
full  OUTER JOIN AttivitaNonProgettuale AS a1 
on a1.giorno = ass.giorno 
full OUTER JOIN AttivitaProgetto AS a2
on a2.giorno = ass.giorno 
GROUP BY p.id
HAVING count(a1.giorno) = 0
AND count(a2.giorno)= 0;

--query 2

-- SELECT p.id ,p.nome, p.cognome
-- FROM persona AS p
-- LEFT OUTER JOIN AttivitaProgetto AS ap ON p.id = ap.persona
-- LEFT OUTER JOIN progetto AS pr ON pr.id = ap.progetto 
-- AND pr.nome = 'Pegasus'
-- GROUP BY p.id
-- HAVING count(ap.progetto) = 0;

WITH Persona_id as (
  SELECT p.id FROM Persona p

  EXCEPT

  SELECT distinct ap.persona
  from AttivitaProgetto ap, Progetto prog
  WHERE prog.nome = 'Pegasus'
  AND ap.giorno BETWEEN prog.inizio AND prog.fine 
)

SELECT p.id, p.nome,  p.cognome
FROM Persona p, Persona_id persona_id
WHERE p.id = persona_id.id
 and 
--query3

  WITH tot_sti AS (
    SELECT max(stipendio) AS max_sti
    FROM persona
    WHERE  (posizione ='Professore Associato' or posizione = 'Professore Ordinario')
)
SELECT p.id , p.nome , p.cognome , p.stipendio
FROM persona AS p , tot_sti AS ts
WHERE p.posizione = 'Ricercatore'
AND ts.max_sti < p.stipendio
GROUP BY p.id

--query4
WITH bdg_tot AS (
    SELECT avg(pr.budget) AS max_bdg
    FROM progetto AS pr 
)
	
SELECT p.id,p.nome,p.cognome
FROM persona AS p, progetto AS pr, AttivitaProgetto AS ap, bdg_tot AS bt
WHERE pr.id = ap.progetto
AND p.id = ap.persona
AND bt.max_bdg < pr.budget
GROUP BY p.id;
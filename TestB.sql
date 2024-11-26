/* Query 1
Qual è il numero di progetti a cui partecipa ogni
professore ordinario. Per ogni professore ordinario,
restituire nome, cognome, numero di progetti nei quali è
coinvolto.
*/

SELECT p.id, p.nome, p.cognome, COUNT(ap.progetto)
FROM Persona AS p
JOIN AttivitaProgetto as ap ON p.id = ap.persona
WHERE p.posizione = 'Professore Ordinario'
GROUP BY p.id, p.nome, p.cognome;


/* Query 2
Qual è il numero medio di ore delle attività progettuali
svolte da ogni ricercatore. Per ogni ricercatore, restituire
nome, cognome e numero medio di ore delle sue attività
progettuali (in qualsivoglia progetto)
*/

SELECT p.id, p.nome, p.cognome, avg(ap.oreDurata)
FROM Persona AS p
JOIN AttivitaProgetto as ap ON p.id = ap.persona
WHERE p.posizione = 'Ricercatore'
GROUP BY p.id, p.nome, p.cognome;


/* Query 3
Quali sono le persone con stipendio di almeno 60000 euro
*/

SELECT p.nome, p.cognome, p.stipendio
FROM Persona AS p
WHERE p.stipendio >= 60000

/* Query 4
Qual è il budget totale dei progetti a cui lavora ogni
professore associato. Per ogni professore associato
restituire nome, cognome e budget totale dei progetti nei
quali è coinvolto
*/

SELECT p.nome, p.cognome, sum(pr.budget)
FROM Persona AS p
JOIN AttivitaProgetto as ap ON p.id = ap.persona
JOIN Progetto as pr ON ap.progetto = pr.id
WHERE p.posizione = 'Professore Associato'
GROUP BY p.id, p.nome, p.cognome;


/* Query 5
Qual è il numero totale di giorni di assenza per maternità
di ogni ricercatore. Per ogni ricercatore, restituire nume,
cognome e numero di giorni di assenza per maternità
*/

SELECT p.nome, p.cognome, count(a.giorno)
FROM Persona AS p
JOIN Assenza as a ON p.id = a.persona
WHERE p.posizione = 'Ricercatore'
AND a.tipo = 'Maternita'
GROUP BY p.id, p.nome, p.cognome;


/* Query 6
 Qual è il budget medio dei progetti nel db 
*/

SELECT avg(pr.budget)
FROM Progetto AS pr;


/* Query 7
Qual è il numero totale di ore, per ogni persona, dedicate
al progetto con id ‘3’. Per ogni persona che lavora al
progetto, restituire nome, cognome e numero di ore totali
dedicate ad attività progettuali relative al progetto 
*/

SELECT p.id, p.nome, p.cognome, avg(ap.oreDurata)
FROM Persona AS p
JOIN AttivitaProgetto as ap ON p.id = ap.persona
WHERE ap.progetto = 3
GROUP BY p.id, p.nome, p.cognome;

/* Query 8
Quali sono i professori ordinari che hanno svolto attività
nel WP di id ‘3’ del progetto con id ‘4’. Per ogni professore
ordinario, restituire il numero totale di ore svolte in
attività progettuali per il WP in questione
*/

SELECT p.id, p.nome, p.cognome, avg(ap.oreDurata)
FROM Persona AS p
JOIN AttivitaProgetto as ap ON p.id = ap.persona
JOIN WP as wp ON ap.wp = wp.id
WHERE ap.progetto = 3
AND ap.progetto = 4
AND p.posizione = 'Professore Ordinario'
GROUP BY p.id, p.nome, p.cognome;

/* Query 9
Quali sono i professori ordinari che lavorano ad almeno un
progetto e hanno uno stipendio di almeno 60000
*/

SELECT p.id, p.nome, p.cognome
FROM Persona AS p
JOIN AttivitaProgetto as ap ON p.id = ap.persona
WHERE p.posizione = 'Professore Ordinario'
AND p.stipendio >= 60000
GROUP BY p.id, p.nome, p.cognome;

/* Query 10
Qual è la durata media in ore delle attività didattiche
svolte da ogni persona. Per ogni persona che ha svolto
attività didattica, restituire nome, cognome e numero
medio di ore delle sue singole attività didattiche
*/

SELECT p.id, p.nome, p.cognome, avg(anp.oreDurata)
FROM Persona AS p
JOIN AttivitaNonProgettuale as anp ON p.id = anp.persona
WHERE anp.tipo = 'Didattica'
GROUP BY p.id, p.nome, p.cognome;
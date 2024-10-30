---QUERY 1

SELECT cognome
FROM Persona;

---QUERY 2

SELECT nome, cognome
FROM Persona
WHERE posizione = 'Ricercatore';

---QUERY 3

SELECT cognome
FROM Persona
WHERE posizione = 'Professore Associato'
AND cognome LIKE 'V%';

---QUERY 4

SELECT cognome
FROM Persona
WHERE (posizione = 'Professione Associato' OR posizione = 'Professore Ordinario')
AND cognome LIKE 'V%';
    
---QUERY 5

SELECT nome
FROM Progetto
WHERE fine < CURRENT_DATE;

---QUERY 6

SELECT nome
FROM Progetto
--WHERE TRUE (opzionale)
ORDER BY inizio ASC;

---QUERY 7

SELECT nome
FROM WP
--WHERE TRUE (opzionale)
ORDER BY nome ASC;

---QUERY 8

SELECT DISTINCT tipo
FROM Assenza;

---QUERY 9

SELECT DISTINCT tipo
FROM AttivitàProgetto;

--QUERY 10

SELECT DISTINCT giorno
FROM AttivitaNonProgettuale
WHERE tipo = 'Didattica'
ORDER BY giorno ASC;
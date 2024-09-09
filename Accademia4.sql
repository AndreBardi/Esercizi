---QUERY 1

SELECT cognome
FROM Persona

---QUERY 2

SELECT nome, cognome
FROM Persona
WHERE posizione = 'Ricercatore'

---QUERY 3

SELECT cognome
FROM Persona
WHERE posizione = 'Professore Associato'
AND cognome LIKE 'V%'

---QUERY 4

SELECT cognome
FROM Persona
WHERE (posizione = 'Professione Associato' OR posizione = 'Professore Ordinario')
AND cognome LIKE 'V%'
    
---QUERY 5

SELECT nome
FROM Progetto
WHERE fine < CURRENT_DATE
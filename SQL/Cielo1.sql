--QUERY 1
SELECT codice, comp
FROM Volo
WHERE durataMinuti > 180;

--QUERY 2

SELECT DISTINCT comp
FROM Volo
WHERE durataMinuti > 180;

--QUERY 3

SELECT codice, comp
FROM ArrPart
WHERE partenza = 'CIA';

--QUERY 4

SELECT DISTINCT comp	
FROM ArrPart
WHERE arrivo = 'FCO';

--QUERY 5

SELECT DISTINCT codice, comp	
FROM ArrPart
WHERE partenza = 'FCO' 
AND arrivo = 'JFK';

--QUERY 6

SELECT comp	
FROM ArrPart
WHERE partenza = 'FCO' 
AND arrivo = 'JFK';

--QUERY 7

SELECT DISTINCT comp	
FROM ArrPart as ARP, LuogoAeroporto as partenza, LuogoAeroporto as arrivo
WHERE partenza.citta = 'Roma' 
AND arrivo.citta = 'New York'
AND ARP.partenza = partenza.Aeroporto 
AND ARP.arrivo = arrivo.Aeroporto;


--QUERY 8

SELECT ar.codice as codiceIATA, ar.nome, L1.citta
FROM ArrPart as ARP, Aeroporto as ar, LuogoAeroporto as L1
WHERE ARP.comp  = 'MagicFly'
AND ar.codice = ARP.partenza
AND L1.aeroporto = ar.codice;

--QUERY 9

SELECT ARP.codice as codice_volo, ARP.comp as compagnia, ARP.partenza as partenza, ARP.arrivo as arrivo
FROM ArrPart as ARP, LuogoAeroporto as lpart, LuogoAeroporto as larr
WHERE ARP.partenza  = lpart.aeroporto
AND ARP.arrivo = larr.aeroporto
AND lpart.citta = 'Roma'
AND larr.citta = 'New York';

--QUERY 10

SELECT a1.comp as compagnia, 
		a1.codice as volo_1, 
		a2.codice as volo_2, 
		a1.partenza as partenza, 
		a1.arrivo as scalo, 
		a2.arrivo as arrivo
FROM ArrPart a1, ArrPart a2, LuogoAeroporto lpart, LuogoAeroporto larr
WHERE a1.arrivo = a2.partenza
AND a1.comp = a2.comp
AND a1.partenza = lpart.aeroporto
AND a2.arrivo = larr.aeroporto
AND lpart.citta = 'Roma'
AND larr.citta = 'New York'

--QUERY 11

SELECT DISTINCT comp.nome, comp.annoFondaz
FROM ArrPart as ARP
JOIN Compagnia comp on ARP.comp = comp.nome
WHERE ARP.partenza = 'FCO'
AND ARP.arrivo = 'JFK'
AND comp.annoFondaz IS NOT NULL
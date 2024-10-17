--query 3

SELECT la.nazione AS nazione, COUNT( distinct a.codice) AS num_aerop
FROM Volo v
JOIN ArrPart ap ON v.codice = ap.codice AND v.comp = ap.comp
JOIN Aeroporto a ON (a.codice = ap.arrivo OR a.codice = ap.partenza)
JOIN LuogoAeroporto la ON la.aeroporto = a.codice
WHERE v.comp = 'Apitalia'
GROUP BY la.nazione

--query 4
SELECT 
    avg(v.durataMinuti) as durata_media,
    min(v.durataMinuti) as durata_min,
    max(v.durataMinuti) as durata_max
from 
--query 6

SELECT lap.nazione AS nazione, COUNT(distinct laa.nazione)
FROM ArrPart ap, LuogoAeroporto lap, LuogoAeroporto laa
WHERE ap.partenza = lap.aeroporto
AND ap.arrivo = laa.aeroporto
AND lap.nazione <> laa.nazione 
GROUP BY lap.nazione;
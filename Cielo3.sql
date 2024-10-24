--query 1

SELECT v.comp as Compagnia, avg(v.durataMinuti) as durata_media
FROM Volo as v
JOIN ArrPart ap on v.codice = ap.codice and v.comp = ap.comp
JOIN Aeroporto a on ap.partenza = a.codice
JOIN LuogoAeroporto la on a.codice = la.aeroporto
WHERE la.nazione = 'Italy'
GROUP BY v.comp

--query 2

WITH durata_totale as (
    SELECT sum(v.durataMinuti) as som_dur , v.codice
    FROM Volo as v
    GROUP BY v.codice
    )

SELECT distinct v.comp, avg(v.durataMinuti)
FROM durata_totale as dt, Volo as v ,ArrPart as ap
WHERE v.codice = ap.codice
AND v.comp = ap.comp
GROUP BY v.comp
HAVING avg(dt.som_dur) < avg(v.durataMinuti)

--query 3



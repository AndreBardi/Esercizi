--query 1

SELECT v.comp AS Compagnia, avg(v.durataMinuti) AS durata_media
FROM Volo AS v
JOIN ArrPart ap ON v.codice = ap.codice AND v.comp = ap.comp
JOIN Aeroporto a ON ap.partenza = a.codice
JOIN LuogoAeroporto la ON a.codice = la.aeroporto
WHERE la.nazione = 'Italy'
GROUP BY v.comp

--query 2

WITH durata_totale AS (
    SELECT sum(v.durataMinuti) AS som_dur , v.codice
    FROM Volo AS v
    GROUP BY v.codice
    )

SELECT distinct v.comp, avg(v.durataMinuti)
FROM durata_totale AS dt, Volo AS v ,ArrPart AS ap
WHERE v.codice = ap.codice
AND v.comp = ap.comp
GROUP BY v.comp
HAVING avg(dt.som_dur) < avg(v.durataMinuti)

--query 3

WITH num_voli AS (
    SELECT la.citta, count(ap.arrivo) AS numero_arrivi
    FROM ArrPart AS ap, LuogoAeroporto AS la
    WHERE ap.arrivo = la.aeroporto 
    GROUP BY la.citta
),
media_voli AS (

    SELECT avg(num_voli.numero_arrivi) AS tot_arr
    FROM num_voli
)

SELECT nv.citta , nv.numero_arrivi
FROM num_voli AS nv, media_voli AS nm
WHERE nv.numero_arrivi > nm.tot_arr;

--query 4

WITH part_da_ita AS (
    SELECT ap.comp , avg(v.durataMinuti) AS pa_med
    FROM LuogoAeroporto AS la , ArrPart AS ap , Volo AS v
    WHERE la.aeroporto = ap.partenza
    AND v.codice = ap.codice
    AND la.nazione = 'Italy'
    GROUP BY ap.comp
),
media_tot AS ( 
    SELECT avg(v.durataMinuti) AS med_voli
    FROM LuogoAeroporto AS la , ArrPart AS ap , Volo AS v
    WHERE la.aeroporto = ap.partenza
    AND v.codice = ap.codice
    AND la.nazione = 'Italy'
    )
SELECT pa.comp , mt.med_voli
FROM part_da_ita AS pa , media_tot AS mt
WHERE pa.pa_med < mt.med_voli

--query 5

WITH media_voli AS (
SELECT la.citta , avg(v.durataMinuti) AS dur_med
FROM LuogoAeroporto AS la , Volo AS v , ArrPart AS ap
WHERE ap.codice = v.codice
AND ap.arrivo = la.aeroporto
GROUP BY la.citta
),
media_tot_voli AS (
SELECT v.durataMinuti AS sum_tot
FROM Volo AS v 
)
SELECT mv.citta , mv.dur_med
FROM media_voli AS mv ,media_tot_voli AS mtv , Volo AS v
GROUP BY mv.citta , mv.dur_med 
HAVING mv.dur_med > (avg(mtv.sum_tot) + STDDEV_SAMP(v.durataMinuti))
OR  mv.dur_med < (avg(mtv.sum_tot) - STDDEV_SAMP(v.durataMinuti))

--query6
WITH num_citta AS (
    SELECT nazione,aeroporto, count(citta) AS n_citta
    FROM LuogoAeroporto 
    GROUP BY nazione , aeroporto 
)
SELECT DISTINCT nc.nazione, nc.n_citta
FROM LuogoAeroporto AS la1 ,LuogoAeroporto AS la2,ArrPart AS ap,num_citta AS nc
WHERE ap.partenza = la1.aeroporto
AND la2.aeroporto = ap.arrivo
AND la1.nazione <> la2.nazione
AND la1.aeroporto <> la2.aeroporto
AND nc.aeroporto = ap.partenza
/* Query 1
Quali sono gli aeroporti raggiungibili

da dall’aeroporto ‘JFK’ 
 
tramite voli diretti e
indiretti?
*/

SELECT DISTINCT ap.arrivo as aereoporti
FROM ArrPart as ap 
WHERE ap.partenza = 'JFK'

UNION

SELECT DISTINCT ap.arrivo as aeroporti
FROM ArrPart as ap
WHERE ap.partenza IN (

    SELECT nest_ap.arrivo
    FROM ArrPart nest_ap
    WHERE nest_ap.partenza = 'JFK'
);

/*Query 2
Quali sono le citta’ raggiungibili con voli diretti e indiretti partendo
da Roma?
*/

SELECT DISTINCT la.citta as citta
FROM LuogoAeroporto as la 
WHERE la.citta = 'Roma'
AND la.aeroporto IN (
    SELECT ap.partenza
    FROM ArrPart as ap
)

UNION


SELECT DISTINCT la.citta as citta
FROM LuogoAeroporto as la 
WHERE la.aeroporto IN (
    SELECT nest_ap.arrivo
    FROM ArrPart as nest_ap
    WHERE nest_ap.partenza IN (
        SELECT nest_ap.partenza
        FROM ArrPart as nest_ap
        WHERE nest_ap.partenza IN (
            SELECT la.aeroporto
            FROM LuogoAeroporto as la 
            WHERE la.citta = 'Roma'
        )
    )

);

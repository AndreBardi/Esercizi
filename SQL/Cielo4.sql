/* Query 1
Quali sono i voli con durata maggiore 
della media di tutti i voli della stessa compagnia?
Restituire il codice del volo, 
la compagnia e la durata.
*/

SELECT v.codice, v.comp, v.durataMinuti
FROM Volo as v
WHERE v.durataMinuti > (
    select avg(nest_v.durataMinuti)
    from Volo as nest_v
    where nest_v.comp = v.comp
);


/* Query 2
Quali sono le città che hanno più di un aeroporto e dove 
almeno uno di questi ha in volo operato da 'Apitalia'?
*/


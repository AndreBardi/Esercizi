--query 1
select posizione, avg(stipendio) as media, stddev(stipendio) as dev_standard 
from persona 
group by posizione 
order by dev_standard asc;

--query 2
select * from persona as p
where p.posizione = 'Ricercatore' 
and stipendio >(
    select avg(stipendio) as stipendio 
    from persona 
    where posizione = 'Ricercatore');

--query 4
select * from (
    select p.id, nome, cognome, posizione, stipendio, sum(oredurata) as oreLavorate 
    from persona p
    inner join attivitaprogetto a on p.id = a.persona
    group by p.id, nome, cognome, posizione, stipendio 
    order by p.id asc ) r
    where r.oreLavorate > 20;


--query 5
with Durate_Progetti as (
    select id, nome, (fine - inizio) as durata
    from Progetto
),
Media_Durata as (
    select avg(durata) as media_durata
    from Durate_Progetti
)
select dp.nome, dp.durata
from Durate_Progetti dp
join Media_Durata md on dp.durata > md.media_durata;

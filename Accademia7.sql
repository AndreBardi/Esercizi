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
    

--query 3
with Stats as (
	select p.posizione, avg(p.stipendio) as media, stddev(p.stipendio) as dev_standard 
	from persona as p
	group by posizione 
	order by dev_standard asc
)
select p.posizione, count(*) as numero
from persona as p, Stats as s
where p.posizione = s.posizione
    and p.stipendio >= s.media - s.dev_standard
    and p.stipendio <= s.media + s.dev_standard
    group by p.posizione;


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

--query 6

select p.nome, SUM(ap.oreDurata) as totale_ore_dimostrazione
from Progetto p
join WP wp on p.id = wp.progetto
join AttivitaProgetto ap on wp.progetto = ap.progetto and wp.id = ap.wp
where p.fine = CURRENT_DATE
and ap.tipo = 'Dimostrazione'
group by p.nome;

--query 7

with AssenzeProfAssociati as (
    select p.id, p.nome, p.cognome, COUNT(*) AS numero_assenze
    from Assenza a
    join Persona p on a.persona = p.id
    where a.tipo = 'Malattia'
    and p.posizione = 'Professore Associato'
    group by p.id, p.nome, p.cognome
),
MediaAssenzeAssociati as (
    select AVG(numero_assenze) as media_assenze
    from AssenzeProfAssociati
),
AssenzeProfOrdinari AS (
    select p.id, p.nome, p.cognome, COUNT(*) as numero_assenze
    from Assenza a
    join Persona p on a.persona = p.id
    where a.tipo = 'Malattia'
    and p.posizione = 'Professore Ordinario'
    group by p.id, p.nome, p.cognome
)
select o.id, o.nome, o.cognome, o.numero_assenze
from AssenzeProfOrdinari o, MediaAssenzeAssociati m
where o.numero_assenze > m.media_assenze;
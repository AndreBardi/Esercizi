---QUERY 1

select WP.nome, WP.inizio, WP.fine
from Progetto,WP 
where Progetto.id = WP.progetto
and Progetto.nome = 'Pegasus';

---QUERY 2



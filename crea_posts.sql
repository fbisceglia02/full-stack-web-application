-- elimina la tabella se esiste
DROP TABLE IF EXISTS posts;

-- posts: promemoria
CREATE TABLE posts ( -- creata tabella
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- aggiungiamo un identificatore univoco
    titolo TEXT,
    info TEXT
);
-- è opportuno cancellare una tabella se esistente, prima di crearne un altra

-- inseriamo un promemoria
INSERT INTO posts (titolo, info) VALUES (
    'Lava il gatto',
    'Lucidare accuratamente il pelo e non dimenticare di spazzolare i denti'
);

INSERT INTO posts (titolo, info) VALUES (
    'Fare benzina',
    'Dopo lunghe e scrupolose analisi ho capito che la mia auto non cammina senza carburante'
);

INSERT INTO posts (titolo, info) VALUES (
    'Imparare urgentemente il portoghese',
    'Antes chorar num Mercedes, do que sorrir num ponto de onibus...'
);

-- Creation de la bdd
CREATE DATABASE sae_jv;

-- On se co a la bdd
\c sae_jv;

-- creation table des parties
CREATE TABLE parties (é
    id SERIAL PRIMARY KEY,
    date_partie TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    gagnant BOOLEAN DEFAULT FALSE
);

-- creation de la table pr les ptits bébou joueurs
CREATE TABLE joueurs (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(50) NOT NULL
);

-- creation de la table des joueurs dans chaque partie jouée
CREATE TABLE statistiques (
    id SERIAL PRIMARY KEY,
    partie_id INT REFERENCES parties(id) ON DELETE CASCADE,
    joueur_id INT REFERENCES joueurs(id) ON DELETE CASCADE,
    cases_decouvertes INT DEFAULT 0,
    manches_effectuees INT DEFAULT 0,
    morts INT DEFAULT 0,
    cles_recuperees INT DEFAULT 0,
    points_vie INT DEFAULT 100,
    boss_vaincus INT DEFAULT 0,
    score INT DEFAULT 0,
    pv_moyen DECIMAL
);

-- creation de la fonction qui calcule les ptits tchoupi-points
CREATE OR REPLACE FUNCTION calculer_score() RETURNS TRIGGER AS $$
BEGIN
    -- Calcule le tchoupiscore
    NEW.score := (NEW.cases_decouvertes * 1) + 
                 (NEW.cles_recuperees * 10) + 
                 (NEW.boss_vaincus * 15) + 
                 (CASE 
                      WHEN (SELECT gagnant FROM parties WHERE id = NEW.partie_id) THEN 200 
                      ELSE 0 
                  END);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- le trigger pour chaque maj des stats
CREATE TRIGGER trigger_calculer_score
BEFORE INSERT OR UPDATE ON statistiques
FOR EACH ROW
EXECUTE FUNCTION calculer_score();
# Pour mise en réseau
1. Selection du nombre de joueur (1(bot?) à 4)
2. premier tour:
    - selection du personnage (icon + nom) (actuellement on peut choisir plusieur fois le même)
    - lancé le dés
    - avance du nombre de case avec les fleches (pas de direction en sorti/debut de tableau/extrémité)

3. tour normal
    - attaqué (seulement si un joueur est sur un case voisin) (perdant ou fuyar élimné):
        joueur engagant l'attaque:
            - attack leger
            - forte
            - fuites(sortir)

    - lancé le dés
        - avance du nombre de case avec les fleches (pas de direction en sorti/debut de tableau/extrémité)

Case:
    - chance/malus : nécessite un click (dialogue et + bonus statistique en +)
    - Grr : tp aléatoir (0 action)
    - Pouff : tp la case opposé (Seulement 2 sur la map) (0 action)
    - blanc/départ : rien
    - mort : joueur éliminé n'est pu présent (premier mort == dernier, 2eme avant der)
    - puit : soit mort sois choix entre -200Pv et/ou utilisation de clef (si choix clef mais n'as pas, question reposé)
    - rejoue : reclick sur le dés puit bouge
    - spécialté : question fermer sur le choix d'utiliser ca clef (quite ou double)
    - boss : comme attaque mais avec un action de defense en plus (en cas clef)
    - hutte : click pour rantrer dans la maison, si 4 clef gagner sinon comme case blanches


Gain: 
    - 4 clef ou battre la sorciere


le serveur calcul tout
le client envoie les actions
session multi-joueur et solo
solo necessite d'être connecté au serveur
solo utilise l'IA pour les déplacements des joueurs
multi utilise l'IA uniquement pour les combats avec les bo


Idées de statistiques : nb parties, nb cases découvertes, nb de manche effectués, nb de morts dans la partie, score moyen par joueurs(de 1er a 4eme = nb morts, nb clés, nb pvs, nb cases découverte)
IA = prise en compte cases découverte + chercher clef + découvrir de nouvelle case + si condition rempli aller voir la sorciere
calcule du score:
- +1 par case découverte
- +10 par key
- +10 par boss vaincus (15 + la clef)
- +200 gagnée
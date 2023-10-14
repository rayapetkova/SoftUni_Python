CREATE OR REPLACE PROCEDURE sp_players_team_name(
    IN player_name VARCHAR(50),
    OUT team_name VARCHAR(45)
)
AS
$$
   DECLARE
           current_team VARCHAR(45);
           player_full_name VARCHAR(50);
   BEGIN
         SELECT
                CONCAT(first_name, ' ', last_name)
         FROM players
         INTO player_full_name;

         SELECT
                t.NAME
         FROM players AS "p"
         JOIN teams AS "t" ON t.id = p.team_id
         WHERE CONCAT(first_name, ' ', last_name) = player_name
         INTO current_team;

         IF current_team IS NULL THEN
            team_name:= 'The player currently has no team';
         ELSE
            team_name:= current_team;
         END IF;
   END;
$$
LANGUAGE plpgsql;
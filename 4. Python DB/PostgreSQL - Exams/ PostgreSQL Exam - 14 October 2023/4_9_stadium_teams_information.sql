CREATE OR REPLACE FUNCTION fn_stadium_team_name(
    stadium_name VARCHAR(30)
)
RETURNS TABLE(current_team VARCHAR)
AS
$$
   BEGIN
         RETURN QUERY
         SELECT
                t.NAME
         FROM teams AS "t"
         JOIN stadiums AS "s" ON s.id = t.stadium_id
         WHERE s.NAME = stadium_name
         ORDER BY t.NAME ASC;
   END;
$$
LANGUAGE plpgsql;
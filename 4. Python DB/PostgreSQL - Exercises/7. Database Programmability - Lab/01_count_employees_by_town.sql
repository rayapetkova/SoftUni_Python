CREATE OR REPLACE FUNCTION fn_count_employees_by_town(town_name VARCHAR(20))
RETURNS INT AS
$$
   DECLARE
   		   final_result INT;
   BEGIN
	   	SELECT
		       COUNT(*)
		FROM towns AS "t"
		JOIN addresses AS "a"
		 	 ON a.town_id = t.town_id
		JOIN employees AS "e"
		 	 ON e.address_id = a.address_id
		WHERE t.name = town_name
		GROUP BY t.name
		INTO final_result;
		RETURN final_result;
   END;
$$
LANGUAGE plpgsql;
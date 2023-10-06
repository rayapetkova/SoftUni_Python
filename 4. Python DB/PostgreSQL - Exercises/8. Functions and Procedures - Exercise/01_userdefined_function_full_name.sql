CREATE OR REPLACE FUNCTION fn_full_name(
	first_name VARCHAR,
	last_name VARCHAR
)
RETURNS VARCHAR
AS
$$
   DECLARE
   		final_result VARCHAR;
   BEGIN
   		 SELECT
		 		INITCAP(CONCAT(first_name, ' ', last_name))
		 INTO final_result;
		 RETURN final_result;
   END;
$$
LANGUAGE plpgsql;
CREATE OR REPLACE FUNCTION fn_courses_by_client(
	phone_num VARCHAR(20)
)
RETURNS INT
AS
$$
DECLARE
	    final_result INT;
BEGIN
   SELECT
   		  COUNT(cou.id)
   FROM
   		clients
   JOIN courses AS "cou"
   		ON clients.id = cou.client_id
   WHERE clients.phone_number = phone_num
   INTO final_result;

   RETURN final_result;
END;
$$
LANGUAGE plpgsql;
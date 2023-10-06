CREATE OR REPLACE FUNCTION fn_is_word_comprised(
	set_of_letters VARCHAR(50),
	word VARCHAR(50)
)
RETURNS BOOLEAN
AS
$$
   DECLARE
   		   final_result VARCHAR;
   BEGIN
   		 SELECT
		 	    TRIM(LOWER(set_of_letters) FROM LOWER(word))
		 INTO final_result;
		 RETURN LENGTH(final_result) = 0;
   END;
$$
LANGUAGE plpgsql;
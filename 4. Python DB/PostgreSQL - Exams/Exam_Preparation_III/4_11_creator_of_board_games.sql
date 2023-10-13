CREATE OR REPLACE FUNCTION fn_creator_with_board_games(
first_name_creator VARCHAR(30)
)
RETURNS INT
AS
$$
  DECLARE
  		  final_result INT;
  BEGIN
  		SELECT
			   COUNT(*)
		FROM creators_board_games
		WHERE creator_id = (SELECT id FROM creators WHERE first_name = first_name_creator)
		INTO final_result;

		RETURN final_result;
  END;
$$
LANGUAGE plpgsql;
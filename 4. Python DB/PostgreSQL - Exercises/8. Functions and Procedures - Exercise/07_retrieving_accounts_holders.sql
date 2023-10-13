CREATE OR REPLACE PROCEDURE sp_retrieving_holders_with_balance_higher_than(
	searched_balance NUMERIC
)
AS
$$
  DECLARE
  		  current_holder RECORD;
  BEGIN
  		FOR current_holder IN
			SELECT
				   CONCAT(ah.first_name, ' ', ah.last_name) AS "full_name",
				   SUM(accounts.balance) AS "total_sum"
			FROM account_holders AS "ah"
			JOIN accounts ON ah.id = accounts.account_holder_id
			GROUP BY ah.id
			ORDER BY full_name
		LOOP
			IF current_holder.total_sum > searched_balance THEN
				RAISE NOTICE '% - %', current_holder.full_name, current_holder.total_sum;
			END IF;
		END LOOP;
  END;
$$
LANGUAGE plpgsql;

CALL sp_retrieving_holders_with_balance_higher_than(200000);

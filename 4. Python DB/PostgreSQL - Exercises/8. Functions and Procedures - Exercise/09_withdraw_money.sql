CREATE OR REPLACE PROCEDURE sp_withdraw_money(
	account_id INT,
	money_amount NUMERIC(4)
)
AS
$$
   DECLARE
   		   account_balance NUMERIC;
   BEGIN
   		 SELECT balance
		 FROM accounts
		 WHERE id = account_id
		 INTO account_balance;

		 IF account_balance - money_amount >= 0 THEN
		 	UPDATE accounts
			SET balance = balance - money_amount
			WHERE id = account_id;

			COMMIT;
		 ELSE
		 	RAISE NOTICE 'Insufficient balance to withdraw %', account_balance;
		 END IF;
   END;
$$
LANGUAGE plpgsql;
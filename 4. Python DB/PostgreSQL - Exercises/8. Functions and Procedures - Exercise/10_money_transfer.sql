CREATE OR REPLACE PROCEDURE sp_transfer_money(
	sender_id INT,
	receiver_id INT,
	amount NUMERIC(4)
)
AS
$$
   BEGIN
   		 CALL sp_withdraw_money(sender_id, amount);
		 CALL sp_deposit_money(receiver_id, amount);

		 IF (SELECT balance FROM accounts WHERE id = sender_id) >= 0 THEN
		 	COMMIT;
		 ELSE
		 	ROLLBACK;
		 END IF;
   END;
$$
LANGUAGE plpgsql;
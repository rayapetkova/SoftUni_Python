CREATE OR REPLACE VIEW
		view_wizard_deposits_with_expiration_date_before_1983_08_17
AS SELECT
		  CONCAT(w.first_name, ' ', w.last_name) AS "Wizard Name",
		  w.deposit_start_date AS "Start Date",
		  w.deposit_expiration_date AS "Expiration Date",
		  w.deposit_amount AS "Amount"
FROM wizard_deposits AS w
GROUP BY "Wizard Name", "Start Date", "Expiration Date", "Amount"
HAVING w.deposit_expiration_date <= '1983-08-17'
ORDER BY "Expiration Date" ASC;
SELECT deposit_group,
SUM(deposit_interest) AS "Deposit Interest"
FROM wizard_deposits
GROUP BY deposit_group
ORDER BY SUM(deposit_interest) DESC;
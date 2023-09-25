SELECT
	   project_name,
	   CASE
	   		WHEN start_date IS NULL AND end_date IS NULL THEN 'Ready for development'
			WHEN start_date IS NOT NULL AND end_date IS NULL THEN 'In Progress'
			ELSE 'Done'
	   END
FROM projects
WHERE project_name LIKE '%Mountain%';
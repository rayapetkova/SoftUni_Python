CREATE VIEW view_river_info
AS SELECT
		  CONCAT('The river',
		      ' ', river_name,
		      ' ', 'flows into the',
		      ' ', outflow,
		      ' ', 'and is',
		      ' ', "length",
		      ' ', 'kilometers long.')
		  AS "River Information"
FROM rivers
ORDER BY river_name ASC;
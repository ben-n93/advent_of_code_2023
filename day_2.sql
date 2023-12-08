-- Table creation
CREATE TABLE day_2_puzzle_test (game INTEGER, blue_cubes INTEGER, red_cubes INTEGER, green_cubes INTEGER)

-- Part 1.
SELECT SUM(GAME) AS answer 
FROM 
(
SELECT 
DISTINCT GAME 
from
(
SELECT
game,
CASE WHEN blue_cubes <= 14 THEN 1 END AS BLUE,
CASE WHEN red_cubes <= 12 THEN 1 END AS RED, 
CASE WHEN green_cubes <= 13 THEN 1 END AS GREEN
FROM day_2_puzzle
)
GROUP BY 1 
HAVING SUM(BLUE + RED + GREEN) = 18
)

-- Part 2.
SELECT 
SUM(power_of_cubes) AS answer
FROM
(
SELECT  
game, 
max_blue * max_red * max_green AS power_of_cubes
FROM 
	(
	SELECT game,
	MAX(blue_cubes) AS max_blue,
	MAX(red_cubes) AS max_red,
	MAX(green_cubes) AS max_green
	FROM day_2_puzzle dp 
	GROUP BY 1 
	)
)
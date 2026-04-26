--Identifies roads with the most banks nearby within  .25 miles.

WITH banks AS (
    SELECT
        geom
    FROM
        pois
    WHERE
        fclass = 'bank'
)

SELECT
    rds.name AS road_name,
    rds.fclass AS road_type,
    COUNT(DISTINCT b.geom) AS nearby_bank_count,
    ST_Union(rds.geom) AS geom
FROM
    roads AS rds
JOIN
    banks AS b ON ST_DWithin(b.geom::geography, rds.geom::geography, 402)
WHERE
    rds.name IS NOT NULL
    AND rds.fclass IN ('motorway', 'trunk', 'primary')
GROUP BY
    rds.name,
    rds.fclass
HAVING
    COUNT(DISTINCT b.geom) > 1
ORDER BY
    nearby_bank_count DESC;
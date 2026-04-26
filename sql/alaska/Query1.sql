--Extracting Bank locations with name for spatial ditribution analysis


SELECT
    name,
    geom
FROM
    pois
WHERE
    fclass = 'bank';
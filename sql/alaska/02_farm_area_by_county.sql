--Taking the county level across Alaska and calculating the sq km of farm area for each

SELECT current_database();

SELECT f_table_name, type
FROM geometry_columns
ORDER BY f_table_name;

SELECT
    aa.name AS county_name,
    SUM(ST_Area(ST_Intersection(l.geom, aa.geom)::geography)) / 1000000 AS farmland_area_sq_km,
    aa.geom
FROM
    adminareas_a AS aa
JOIN
    landuse_a AS l
    ON ST_Intersects(aa.geom, l.geom)
WHERE
    aa.fclass = 'admin_level6'
    AND l.fclass = 'farmland'
    AND aa.name IS NOT NULL
GROUP BY
    aa.name, aa.geom
ORDER BY
    farmland_area_sq_km DESC;
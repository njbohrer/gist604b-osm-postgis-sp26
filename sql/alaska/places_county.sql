SELECT fclass, COUNT(*) AS count
FROM places_a
GROUP BY fclass
ORDER BY count DESC;
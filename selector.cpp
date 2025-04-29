/*
//Opening selector
SELECT h.h_id, h.h_title
FROM hymns h
LEFT JOIN (
    SELECT opening
    FROM history
    ORDER BY date DESC
    LIMIT 20
) AS recent ON h.h_id = recent.opening
WHERE h.position = 1 
  AND recent.opening IS NULL
ORDER BY RAND()
LIMIT 1;

// Sacrament selector
SELECT h.h_id, h.h_title
FROM hymns h
LEFT JOIN (
    SELECT sacraments
    FROM history
    ORDER BY date DESC
    LIMIT 20
) AS recent ON h.h_id = recent.sacraments
WHERE h.position = 2 
  AND recent.sacraments IS NULL
ORDER BY RAND()
LIMIT 1;

// Intermediate selector
SELECT h.h_id, h.h_title
FROM hymns h
LEFT JOIN (
    SELECT intermediate
    FROM history
    ORDER BY date DESC
    LIMIT 20
) AS recent ON h.h_id = recent.intermediate
WHERE h.position IS NULL 
  AND recent.intermediate IS NULL
ORDER BY RAND()
LIMIT 1;

// Closing selector
SELECT h.h_id, h.h_title
FROM hymns h
LEFT JOIN (
    SELECT intermediate
    FROM history
    ORDER BY date DESC
    LIMIT 20
) AS recent ON h.h_id = recent.intermediate
WHERE h.position IS NULL OR h.position = 4
  AND recent.intermediate IS NULL
ORDER BY RAND()
LIMIT 1;
*/
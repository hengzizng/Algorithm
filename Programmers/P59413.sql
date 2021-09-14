-- MySQL
WITH RECURSIVE HOUR_TABLE AS (
    SELECT 0 AS hour
     UNION ALL
    SELECT hour + 1 FROM HOUR_TABLE
     WHERE hour < 23
)
SELECT HOUR_TABLE.hour AS HOUR
     , IFNULL(OUT_HOUR.count, 0) AS COUNT
  FROM HOUR_TABLE
  LEFT OUTER JOIN (SELECT DATE_FORMAT(DATETIME, '%k') AS hour
                        , COUNT(DATE_FORMAT(DATETIME, '%k')) AS count
                     FROM ANIMAL_OUTS
                    GROUP BY DATE_FORMAT(DATETIME, '%k')) OUT_HOUR
               ON HOUR_TABLE.hour = OUT_HOUR.hour
 ORDER BY HOUR_TABLE.hour


 -- Oracle
 SELECT A.HOUR
     , NVL(B.COUNT, 0)
  FROM ( SELECT LEVEL-1 AS HOUR
           FROM DUAL
        CONNECT BY LEVEL <= 24
       ) A
  LEFT OUTER JOIN
       (SELECT TO_NUMBER(TO_CHAR(DATETIME, 'HH24')) AS DATETIME
             , COUNT(*)                             AS COUNT
          FROM ANIMAL_OUTS
         GROUP BY TO_CHAR(DATETIME, 'HH24')
         ORDER BY DATETIME
       ) B
    ON (A.HOUR = B.DATETIME)
 ORDER BY A.HOUR;
-- MySQL
SELECT I.ANIMAL_ID
     , I.NAME
  FROM ANIMAL_INS I
 INNER JOIN ANIMAL_OUTS O ON I.ANIMAL_ID = O.ANIMAL_ID
 ORDER BY O.DATETIME - I.DATETIME DESC
 LIMIT 2

-- Oracle
SELECT ANIMAL_ID
     , NAME
  FROM (
        SELECT O.ANIMAL_ID  AS ANIMAL_ID
             , O.NAME       AS NAME
          FROM ANIMAL_OUTS O
         INNER JOIN ANIMAL_INS I ON (O.ANIMAL_ID = I.ANIMAL_ID)
         ORDER BY O.DATETIME - I.DATETIME DESC
       )
 WHERE ROWNUM <= 2
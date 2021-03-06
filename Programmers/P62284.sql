-- MySQL
SELECT A.CART_ID
  FROM (
        SELECT CART_ID
          FROM CART_PRODUCTS
         WHERE NAME = 'Yogurt'
        ) A
 INNER JOIN (
             SELECT CART_ID
               FROM CART_PRODUCTS
              WHERE NAME = 'Milk'
            ) B ON A.CART_ID = B.CART_ID
 ORDER BY A.CART_ID


-- Oracle
SELECT DISTINCT CART_ID
  FROM CART_PRODUCTS
 WHERE NAME = '우유'
INTERSECT
SELECT DISTINCT CART_ID
  FROM CART_PRODUCTS
 WHERE NAME = '요거트'
 ORDER BY CART_ID;
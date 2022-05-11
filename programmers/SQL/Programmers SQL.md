# Programmers SQL



## 1. SELECT

- SELECT * FROM animal_ins ORDER BY animal_id;
- SELECT name, datetime FROM animal_ins ORDER BY animal_id DESC;
- SELECT animal_id, name FROM animal_ins WHERE intake_condition = 'Sick';
- SELECT animal_id, name FROM animal_ins WHERE intake_condition != 'Aged';
- SELECT animal_id, name FROM animal_ins ORDER BY animal_id;
- SELECT animal_id, name, datetime FROM animal_ins ORDER BY name ASC, datetime DESC;
- SELECT name FROM animal_ins ORDER BY datetime ASC LIMIT 1;



## 2. SUM, MAX, MIN

- SELECT datetime FROM animal_ins ORDER BY datetime DESC LIMIT 1;
- SELECT datetime FROM animal_ins ORDER BY datetime ASC LIMIT 1;
  SELECT MIN(datetime) FROM animal_ins;
- SELECT COUNT(*) FROM animal_ins;
- SELECT COUNT(DISTINCT name) FROM animal_ins WHERE name != 'NULL';
  SELECT COUNT(DISTINCT name) FROM animal_ins WHERE name IS NOT NULL;



## 3. IS NULL

- SELECT animal_id FROM animal_ins WHERE name IS NULL;

- SELECT animal_id FROM animal_ins  WHERE name IS NOT NULL ORDER BY animal_id ASC;

  => order by 가 where 보다 뒤에 와야한다.

- SELECT animal_type, IFNULL(name, 'No name') AS name, sex_upon_intake FROM animal_ins ORDER BY animal_id ASC;

  => IFNULL
  => IFNULL(A, B)
  => A가 NULL이면 B를, 그렇지 않다면 A를 반환



## 4. GROUP BY

- SELECT animal_type, count(animal_type) FROM animal_ins GROUP BY animal_type ORDER BY animal_type ASC;

- SELECT name, COUNT(name) 
  FROM animal_ins 
  GROUP BY name 
  HAVING COUNT(name) > 1 
  ORDER BY name;

  => GROUP BY에 조건을 걸기 위해서는 HAVING 을 사용한다.

- SELECT HOUR(datetime) AS HOUR, COUNT(datetime) AS COUNT
  FROM animal_outs
  WHERE HOUR(datetime) >= 9 AND HOUR(datetime) <= 19
  GROUP BY HOUR
  ORDER BY HOUR;

  => datetime 시간 양식에서 시간만 빼오기 위해 HOUR()함수 적용

  => WHERE을 이용해서 원하는 시간대만 가져옴(SELECT절의 조건에 해당)

- ```mysql
  SET @hour := -1; -- 변수 선언
  
  SELECT (@hour := @hour + 1) as HOUR,
  (SELECT COUNT(*) FROM ANIMAL_OUTS WHERE HOUR(DATETIME) = @hour) as COUNT
  FROM ANIMAL_OUTS
  WHERE @hour < 23
  ```

  => SET @변수를 이용해서 변수 선언

  => (@변수 := @변수 + 1) :=은 대입한다라는 의미

  => SELECT (SELECT COUNT(*) FROM) FROM 안에 또다른 SELECT문 작성
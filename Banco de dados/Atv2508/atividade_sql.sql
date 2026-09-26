-- =====================================================
-- Atividade SQL - Tabelas COUNTRY e CITY (baseado no
-- SQL Basics Cheat Sheet - LearnSQL.com)
-- Cada tabela populada com no mínimo 30 registros (ids)
-- =====================================================

DROP TABLE IF EXISTS city;
DROP TABLE IF EXISTS country;

CREATE TABLE country (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    population INTEGER,
    area INTEGER
);

CREATE TABLE city (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    country_id INTEGER,
    population INTEGER,
    rating INTEGER,
    FOREIGN KEY (country_id) REFERENCES country(id)
);

-- ---------------------------------------------------
-- POPULA COUNTRY (30 registros)
-- ---------------------------------------------------
INSERT INTO country (id, name, population, area) VALUES
(1,  'France', 68200000, 551695),
(2,  'Germany', 84300000, 357386),
(3,  'Iceland', 390000, 103000),
(4,  'Brazil', 216000000, 8515767),
(5,  'Portugal', 10400000, 92212),
(6,  'Spain', 48600000, 505990),
(7,  'Italy', 58900000, 301340),
(8,  'United Kingdom', 68300000, 243610),
(9,  'Netherlands', 17900000, 41850),
(10, 'Belgium', 11800000, 30528),
(11, 'Switzerland', 8800000, 41290),
(12, 'Austria', 9100000, 83879),
(13, 'Poland', 36700000, 312679),
(14, 'Sweden', 10600000, 450295),
(15, 'Norway', 5500000, 385207),
(16, 'Denmark', 5950000, 42933),
(17, 'Finland', 5600000, 338424),
(18, 'Greece', 10400000, 131957),
(19, 'Ireland', 5200000, 70273),
(20, 'Argentina', 46600000, 2780400),
(21, 'Chile', 19900000, 756102),
(22, 'Peru', 34400000, 1285216),
(23, 'Colombia', 52200000, 1141748),
(24, 'Mexico', 130200000, 1964375),
(25, 'Canada', 39500000, 9984670),
(26, 'United States', 336000000, 9833517),
(27, 'Japan', 123700000, 377975),
(28, 'South Korea', 51300000, 100210),
(29, 'China', 1409700000, 9596960),
(30, 'India', 1428600000, 3287263);

-- ---------------------------------------------------
-- POPULA CITY (30 registros, ligados a country_id)
-- ---------------------------------------------------
INSERT INTO city (id, name, country_id, population, rating) VALUES
(1,  'Paris', 1, 2145000, 4),
(2,  'Berlin', 2, 3677000, 4),
(3,  'Reykjavik', 3, 139000, 5),
(4,  'Sao Paulo', 4, 12330000, 5),
(5,  'Lisboa', 5, 567000, 4),
(6,  'Manaus', 4, 2260000, 3),
(7,  'Madrid', 6, 3334000, 5),
(8,  'Roma', 7, 2761000, 4),
(9,  'London', 8, 9002000, 4),
(10, 'Amsterdam', 9, 921000, 5),
(11, 'Brussels', 10, 1240000, 4),
(12, 'Zurich', 11, 447000, 4),
(13, 'Vienna', 12, 1985000, 4),
(14, 'Warsaw', 13, 1863000, 4),
(15, 'Stockholm', 14, 984000, 5),
(16, 'Oslo', 15, 717000, 3),
(17, 'Copenhagen', 16, 660000, 4),
(18, 'Helsinki', 17, 673000, 5),
(19, 'Athens', 18, 643000, 4),
(20, 'Dublin', 19, 592000, 5),
(21, 'Buenos Aires', 20, 3121000, 3),
(22, 'Santiago', 21, 6680000, 4),
(23, 'Lima', 22, 10150000, 3),
(24, 'Bogota', 23, 7743000, 4),
(25, 'Mexico City', 24, 9209000, 5),
(26, 'Toronto', 25, 3025000, 4),
(27, 'New York', 26, 8478000, 5),
(28, 'Tokyo', 27, 13960000, 5),
(29, 'Seoul', 28, 9509000, 4),
(30, 'Beijing', 29, 21893000, 4),
(31, 'Mumbai', 30, 20961000, 3),
(32, 'Rio de Janeiro', 4, 6775000, 4);

-- =====================================================
-- 5 COMANDOS ESCOLHIDOS DA LISTA DE SQL (cheat sheet)
-- =====================================================

-- 1) COMPARISON OPERATOR: cidades com rating acima de 3
SELECT name
FROM city
WHERE rating > 3;

-- 2) TEXT OPERATOR (LIKE): cidades que comecam com 'P' ou terminam com 's'
SELECT name
FROM city
WHERE name LIKE 'P%'
   OR name LIKE '%s';

-- 3) INNER JOIN: cidade + pais correspondente
SELECT city.name, country.name
FROM city
INNER JOIN country ON city.country_id = country.id;

-- 4) LEFT JOIN: todas as cidades, mesmo sem pais correspondente
SELECT city.name, country.name
FROM city
LEFT JOIN country ON city.country_id = country.id;

-- 5) ORDER BY: nomes de cidades ordenados pelo rating (decrescente)
SELECT name
FROM city
ORDER BY rating DESC;

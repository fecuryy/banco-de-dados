TRUNCATE TABLE usuarios RESTART IDENTITY;

CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(14) NOT NULL,
    idade INT NOT NULL
);

INSERT INTO usuarios (nome, cpf, idade)
SELECT
    'Usuario ' || i,
    LPAD((floor(random() * 99999999999))::text, 11, '0'),
    floor(random() * 63 + 18)::int
FROM generate_series(1, 30) AS i;

SELECT * FROM usuarios;

SELECT * FROM usuarios WHERE idade > 30;
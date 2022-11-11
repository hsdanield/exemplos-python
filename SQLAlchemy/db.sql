
CREATE DATABASE IF NOT EXISTS dev
    DEFAULT CHARACTER SET = 'utf8mb4';

USE dev;

CREATE TABLE IF NOT EXISTS livros (
    autor VARCHAR(50) NOT NULL,
    titulo VARCHAR(100) NOT NULL,
    genero VARCHAR(50) NOT NULL,
    ano INT NOT NULL,
    PRIMARY KEY(titulo)
);

INSERT INTO livros (autor, titulo, genero,ano)
VALUE ("Stephen Hawking", "Uma Breve História do Tempo", "Astronomia/Cosmologia", 2015);
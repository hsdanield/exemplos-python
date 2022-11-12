CREATE DATABASE IF NOT EXISTS dev;

USE dev;

CREATE TABLE
    IF NOT EXISTS estados (
        id_estado BIGINT NOT NULL AUTO_INCREMENT,
        codigo_ibge INT NOT NULL,
        sigla VARCHAR(2) NOT NULL,
        nome VARCHAR(50) NOT NULL,
        PRIMARY KEY(id_estado)
    );

CREATE TABLE
    IF NOT EXISTS cidades (
        id_cidade BIGINT AUTO_INCREMENT,
        nome VARCHAR(100) NOT NULL,
        id_estado BIGINT NOT NULL,
        PRIMARY KEY(id_cidade),
        FOREIGN KEY (id_estado) REFERENCES estados(id_estado)
    );

INSERT INTO
    estados (
        id_estado,
        codigo_ibge,
        sigla,
        nome
    )
VALUES ('1', '12', 'AC', 'Acre');

INSERT INTO
    estados (
        id_estado,
        codigo_ibge,
        sigla,
        nome
    )
VALUES ('2', '27', 'AL', 'Alagoas');

INSERT INTO
    estados (
        id_estado,
        codigo_ibge,
        sigla,
        nome
    )
VALUES ('3', '16', 'AP', 'Amapá');

INSERT INTO
    estados (
        id_estado,
        codigo_ibge,
        sigla,
        nome
    )
VALUES ('4', '13', 'AM', 'Amazonas');

INSERT INTO
    estados (
        id_estado,
        codigo_ibge,
        sigla,
        nome
    )
VALUES ('5', '29', 'BA', 'Bahia');

INSERT INTO
    estados (
        id_estado,
        codigo_ibge,
        sigla,
        nome
    )
VALUES ('6', '23', 'CE', 'Ceará');

INSERT INTO
    estados (
        id_estado,
        codigo_ibge,
        sigla,
        nome
    )
VALUES (
        '7',
        '53',
        'DF',
        'Distrito Federal'
    );

INSERT INTO
    estados (
        id_estado,
        codigo_ibge,
        sigla,
        nome
    )
VALUES (
        '8',
        '32',
        'ES',
        'Espírito Santo'
    );

INSERT INTO
    estados (
        id_estado,
        codigo_ibge,
        sigla,
        nome
    )
VALUES ('9', '52', 'GO', 'Goiás');

INSERT INTO
    estados (
        id_estado,
        codigo_ibge,
        sigla,
        nome
    )
VALUES ('10', '21', 'MA', 'Maranhão');

INSERT INTO
    estados (
        id_estado,
        codigo_ibge,
        sigla,
        nome
    )
VALUES ('11', '51', 'MT', 'Mato Grosso');

INSERT INTO
    estados (
        id_estado,
        codigo_ibge,
        sigla,
        nome
    )
VALUES (
        '12',
        '50',
        'MS',
        'Mato Grosso do Sul'
    );

INSERT INTO
    estados (
        id_estado,
        codigo_ibge,
        sigla,
        nome
    )
VALUES (
        '13',
        '31',
        'MG',
        'Minas Gerais'
    );

INSERT INTO
    estados (
        id_estado,
        codigo_ibge,
        sigla,
        nome
    )
VALUES ('14', '15', 'PA', 'Pará');

INSERT INTO
    estados (
        id_estado,
        codigo_ibge,
        sigla,
        nome
    )
VALUES ('15', '25', 'PB', 'Paraíba');

INSERT INTO
    estados (
        id_estado,
        codigo_ibge,
        sigla,
        nome
    )
VALUES ('16', '41', 'PR', 'Paraná');

INSERT INTO
    estados (
        id_estado,
        codigo_ibge,
        sigla,
        nome
    )
VALUES ('17', '26', 'PE', 'Pernambuco');

INSERT INTO
    estados (
        id_estado,
        codigo_ibge,
        sigla,
        nome
    )
VALUES ('18', '22', 'PI', 'Piauí');

INSERT INTO
    estados (
        id_estado,
        codigo_ibge,
        sigla,
        nome
    )
VALUES (
        '19',
        '33',
        'RJ',
        'Rio de Janeiro'
    );

INSERT INTO
    estados (
        id_estado,
        codigo_ibge,
        sigla,
        nome
    )
VALUES (
        '20',
        '24',
        'RN',
        'Rio Grande do Norte'
    );

INSERT INTO
    estados (
        id_estado,
        codigo_ibge,
        sigla,
        nome
    )
VALUES (
        '21',
        '43',
        'RS',
        'Rio Grande do Sul'
    );

INSERT INTO
    estados (
        id_estado,
        codigo_ibge,
        sigla,
        nome
    )
VALUES ('22', '11', 'RO', 'Rondônia');

INSERT INTO
    estados (
        id_estado,
        codigo_ibge,
        sigla,
        nome
    )
VALUES ('23', '14', 'RR', 'Roraima');

INSERT INTO
    estados (
        id_estado,
        codigo_ibge,
        sigla,
        nome
    )
VALUES (
        '24',
        '42',
        'SC',
        'Santa Catarina'
    );

INSERT INTO
    estados (
        id_estado,
        codigo_ibge,
        sigla,
        nome
    )
VALUES ('25', '35', 'SP', 'São Paulo');

INSERT INTO
    estados (
        id_estado,
        codigo_ibge,
        sigla,
        nome
    )
VALUES ('26', '28', 'SE', 'Sergipe');

INSERT INTO
    estados (
        id_estado,
        codigo_ibge,
        sigla,
        nome
    )
VALUES ('27', '17', 'TO', 'Tocantins');

INSERT INTO cidades (nome, id_estado) VALUES('Assis', 25);

INSERT INTO cidades (nome, id_estado) VALUES('São Paulo', 25);

INSERT INTO cidades (nome, id_estado) VALUES('Londrina', 16);

INSERT INTO cidades (nome, id_estado) VALUES('Nova Iguaçu', 19);

COMMIT;
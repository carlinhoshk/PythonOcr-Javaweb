CREATE TABLE pessoas (
    id VARCHAR(255) PRIMARY KEY NOT NULL,
    nome VARCHAR(255) NOT NULL UNIQUE,
    nascimento VARCHAR(255) NOT NULL
)
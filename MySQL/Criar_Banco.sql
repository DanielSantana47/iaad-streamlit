-- Tabela de Startups
CREATE TABLE Startup (
    ID_Startup INT PRIMARY KEY AUTO_INCREMENT,
    Nome_Startup VARCHAR(255) NOT NULL,
    Cidade_Sede VARCHAR(255) NOT NULL
) AUTO_INCREMENT = 10001;

-- Tabela de Programadores
CREATE TABLE Programador (
    ID_Programador INT PRIMARY KEY AUTO_INCREMENT,
    ID_Startup INT,  -- Chave estrangeira para Startup
    Nome_Programador VARCHAR(255) NOT NULL,
    Genero_Programador CHAR(1) NOT NULL,
    Data_Nasc_Programador DATE NOT NULL,
    FOREIGN KEY (ID_Startup) REFERENCES Startup(ID_Startup) ON DELETE SET NULL
) AUTO_INCREMENT = 30001;

-- Tabela de Dependentes dos Programadores
CREATE TABLE Dependente (
    ID_Dependente INT PRIMARY KEY AUTO_INCREMENT,
    ID_Responsavel INT,  -- Chave estrangeira para Programador
    Nome_Dependente VARCHAR(255) NOT NULL,
    Parentesco_Dependente VARCHAR(100) NOT NULL,
    Data_Nasc_Dependente DATE NOT NULL,
    FOREIGN KEY (ID_Responsavel) REFERENCES Programador(ID_Programador) ON DELETE CASCADE
);

-- Tabela de Linguagens de Programação
CREATE TABLE Linguagem (
    ID_Linguagem INT PRIMARY KEY AUTO_INCREMENT,
    Nome_Linguagem VARCHAR(100) NOT NULL
) AUTO_INCREMENT = 20001;

-- Tabela de relação entre Programadores e Linguagens
CREATE TABLE Programador_Linguagem (
    ID_Programador INT,
    ID_Linguagem INT,
    PRIMARY KEY (ID_Programador, ID_Linguagem),
    FOREIGN KEY (ID_Programador) REFERENCES Programador(ID_Programador) ON DELETE CASCADE,
    FOREIGN KEY (ID_Linguagem) REFERENCES Linguagem(ID_Linguagem) ON DELETE CASCADE
);

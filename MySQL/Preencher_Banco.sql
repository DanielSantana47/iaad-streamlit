INSERT INTO Startup (Nome_Startup, Cidade_Sede) VALUES
('Tech4Toy', 'Porto Alegre'),
('Smart123', 'Belo Horizonte'),
('knowledgeUp', 'Rio de Janeiro'),
('BSI Next Level', 'Recife'),
('QualiHealth', 'São Paulo'),
('ProEdu', 'Florianópolis'),
('CommerceIA', 'Manaus');

INSERT INTO Linguagem (Nome_Linguagem) VALUES
('Python'),
('PHP'),
('Java'),
('C'),
('JavaScript'),
('Dart'),
('SQL');

INSERT INTO Programador (ID_Startup, Nome_Programador, Genero_Programador, Data_Nasc_Programador) VALUES
(10001, 'João Pedro', 'M', '1993-06-23'),
(10002, 'Paula Silva', 'F', '1986-01-10'),
(10003, 'Renata Vieira', 'F', '1991-07-05'),
(10004, 'Felipe Santos', 'M', '1976-11-25'),
(10001, 'Ana Cristina', 'F', '1968-02-19'),
(10004, 'Fernando Alves', 'M', '1988-07-07'),
(10002, 'Laura Marques', 'F', '1987-10-04'),
(NULL, 'Lucas Lima', 'M', '2000-10-09'),
(NULL, 'Camila Macedo', 'F', '1995-07-03'),
(NULL, 'Leonardo Ramos', 'M', '2005-03-07'),
(10007, 'Alice Lins', 'F', '2000-10-09');

INSERT INTO Dependente (ID_Responsavel, Nome_Dependente, Parentesco_Dependente, Data_Nasc_Dependente) VALUES
(30001, 'André Sousa', 'Filho', '2020-05-15'),
(30002, 'Luciana Silva', 'Filha', '2018-07-26'),
(30002, 'Elisa Silva', 'Filha', '2020-01-06'),
(30002, 'Breno Silva', 'Esposo', '1984-05-21'),
(30004, 'Rafaela Santos', 'Esposa', '1980-02-12'),
(30004, 'Marcos Martins', 'Filho', '2008-03-26'),
(30006, 'Laís Meneses', 'Esposa', '1990-11-09'),
(30007, 'Daniel Marques', 'Filho', '2014-06-06'),
(30009, 'Lidiane Macedo', 'Filha', '2015-04-14');

INSERT INTO Programador_Linguagem (ID_Programador, ID_Linguagem) VALUES
(30001, 20001),  -- João Pedro sabe Python
(30001, 20002),  -- João Pedro sabe PHP
(30002, 20003),  -- Paula Silva sabe Java
(30003, 20004),  -- Renata Vieira sabe C
(30003, 20005),  -- Renata Vieira sabe JavaScript
(30004, 20005),  -- Felipe Santos sabe JavaScript
(30007, 20001),  -- Laura Marques sabe Python
(30007, 20002),  -- Laura Marques sabe PHP
(30009, 20004),  -- Camila Macedo sabe C
(30009, 20007),  -- Camila Macedo sabe SQL
(30010, 20007);  -- Leonardo Ramos sabe SQL


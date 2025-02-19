DELIMITER //

CREATE TRIGGER before_insert_programador
BEFORE INSERT ON Programador
FOR EACH ROW
BEGIN
    IF TIMESTAMPDIFF(YEAR, NEW.Data_Nasc_Programador, CURDATE()) < 18 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Erro: O programador deve ter pelo menos 18 anos.';
    END IF;
END;
//

CREATE TRIGGER before_update_programador
BEFORE UPDATE ON Programador
FOR EACH ROW
BEGIN
    IF TIMESTAMPDIFF(YEAR, NEW.Data_Nasc_Programador, CURDATE()) < 18 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Erro: O programador deve ter pelo menos 18 anos.';
    END IF;
END;
//

DELIMITER ;
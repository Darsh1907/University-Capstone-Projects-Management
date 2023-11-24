-- ----------------------------------

-- To create schema:
CREATE SCHEMA `capstones`;
use `capstones`;

-- ----------------------------------

-- 1. Student table:
-- Creation:
CREATE TABLE student (
  `Name` VARCHAR(20) NOT NULL,
  `SRN` VARCHAR(13) NOT NULL,
  `Sem` INT NOT NULL,
  `Gender` VARCHAR(1) NOT NULL CHECK (Gender IN ('M', 'F')),
  `CGPA` FLOAT NOT NULL,
  `Email` VARCHAR(45) NOT NULL,
  `project_id` INT NULL DEFAULT NULL,
  PRIMARY KEY (`SRN`),
  UNIQUE INDEX `Email_UNIQUE` (`Email` ASC) VISIBLE,
  UNIQUE INDEX `SRN_UNIQUE` (`SRN` ASC) VISIBLE);

-- -----------------------

-- 2. Evaluation table:
-- Creation:
CREATE TABLE evaluation (
  `Semester` INT NOT NULL,
  `SRN` VARCHAR(13) NOT NULL,
  `Faculty_ID` INT NOT NULL,
  `ISA1` FLOAT NULL DEFAULT NULL,
  `ISA2` FLOAT NULL DEFAULT NULL,
  `ISA3` FLOAT NULL DEFAULT NULL,
  `ESA` FLOAT NULL DEFAULT NULL,
  PRIMARY KEY (`Semester`, `SRN`),
  CONSTRAINT `srn_fk` FOREIGN KEY (`SRN`) REFERENCES `student` (`SRN`) ON DELETE CASCADE ON UPDATE CASCADE
);

-- ------------------

-- 3. Domain Table:
-- Creation:
CREATE TABLE domain (
  `DomainID` INT NOT NULL AUTO_INCREMENT,
  `Domain Name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`DomainID`),
  UNIQUE INDEX `Domain Name_UNIQUE` (`Domain Name` ASC) VISIBLE,
  UNIQUE INDEX `DomainID_UNIQUE` (`DomainID` ASC) VISIBLE);
-- Insertion:
INSERT INTO domain (`Domain Name`) VALUES ('Sample');
INSERT INTO domain (`Domain Name`) VALUES ('MIDS');
INSERT INTO domain (`Domain Name`) VALUES ('IOT');
INSERT INTO domain (`Domain Name`) VALUES ('Networks');
INSERT INTO domain (`Domain Name`) VALUES ('System and Core');
INSERT INTO domain (`Domain Name`) VALUES ('DBMS');
-- domain_backup Table:
CREATE TABLE domain_backup (
  `DomainID` INT NOT NULL AUTO_INCREMENT,
  `Domain Name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`DomainID`),
  UNIQUE INDEX `Domain Name_UNIQUE` (`Domain Name` ASC) VISIBLE,
  UNIQUE INDEX `DomainID_UNIQUE` (`DomainID` ASC) VISIBLE);
  
-- -----------------------------------------

-- 4. Faculty:
-- Creation:
CREATE TABLE faculty (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `email_id` VARCHAR(45) NOT NULL,
  `panel_id` INT NULL DEFAULT NULL,
  `domain_id` INT NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE INDEX `email_id_UNIQUE` (`email_id` ASC) VISIBLE,
	  CONSTRAINT `domain_fk` FOREIGN KEY (`domain_id`) REFERENCES `domain` (`DomainID`) ON DELETE CASCADE ON UPDATE CASCADE
);

-- ----------------------

-- 5. Panel:
-- Creation:
CREATE TABLE panel (
  `panel_id` INT NOT NULL AUTO_INCREMENT,
  `head_id` INT NOT NULL,
  `domain_id` INT NOT NULL,
  PRIMARY KEY (`panel_id`),
  UNIQUE INDEX `head_id_UNIQUE` (`head_id` ASC) VISIBLE,
  FOREIGN KEY (`domain_id`)
    REFERENCES domain (`DomainID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

-- -----------------------

-- 6. Team:
-- Creation:
CREATE TABLE team (
  `project_id` INT NOT NULL AUTO_INCREMENT,
  `faculty_id` INT NULL DEFAULT NULL,
  `is_approved` INT NOT NULL DEFAULT 0,
  `project_name` VARCHAR(45) NOT NULL,
  `panel_id` INT NULL DEFAULT NULL,
  `project_desc` VARCHAR(100) NOT NULL,
  `domain_id` INT NOT NULL,
  PRIMARY KEY (`project_id`),
  FOREIGN KEY (`domain_id`)
    REFERENCES domain (`DomainID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  FOREIGN KEY (`panel_id`)
    REFERENCES panel (`panel_ID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  UNIQUE INDEX `project_id_UNIQUE` (`project_id` ASC) VISIBLE
);

-- --------------------------

-- To add faculty ID foreign key in Evaluation table:
ALTER TABLE evaluation
ADD CONSTRAINT faculty_fk FOREIGN KEY (Faculty_ID) REFERENCES faculty(ID)
ON DELETE CASCADE ON UPDATE CASCADE;
-- To add panel id foreign key in Faculty table:
ALTER TABLE faculty
ADD CONSTRAINT panel_fk FOREIGN KEY (panel_id) REFERENCES panel(panel_id)
ON DELETE CASCADE ON UPDATE CASCADE;
-- To add Panel Head ID foreign key in Panel tabel:
ALTER TABLE panel
ADD CONSTRAINT faculty_head_fk FOREIGN KEY (head_id) REFERENCES faculty(ID)
ON DELETE CASCADE ON UPDATE CASCADE;
-- To add project_id constraint in Student Table
ALTER TABLE student
ADD CONSTRAINT `project_id_fk` FOREIGN KEY (`project_id`) REFERENCES `team` (`project_id`) 
ON DELETE CASCADE ON UPDATE CASCADE;

-- --------------------------------------------------------

-- Insertions in Faculty
INSERT INTO faculty (`Name`, `email_id`, `domain_id`) VALUES ('Sample', 'sample@gmail.com', 1);
INSERT INTO faculty (`Name`, `email_id`, `domain_id`) VALUES ('Sample2', 'sample2@gmail.com', 1);
INSERT INTO faculty (`Name`, `email_id`, `domain_id`) VALUES ('Nivedita Kasturi', 'nivedita@gmail.com', 6);
INSERT INTO faculty (`Name`, `email_id`, `domain_id`) VALUES ('Alpha', 'alpha@gmail.com', 2);
INSERT INTO faculty (`Name`, `email_id`, `domain_id`) VALUES ('Sheela Devi', 'sheela@gmail.com', 4);
INSERT INTO faculty (`Name`, `email_id`, `domain_id`) VALUES ('Sudeepa Roy Dey', 'sudeepa@gmail.com', 2);
INSERT INTO faculty (`Name`, `email_id`, `domain_id`) VALUES ('Geeta Dayalan', 'geeta_dayalan@gmail.com', 6);
INSERT INTO faculty (`Name`, `email_id`, `domain_id`) VALUES ('Arti Arya', 'arti@gmail.com', 2);
INSERT INTO faculty (`Name`, `email_id`, `domain_id`) VALUES ('Sandesh', 'sandesh@gmail.com', 2);
INSERT INTO faculty (`Name`, `email_id`, `domain_id`) VALUES ('Animesh Giri', 'animesh@gmail.com', 3);
-- Insertion in Students
INSERT INTO student (`Name`, `SRN`, `Sem`, `Gender`, `CGPA`, `Email`) VALUES ('Sample', 'pes2ug20cs000', 6, 'F', 9.99, 'sample@gmail.com');
INSERT INTO student (`Name`, `SRN`, `Sem`, `Gender`, `CGPA`, `Email`) VALUES ('Sample2', 'pes2ug20cs001', 6, 'F', 9.99, 'sample2@gmail.com');
INSERT INTO student (`Name`, `SRN`, `Sem`, `Gender`, `CGPA`, `Email`) VALUES ('Darsh', 'pes2ug21cs150', 5, 'M', 9.18, 'darshpatel@gmail.com');
INSERT INTO student (`Name`, `SRN`, `Sem`, `Gender`, `CGPA`, `Email`) VALUES ('Gautam', 'pes2ug21cs176', 5, 'M', 9, 'gautam@gmail.com');
INSERT INTO student (`Name`, `SRN`, `Sem`, `Gender`, `CGPA`, `Email`) VALUES ('Yashas', 'pes2ug21cs922', 5, 'M', 8.5, 'yashas@gmail.com');
INSERT INTO student (`Name`, `SRN`, `Sem`, `Gender`, `CGPA`, `Email`) VALUES ('Dhyey', 'pes2ug21cs164', 5, 'M', 7.9, 'dhyey@gmail.com');
INSERT INTO student (`Name`, `SRN`, `Sem`, `Gender`, `CGPA`, `Email`) VALUES ('Tirth', 'pes2ug21cs118', 5, 'M', 8.5, 'tirth@gmail.com');
INSERT INTO student (`Name`, `SRN`, `Sem`, `Gender`, `CGPA`, `Email`) VALUES ('Faizan', 'pes2ug21cs169', 5, 'M', 9.5, 'faizan@gmail.com');
INSERT INTO student (`Name`, `SRN`, `Sem`, `Gender`, `CGPA`, `Email`) VALUES ('Vansheel', 'pes2ug21cs909', 5, 'M', 8.57, 'vansheel@gmail.com');
INSERT INTO student (`Name`, `SRN`, `Sem`, `Gender`, `CGPA`, `Email`) VALUES ('Krisha', 'pes2ug21cs239', 5, 'M', 9.2, 'krisha@gmail.com');

-- --------------------------------------

-- Sample Panel formation
INSERT INTO panel (`domain_id`, `head_id`) VALUES (1, 1);
UPDATE faculty SET panel_id=1 WHERE ID in (1, 2);
-- Sample student team formation
INSERT INTO team (`project_name`, `project_desc`, `domain_id`) VALUES ('sample', 'sample sample', 1);
UPDATE student SET project_id = (SELECT COUNT(*) FROM team) WHERE SRN IN ('pes2ug20cs000', 'pes2ug20cs001');
-- Sample team approval
UPDATE team SET is_approved=1, faculty_id=1, panel_id=1 WHERE project_id=1;
-- Sample Evaluation
INSERT IGNORE INTO evaluation (`Semester`, `SRN`, `Faculty_ID`) 
VALUES (
	(SELECT Sem from student where SRN='pes2ug20cs000'),
	'pes2ug20cs000', 
	(SELECT faculty_id from team 
	where project_id=(SELECT project_id from student where SRN='pes2ug20cs000'))
);
UPDATE evaluation SET ISA1=20, ISA2=20, ISA3=20, ESA=80 WHERE SRN='pes2ug20cs000';

-- Stored Procedure to show all domains:
DELIMITER //
CREATE PROCEDURE get_all_domains()
BEGIN
    SELECT * FROM domain ORDER BY DomainID ASC;
END //
DELIMITER ;

-- Stored Procedure to show all students under a faculty
DELIMITER //
CREATE PROCEDURE find_students(in email varchar(45))
BEGIN
    SELECT SRN FROM student 
    WHERE project_id IN (SELECT project_id FROM team where faculty_id=(SELECT ID FROM faculty WHERE email_id=email));
END //
DELIMITER ;

-- Function to increase year by 1
SET SQL_SAFE_UPDATES = 0;
DELIMITER //
CREATE FUNCTION increase_year()
RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE rows_affected INT;
    -- Increase the Sem of every student by 1
    UPDATE student
    SET Sem = Sem + 1
    WHERE Sem <= 8; -- Update only if Sem is less than or equal to 8
    -- Remove entries with Sem greater than 8
    DELETE FROM student
    WHERE Sem > 8;
    -- Get the total number of rows affected
    SELECT ROW_COUNT() INTO rows_affected;
    RETURN rows_affected;
END //
DELIMITER ;

-- Trigger to add Domain data into domain_backup before deleting:
DELIMITER //
CREATE TRIGGER before_delete_domain
BEFORE DELETE
ON capstones.domain FOR EACH ROW
BEGIN
    -- Insert deleted data into domain_backup table
    INSERT INTO domain_backup (DomainID, `Domain Name`)
    VALUES (OLD.DomainID, OLD.`Domain Name`);
END;
//
DELIMITER ;


-- --------------------------------------------------------------
-- View Status of team for student
-- select Name, SRN, s.project_id, faculty_id, is_approved, project_name, panel_id, project_desc, domain_id 
-- from student as s, team as t 
-- where s.project_id = t.project_id AND s.SRN='pes2ug21cs118';

-- Delete project from student table
-- UPDATE `capstones`.`student` SET `project_id` = NULL WHERE (`SRN` = 'pes2ug21cs118');
-- UPDATE `capstones`.`student` SET `project_id` = NULL WHERE (`SRN` = 'pes2ug21cs150');
-- UPDATE `capstones`.`student` SET `project_id` = NULL WHERE (`SRN` = 'pes2ug21cs164');

-- Student viewing its panel
-- SELECT ID, name, email_id, d.`Domain Name` 
-- FROM faculty as f, domain as d 
-- WHERE panel_id=(SELECT panel_id FROM team where project_id=(SELECT project_id FROM student WHERE SRN='pes2ug20cs000')) AND d.DomainID=f.domain_id;

-- To find students under a teachers mentorship:
-- SELECT SRN FROM student 
-- WHERE project_id IN (SELECT project_id 
-- 						FROM team where faculty_id=(SELECT ID 
-- 													FROM faculty 
-- 													WHERE email_id='sample@gmail.com'))
-- ----------------------------------------------------------------

-- Create a new user for the student
CREATE USER 'capstone_student'@'%' IDENTIFIED BY 'studentstudent';
-- Grant permissions on the necessary tables and columns
GRANT SELECT ON capstones.student TO 'capstone_student'@'%';
GRANT SELECT, INSERT ON capstones.team TO 'capstone_student'@'%';
GRANT SELECT ON capstones.domain TO 'capstone_student'@'%';
GRANT SELECT ON capstones.faculty TO 'capstone_student'@'%';
GRANT SELECT ON capstones.panel TO 'capstone_student'@'%';
GRANT SELECT, INSERT, UPDATE ON capstones.evaluation TO 'capstone_student'@'%';
-- If there are additional columns used in the queries, grant permissions on those columns
GRANT SELECT (head_id) ON capstones.panel TO 'capstone_student'@'%';
GRANT SELECT, UPDATE (all_students_db) ON capstones.student TO 'capstone_student'@'%';
GRANT SELECT, INSERT (project_name, project_desc, domain_id) ON capstones.team TO 'capstone_student'@'%';
GRANT SELECT, UPDATE (faculty_id) ON capstones.team TO 'capstone_student'@'%';
GRANT SELECT (is_approved) ON capstones.student TO 'capstone_student'@'%';
GRANT SELECT (ID, name, email_id) ON capstones.faculty TO 'capstone_student'@'%';
GRANT SELECT (DomainID, `Domain Name`) ON capstones.domain TO 'capstone_student'@'%';
GRANT SELECT, INSERT (`Semester`, `SRN`, `Faculty_ID`) ON capstones.evaluation TO 'capstone_student'@'%';
-- Flush privileges to apply the changes
FLUSH PRIVILEGES;

-- Create a new user for the faculty
CREATE USER 'capstone_faculty'@'%' IDENTIFIED BY 'facultyfaculty';
-- Grant permissions on the necessary tables and columns
GRANT SELECT ON capstones.student TO 'capstone_faculty'@'%';
GRANT SELECT ON capstones.team TO 'capstone_faculty'@'%';
GRANT SELECT ON capstones.domain TO 'capstone_faculty'@'%';
GRANT SELECT ON capstones.faculty TO 'capstone_faculty'@'%';
GRANT SELECT ON capstones.panel TO 'capstone_faculty'@'%';
GRANT SELECT, INSERT, UPDATE ON capstones.evaluation TO 'capstone_faculty'@'%';
-- If there are additional columns used in the queries, grant permissions on those columns
GRANT SELECT (ID, name, email_id) ON capstones.faculty TO 'capstone_faculty'@'%';
GRANT SELECT (ID, name, email_id, domain_id) ON capstones.panel TO 'capstone_faculty'@'%';
GRANT SELECT (project_id, project_name, project_desc, domain_id) ON capstones.team TO 'capstone_faculty'@'%';
GRANT SELECT, UPDATE (project_id) ON capstones.student TO 'capstone_faculty'@'%';
GRANT SELECT (DomainID, `Domain Name`) ON capstones.domain TO 'capstone_faculty'@'%';
GRANT SELECT, INSERT (`Semester`, `SRN`, `Faculty_ID`) ON capstones.evaluation TO 'capstone_faculty'@'%';
-- Flush privileges to apply the changes
FLUSH PRIVILEGES;
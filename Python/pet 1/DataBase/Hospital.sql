
/* Drop Tables */

DROP TABLE IF EXISTS History;
DROP TABLE IF EXISTS PeopleDesease;
DROP TABLE IF EXISTS Desease;
DROP TABLE IF EXISTS Doctors;
DROP TABLE IF EXISTS People;




/* Create Tables */

CREATE TABLE Desease
(
	id_desease serial NOT NULL,
	desease_name varchar(50),
	dangerous int,
	symptoms varchar(50),
	durability varchar(50),
	PRIMARY KEY (id_desease)
) WITHOUT OIDS;


ALTER SEQUENCE Desease_id_desease_SEQ INCREMENT 1 MINVALUE 1 RESTART 1;


CREATE TABLE Doctors
(
	doctor_id serial NOT NULL,
	fio_doctor varchar(50),
	room varchar(5),
	specialization varchar(20),
	birthday_date_doctor date,
	PRIMARY KEY (doctor_id)
) WITHOUT OIDS;


ALTER SEQUENCE Doctors_doctor_id_SEQ INCREMENT 1 MINVALUE 1 RESTART 1;


CREATE TABLE History
(
	history_key serial NOT NULL,
	-- суррогатный ключ
	history_people_id int NOT NULL,
	-- суррогатный ключ
	history_doctor_id int NOT NULL,
	-- суррогатный ключ
	-- 
	history_id_desease int NOT NULL,
	status varchar(30),
	date_of_1_receipt date,
	date_of_2_receipt date,
	approintment varchar(100),
	PRIMARY KEY (history_key)
) WITHOUT OIDS;


CREATE TABLE People
(
	people_id serial NOT NULL,
	fio varchar(35),
	serial_of_police varchar(20),
	birthday_date_people date,
	people_id_desease serial,
	address varchar(50),
	phone varchar(20),
	PRIMARY KEY (people_id)
) WITHOUT OIDS;


ALTER SEQUENCE People_people_id_SEQ INCREMENT 1 MINVALUE 1 RESTART 1;


CREATE TABLE PeopleDesease
(
	peopledesease_people_id int NOT NULL,
	peopledesease_id_desease int NOT NULL
) WITHOUT OIDS;



/* Create Foreign Keys */

ALTER TABLE History
	ADD FOREIGN KEY (history_id_desease)
	REFERENCES Desease (id_desease)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE PeopleDesease
	ADD FOREIGN KEY (peopledesease_id_desease)
	REFERENCES Desease (id_desease)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE History
	ADD FOREIGN KEY (history_doctor_id)
	REFERENCES Doctors (doctor_id)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE History
	ADD FOREIGN KEY (history_people_id)
	REFERENCES People (people_id)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE PeopleDesease
	ADD FOREIGN KEY (peopledesease_people_id)
	REFERENCES People (people_id)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;



/* Comments */

COMMENT ON COLUMN History.history_people_id IS 'суррогатный ключ';
COMMENT ON COLUMN History.history_doctor_id IS 'суррогатный ключ';
COMMENT ON COLUMN History.history_id_desease IS 'суррогатный ключ
';




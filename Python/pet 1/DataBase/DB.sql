
/* Drop Tables */

DROP TABLE IF EXISTS equipment;
DROP TABLE IF EXISTS Firm;
DROP TABLE IF EXISTS Provider;
DROP TABLE IF EXISTS Seller;
DROP TABLE IF EXISTS type;




/* Create Tables */

CREATE TABLE equipment
(
	equipment_key int NOT NULL,
	name char(50),
	equipment_price float,
	equipment_size int,
	equipment_date date,
	equipment_country char(50),
	equipment_firm char(50),
	equipment_provider char(50),
	equipment_type char(50) NOT NULL,
	Firm char(50) NOT NULL,
	equipment_name char(50) NOT NULL,
	PRIMARY KEY (equipment_key)
) WITHOUT OIDS;


CREATE TABLE Firm
(
	Firm char(50) NOT NULL,
	Country char(50),
	Address char(50),
	Firm_name char(50),
	Site char(50),
	PRIMARY KEY (Firm)
) WITHOUT OIDS;


CREATE TABLE Provider
(
	Name char(50) NOT NULL,
	Country char(50),
	Address char(50),
	Provider_number char(50),
	PRIMARY KEY (Name)
) WITHOUT OIDS;


CREATE TABLE Seller
(
	Name char(50),
	Address char(50),
	Seller_number char(50),
	Experience int,
	Seller_type char(50),
	Type char(50) NOT NULL
) WITHOUT OIDS;


CREATE TABLE type
(
	Type char(50) NOT NULL,
	PRIMARY KEY (Type)
) WITHOUT OIDS;



/* Create Foreign Keys */

ALTER TABLE equipment
	ADD FOREIGN KEY (Firm)
	REFERENCES Firm (Firm)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE equipment
	ADD FOREIGN KEY (equipment_name)
	REFERENCES Provider (Name)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE equipment
	ADD FOREIGN KEY (equipment_type)
	REFERENCES type (Type)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE Seller
	ADD FOREIGN KEY (Type)
	REFERENCES type (Type)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;




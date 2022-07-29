
/* Drop Tables */

DROP TABLE IF EXISTS equipment;
DROP TABLE IF EXISTS equipment_type_seller;
DROP TABLE IF EXISTS equipment_type;
DROP TABLE IF EXISTS firm;
DROP TABLE IF EXISTS provider;
DROP TABLE IF EXISTS seller;




/* Create Tables */

CREATE TABLE equipment
(
	equipment_key serial NOT NULL,
	equiment_name varchar(50),
	equipment_price float,
	equipment_size int,
	equipment_date date,
	equipment_country varchar(50),
	-- Суррогатный ключ
	if_firm int NOT NULL,
	-- Суррогатный ключ
	id_provider int NOT NULL,
	-- суррогатный ключ
	id_equipment_type int NOT NULL,
	-- суррогатный ключ
	id_seller int NOT NULL,
	PRIMARY KEY (equipment_key)
) WITHOUT OIDS;


ALTER SEQUENCE equipment_equipment_key_SEQ INCREMENT 1 MINVALUE 0 RESTART 1;


CREATE TABLE equipment_type
(
	-- суррогатный ключ
	equipment_type_id serial NOT NULL,
	equipment_type_name varchar(50) NOT NULL,
	PRIMARY KEY (equipment_type_id)
) WITHOUT OIDS;


ALTER SEQUENCE equipment_type_equipment_type_id_SEQ INCREMENT 1 MINVALUE 0 RESTART 1;


CREATE TABLE equipment_type_seller
(
	-- суррогатный ключ
	equipment_type_id int NOT NULL,
	-- суррогатный ключ
	id_sellerss int NOT NULL
) WITHOUT OIDS;


CREATE TABLE firm
(
	-- Суррогатный ключ
	id_firm serial NOT NULL,
	firm_name varchar(50) NOT NULL,
	country varchar(50),
	address varchar(50),
	firm_number varchar(50),
	site varchar(50),
	PRIMARY KEY (id_firm)
) WITHOUT OIDS;


ALTER SEQUENCE firm_id_firm_SEQ INCREMENT 1 MINVALUE 0 RESTART 1;


CREATE TABLE provider
(
	-- Суррогатный ключ
	id_provider serial NOT NULL,
	provider_name varchar(50) NOT NULL,
	provider_country varchar(50),
	provider_address varchar(50),
	provider_number varchar(50),
	PRIMARY KEY (id_provider)
) WITHOUT OIDS;


ALTER SEQUENCE provider_id_provider_SEQ INCREMENT 1 MINVALUE 0 RESTART 0;


CREATE TABLE seller
(
	-- суррогатный ключ
	id_sellerss serial NOT NULL,
	name_seller varchar(50),
	seller_address varchar(50),
	seller_number varchar(50),
	experience int,
	seller_type varchar(50),
	PRIMARY KEY (id_sellerss)
) WITHOUT OIDS;


ALTER SEQUENCE seller_id_sellerss_SEQ INCREMENT 1 MINVALUE 0 RESTART 1;



/* Create Foreign Keys */

ALTER TABLE equipment
	ADD FOREIGN KEY (id_equipment_type)
	REFERENCES equipment_type (equipment_type_id)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE equipment_type_seller
	ADD FOREIGN KEY (equipment_type_id)
	REFERENCES equipment_type (equipment_type_id)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE equipment
	ADD FOREIGN KEY (if_firm)
	REFERENCES firm (id_firm)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE equipment
	ADD FOREIGN KEY (id_provider)
	REFERENCES provider (id_provider)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE equipment
	ADD FOREIGN KEY (id_seller)
	REFERENCES seller (id_sellerss)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE equipment_type_seller
	ADD FOREIGN KEY (id_sellerss)
	REFERENCES seller (id_sellerss)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;



/* Comments */

COMMENT ON COLUMN equipment.if_firm IS 'Суррогатный ключ';
COMMENT ON COLUMN equipment.id_provider IS 'Суррогатный ключ';
COMMENT ON COLUMN equipment.id_equipment_type IS 'суррогатный ключ';
COMMENT ON COLUMN equipment.id_seller IS 'суррогатный ключ';
COMMENT ON COLUMN equipment_type.equipment_type_id IS 'суррогатный ключ';
COMMENT ON COLUMN equipment_type_seller.equipment_type_id IS 'суррогатный ключ';
COMMENT ON COLUMN equipment_type_seller.id_sellerss IS 'суррогатный ключ';
COMMENT ON COLUMN firm.id_firm IS 'Суррогатный ключ';
COMMENT ON COLUMN provider.id_provider IS 'Суррогатный ключ';
COMMENT ON COLUMN seller.id_sellerss IS 'суррогатный ключ';




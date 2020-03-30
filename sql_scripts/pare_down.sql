--remove members not in target set
--hha_claimsk
CREATE TABLE temp AS
SELECT t1.* 
FROM hha_claimsk t1
INNER JOIN target_members t2
ON t1.dsysrtky = t2.dsysrtky;

DROP TABLE hha_claimsk;

ALTER TABLE temp
RENAME TO hha_claimsk;

--hha_revenuek
CREATE TABLE temp AS
SELECT t1.* 
FROM hha_revenuek t1
INNER JOIN target_members t2
ON t1.dsysrtky = t2.dsysrtky;

DROP TABLE hha_revenuek;

ALTER TABLE temp
RENAME TO hha_revenuek;

--car_claimsk
CREATE TABLE temp AS
SELECT t1.* 
FROM car_claimsk t1
INNER JOIN target_members t2
ON t1.dsysrtky = t2.dsysrtky;

DROP TABLE car_claimsk;

ALTER TABLE temp
RENAME TO car_claimsk;

--DELETE FROM car_linek WHERE dsysrtky NOT IN (SELECT dsysrtky FROM target_members);

--dme_claimsk
CREATE TABLE temp AS
SELECT t1.* 
FROM dme_claimsk t1
INNER JOIN target_members t2
ON t1.dsysrtky = t2.dsysrtky;

DROP TABLE dme_claimsk;

ALTER TABLE temp
RENAME TO dme_claimsk;

--dme_linek
CREATE TABLE temp AS
SELECT t1.* 
FROM dme_linek t1
INNER JOIN target_members t2
ON t1.dsysrtky = t2.dsysrtky;

DROP TABLE dme_linek;

ALTER TABLE temp
RENAME TO dme_linek;

--inp_claimsk
CREATE TABLE temp AS
SELECT t1.* 
FROM inp_claimsk t1
INNER JOIN target_members t2
ON t1.dsysrtky = t2.dsysrtky;

DROP TABLE inp_claimsk;

ALTER TABLE temp
RENAME TO inp_claimsk;

--inp_revenuek
CREATE TABLE temp AS
SELECT t1.* 
FROM inp_revenuek t1
INNER JOIN target_members t2
ON t1.dsysrtky = t2.dsysrtky;

DROP TABLE inp_revenuek;

ALTER TABLE temp
RENAME TO inp_revenuek;

--out_claimsk
CREATE TABLE temp AS
SELECT t1.* 
FROM out_claimsk t1
INNER JOIN target_members t2
ON t1.dsysrtky = t2.dsysrtky;

DROP TABLE out_claimsk;

ALTER TABLE temp
RENAME TO out_claimsk;
--DELETE FROM out_revenuek WHERE dsysrtky NOT IN (SELECT dsysrtky FROM target_members);

--snf_claimsk
CREATE TABLE temp AS
SELECT t1.* 
FROM snf_claimsk t1
INNER JOIN target_members t2
ON t1.dsysrtky = t2.dsysrtky;

DROP TABLE snf_claimsk;

ALTER TABLE temp
RENAME TO snf_claimsk;

--snk_revenuek
CREATE TABLE temp AS
SELECT t1.* 
FROM snf_revenuek t1
INNER JOIN target_members t2
ON t1.dsysrtky = t2.dsysrtky;

DROP TABLE snf_revenuek;

ALTER TABLE temp
RENAME TO snf_revenuek;
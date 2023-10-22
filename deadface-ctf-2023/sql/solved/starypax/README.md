# starypax

Starypax (street name STAR) is a controlled substance and is in high demand on the Dark Web. 
DEADFACE might leverage this database to find out which patients currently carry STAR.

How many patients in the Aurora database have an active prescription for Starypax as of Oct 20, 2023? 
And whose prescription expires first?

Submit the flag as flag{#_firstname lastname}.

Use the database dump from Aurora Compromise.

## Solution

loaded dump in mysql docker container

```sh
mysql -u root -p aurora < aurora.sql
```

```sql
USE AURORA;
SHOW TABLES;
```

```sql
select drug_id,drug_name from drugs order by drug_name;
-- 26 | Starypax

select count(*) from patients; -- 10391

select expiration from prescriptions limit 10;

select patients.first_name, patients.last_name, 
  prescriptions.expiration
from patients
join prescriptions on prescriptions.patient_id=patients.patient_id
  and prescriptions.expiration > '2023-10-20' -- 193
join drugs on drugs.drug_id=prescriptions.drug_id
  and drugs.drug_id='26'
order by prescriptions.expiration desc; 

/*
+------------+-----------+------------+
| first_name | last_name | expiration |
+------------+-----------+------------+
| Lenci      | Springett | 2023-12-19 |
| Appolonia  | Benda     | 2023-11-26 |
| Chic       | Abrashkov | 2023-11-20 |
| Rodi       | Godfery   | 2023-11-04 |
| Eolanda    | Maciaszek | 2023-10-31 |
| Chrissie   | Hargraves | 2023-10-28 |
| Renae      | Allum     | 2023-10-26 |
+------------+-----------+------------+
7 rows in set (0.00 sec)
*/
```

`flag{7_Renae Allum}`

# High Tower

We need your help tracking down `d34th`, the leader of DEADFACE. He recently conducted an attack against SkyWave Telecommunications. 
We’ve received cell tower data that might help us pinpoint `d34th`’s device and potentially lead us to his identity.

But first, we need to assess your familiarity with SQL and the data you’re being provided.

What is the tower_id of the cell tower that sits at an approximate elevation of 220 ft?

Submit the flag as `flag{tower_id}`. Example: flag{10}.

Access the database via SSH at skywave.deadface.io.
Username: skywave
Password: d34df4c3

## Solution

```sh
ssh skywave@skywave.deadface.io
```

```txt
-- MySQL CLI

SHOW DATABASES;
-- cell_tower_db

SHOW TABLES;

SHOW COLUMNS FROM Towers;
+-----------------------+---------------------------------+------+-----+---------+----------------+
| Field                 | Type                            | Null | Key | Default | Extra          |
+-----------------------+---------------------------------+------+-----+---------+----------------+
| tower_id              | int(11)                         | NO   | PRI | NULL    | auto_increment |
| location_name         | varchar(255)                    | NO   |     | NULL    |                |
| latitude              | decimal(9,6)                    | NO   |     | NULL    |                |
| longitude             | decimal(9,6)                    | NO   |     | NULL    |                |
| elevation             | decimal(5,2)                    | YES  |     | NULL    |                |
| tower_height          | decimal(5,2)                    | YES  |     | NULL    |                |
| operator_id           | int(11)                         | YES  | MUL | NULL    |                |
| status                | enum('active','decommissioned') | YES  |     | active  |                |
| install_date          | date                            | YES  |     | NULL    |                |
| last_maintenance_date | date                            | YES  |     | NULL    |                |
+-----------------------+---------------------------------+------+-----+---------+----------------+

select tower_id, elevation from Towers
where elevation > 200;
-- 215, 220.32
```

`flag{215}`


# Updates

How many towers received software updates?

Submit the flag as flag{number}. Example: flag{10}.

## Solution

```sh
ssh skywave@skywave.deadface.io
```

```sql
SHOW COLUMNS FROM Towers;

select count(*) from Towers
where install_date=last_maintenance_date;

SHOW TABLES;

SHOW COLUMNS FROM Tower_Maintenance;
/*
+------------------+--------------+------+-----+---------+----------------+
| Field            | Type         | Null | Key | Default | Extra          |
+------------------+--------------+------+-----+---------+----------------+
| maintenance_id   | int(11)      | NO   | PRI | NULL    | auto_increment |
| tower_id         | int(11)      | YES  | MUL | NULL    |                |
| maintenance_type | varchar(255) | YES  |     | NULL    |                |
| maintenance_date | date         | NO   |     | NULL    |                |
| technician_id    | int(11)      | YES  | MUL | NULL    |                |
+------------------+--------------+------+-----+---------+----------------+
*/

select count(*), maintenance_type
from Tower_Maintenance
group by maintenance_type; 
-- 96 | Software updates

select count(distinct tower_id)
from Tower_Maintenance
where maintenance_type='Software updates';
-- 70
```

`flag{70}`

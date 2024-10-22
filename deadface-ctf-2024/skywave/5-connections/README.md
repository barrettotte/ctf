# 5-Connections

We’re running with an assumption that d34th drove around and connected to various cell towers the day leading up to the attack.

We need you to determine which device IMEI connected to the most unique towers on September 7 from 16:10 to 18:54.

Submit the flag as flag{device_imei}. Example: flag{123456789012345}.

## Solutions

Access the database via SSH at skywave.deadface.io.
Username: skywave
Password: d34df4c3

```sql
/*
+---------------------+--------------+------+-----+-------------------+----------------+
| Field               | Type         | Null | Key | Default           | Extra          |
+---------------------+--------------+------+-----+-------------------+----------------+
| connection_id       | int(11)      | NO   | PRI | NULL              | auto_increment |
| device_id           | int(11)      | YES  | MUL | NULL              |                |
| tower_id            | int(11)      | YES  | MUL | NULL              |                |
| sector_id           | int(11)      | YES  | MUL | NULL              |                |
| connection_time     | timestamp    | NO   |     | CURRENT_TIMESTAMP |                |
| signal_strength     | decimal(5,2) | YES  |     | NULL              |                |
| connection_duration | int(11)      | YES  |     | NULL              |                |
+---------------------+--------------+------+-----+-------------------+----------------+
*/

select device_id, tower_id
from Connections
where connection_time between '2024-09-07 16:10:00' AND '2024-09-07 18:54:00'
order by device_id desc
;

select count(tower_id), device_id
from Connections
where connection_time between '2024-09-07 16:10:00' AND '2024-09-07 18:54:00'
group by device_id
having count(tower_id) > 1
order by count(tower_id) desc
;

-- |               5 |      2279 |
-- |               5 |      2325 |

select * from Devices
where device_id in (2279,2325);

select * from Devices where device_id=2207;
-- 525524944410322
```

`flag{525524944410322}`

`flag{643366592089524}`
`flag{377494868035375}`

# Rabbit Ears

Florian Olyff operates several towers. 
What is the most commonly used antenna type on the towers she manages?

Submit the flag as flag{antenna_type number}. Example: flag{Long Antenna 5}.

## Solution

```sql
select * from Antennas;
-- +------------+---------------------------------------+
-- | antenna_id | antenna_name                          |
-- +------------+---------------------------------------+
-- |          1 | Omnidirectional                       |
-- |          2 | Directional                           |
-- |          3 | Panel                                 |
-- |          4 | Log-Periodic                          |
-- |          5 | Parabolic                             |
-- |          6 | Small Cell                            |
-- |          7 | Use Case                              |
-- |          8 | Distributed Antenna System (DAS)      |
-- |          9 | Multiple Input Multiple Output (MIMO) |
-- +------------+---------------------------------------+

SHOW TABLES;
-- +-------------------------+
-- | Tables_in_cell_tower_db |
-- +-------------------------+
-- | Antennas                |
-- | Carriers                |
-- | Connections             |
-- | Device_Types            |
-- | Devices                 |
-- | Operators               |
-- | Technicians             |
-- | Tower_Maintenance       |
-- | Tower_Sectors           |
-- | Towers                  |
-- +-------------------------+

select count(*), maintenance_type
from Tower_Maintenance
group by maintenance_type; 


select * from Operators where last_name='Olyff';
-- +-------------+------------+-----------+-----------------+
-- | operator_id | first_name | last_name | employee_number |
-- +-------------+------------+-----------+-----------------+
-- |           4 | Florian    | Olyff     | 3223634520      |
-- +-------------+------------+-----------+-----------------+

select * from Towers
where operator_id='4';

show columns from Tower_Sectors;
-- +----------------+--------------+------+-----+---------+----------------+
-- | Field          | Type         | Null | Key | Default | Extra          |
-- +----------------+--------------+------+-----+---------+----------------+
-- | sector_id      | int(11)      | NO   | PRI | NULL    | auto_increment |
-- | tower_id       | int(11)      | YES  | MUL | NULL    |                |
-- | azimuth        | decimal(5,2) | NO   |     | NULL    |                |
-- | antenna_id     | int(11)      | YES  | MUL | NULL    |                |
-- | frequency_band | varchar(50)  | YES  |     | NULL    |                |
-- | power_output   | decimal(5,2) | YES  |     | NULL    |                |
-- +----------------+--------------+------+-----+---------+----------------+

select count(*), a.antenna_name
from Towers t
join Tower_Sectors s on t.tower_id=s.tower_id
join Antennas a on s.antenna_id=a.antenna_id
where t.operator_id='4'
group by antenna_name
order by count(*);

-- flag{antenna_type number}
-- flag{MIMO 3}
-- flag{Multiple Input Multiple Output (MIMO) 3}
```

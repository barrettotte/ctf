# Trifecta

We can assume that d34th used some kind of smart device or computer to conduct his attacks. 
How many devices in the database are either a smart phone, a computer, or a tablet?

Submit the flag as flag{number}. Example: flag{10}.

## Solution

```sql
show columns from Devices;
/*
+----------------+--------------+------+-----+---------+----------------+
| Field          | Type         | Null | Key | Default | Extra          |
+----------------+--------------+------+-----+---------+----------------+
| device_id      | int(11)      | NO   | PRI | NULL    | auto_increment |
| device_imei    | varchar(15)  | NO   | UNI | NULL    |                |
| device_type_id | int(11)      | YES  | MUL | NULL    |                |
| manufacturer   | varchar(100) | YES  |     | NULL    |                |
| model          | varchar(100) | YES  |     | NULL    |                |
| carrier_id     | int(11)      | YES  | MUL | NULL    |                |
+----------------+--------------+------+-----+---------+----------------+
*/

show columns from Device_Types;
/*
+------------------+--------------+------+-----+---------+----------------+
| Field            | Type         | Null | Key | Default | Extra          |
+------------------+--------------+------+-----+---------+----------------+
| device_type_id   | int(11)      | NO   | PRI | NULL    | auto_increment |
| device_type_name | varchar(100) | NO   |     | NULL    |                |
+------------------+--------------+------+-----+---------+----------------+
*/

select * from Device_Types order by device_type_name;
/*
+----------------+---------------------------+
| device_type_id | device_type_name          |
+----------------+---------------------------+
|              4 | computer                  |
|              7 | gps fleet tracking device |
|              8 | health monitoring device  |
|              5 | iot                       |
|              2 | mobile phone              |
|              6 | modem                     |
|              9 | point of sale             |
|              1 | smartphone                |
|              3 | tablet                    |
|             10 | vehicle                   |
+----------------+---------------------------+
*/
-- smart phone, a computer, or a tablet
select count(*)
from Devices
where device_type_id in ('4', '3', '1');
-- 714

```

`flag{714}`
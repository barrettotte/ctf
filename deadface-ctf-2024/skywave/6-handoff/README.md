# 6-Handoff

Which devices switched between towers within a 5 to 10 minute timespan? 
Submit the number of connections and the IMEI of the device with the earliest connection time.

Submit the flag as flag{number_IMEI}. Example: flag{100_123456789012345}.

## Solution

```sql
select c1.device_id, c1.tower_id as from_tower, c2.tower_id as to_tower,
  c1.connection_time as from_time, c2.connection_time as to_time,
  timestampdiff(minute, c1.connection_time, c2.connection_time) as timespan_mins
from Connections c1
join Connections c2 on c1.device_id=c2.device_id
  and c1.tower_id != c2.tower_id
where timestampdiff(minute, c1.connection_time, c2.connection_time) between 5 and 10
order by c1.connection_time;

-- |      1680 |         75 |       42 | 2024-09-07 10:10:36 | 2024-09-07 10:16:48 |             6 |

select * from Devices where device_id=1680;
select * from Devices where device_id=1800;

select count(*) from Connections where device_id=1800; -- 3

select * from Devices where device_id=74; -- 675518945697602
select count(*) from Connections where device_id=74; -- 3
```

`flag{917631023473168}`
`flag{10_042813788700728}`
`flag{1_042813788700728}`
`flag{3_042813788700728}`

`flag{3_675518945697602}`

`flag{17_042813788700728}`

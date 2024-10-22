# Longest Run

We need to determine which device had the longest running connection out of the towers with the following coordinates:

    (41.639642, -79.220682)
    (40.598271, -78.801089)
    (41.045892, -79.068358)
    (41.257279, -77.529468)

Additionally, let’s focus on only finding the longest running connection with a dBm greater than -100.

Submit the flag as flag{device_imei}. Example: flag{123456789012345}.

## Solution

```sql
select *
from Towers
where (latitude=41.639642 and longitude=-79.220682) or
  (latitude=40.598271 and longitude=-78.801089) or
  (latitude=41.045892 and longitude=-79.068358) or
  (latitude=41.257279 and longitude=-77.529468)
;
-- 105,123,187,200

select *
from Connections
where signal_strength > -100
  and tower_id in (105,123,187,200)
  order by connection_duration desc
  limit 1;
-- +---------------+-----------+----------+-----------+---------------------+-----------------+---------------------+
-- | connection_id | device_id | tower_id | sector_id | connection_time     | signal_strength | connection_duration |
-- +---------------+-----------+----------+-----------+---------------------+-----------------+---------------------+
-- |          5169 |       344 |      200 |      1211 | 2024-09-07 19:06:39 |          -89.43 |               85709 |
-- +---------------+-----------+----------+-----------+---------------------+-----------------+---------------------+

select * from Devices
where device_id=344;
-- 845303290931675
```

`flag{845303290931675}`

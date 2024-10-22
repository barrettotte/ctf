# 8 - Phone of Death

We’re close to pinpointing d34th’s device! We’re confident that d34th is among those devices with at least 2 connections to various towers between 15:00 and 19:00 on September 7th.

What is the manufacturer and model of d34th’s phone? Provide the SHA1 of the concatenated IMEI, manufacturer, and model of d34th’s phone.

Submit the flag as flag{sha1 hash}.

## Solution

```sql
select device_id, tower_id, connection_time
from Connections
where connection_time between '2024-09-07 15:00:00' and '2024-09-07 19:00:00'
order by device_id,connection_time;

select count(*), device_id
from Connections
where connection_time between '2024-09-07 15:00:00' and '2024-09-07 19:00:00'
group by device_id
having count(*) > 1;

select count(*),model from Devices group by model;
-- |       10 | Synthesis 8    |


select c.device_id, c.tower_id, c.connection_time
from Connections c
join Devices d on c.device_id=d.device_id
  and d.model='Synthesis 8'
where c.connection_time between '2024-09-07 15:00:00' and '2024-09-07 19:00:00'
order by c.device_id, c.connection_time;
-- 2099

-- https://ghosttown.deadface.io/t/just-got-my-synthesis-8/63

select * from Devices where device_id=2099;
-- +-----------+-----------------+----------------+--------------+-------------+------------+
-- | device_id | device_imei     | device_type_id | manufacturer | model       | carrier_id |
-- +-----------+-----------------+----------------+--------------+-------------+------------+
-- |      2099 | 548884492651613 |              1 | Syntheta     | Synthesis 8 |          4 |
-- +-----------+-----------------+----------------+--------------+-------------+------------+


select sha1(concat(concat(device_imei, manufacturer), model))
from Devices
where device_id=2099;
-- a0673fc386f438b907a2a6b14b397e679fa9254f

select sha1('548884492651613SynthetaSynthesis 8');
-- a0673fc386f438b907a2a6b14b397e679fa9254f

select sha1('548884492651613SynthetaSynthesis8');
```

`flag{f16342613727bb7444de33de7ca8efe9be75909f}`


`flag{a0673fc386f438b907a2a6b14b397e679fa9254f}`
retry this before ending (last attempt)

# clean-up-on-aisle-5

Based on Ghost Town conversations, DEADFACE is going to try to compromise an Aurora Health pharmacy to get their hands on STAR. 
Turbo Tactical wants to provide security personnel at Aurora with information about which facility, aisle, and bin contains 
the most STAR, since it is likely what DEADFACE will target.

Provide the facility_id, aisle, and bin where the most STAR is kept in the city DEADFACE is targeting. 
Submit the flag as flag{facility_id-aisle-bin}.

Example: flag{123-4-8}

Use the database dump from Aurora Compromise.

## Solution

```sql
select drug_name from drugs where drug_id=26; -- Starypax

select locator from inventory order by locator limit 10;

select locator, 
  substring(locator, locate('A', locator) + 1, locate('B', locator) - locate('A', locator) - 1) as aisle,
  substring(locator, locate('B', locator) + 1) as bin
from inventory
order by locator
limit 10;

select i.qty, f.facility_id, i.locator
from inventory as i
join facilities as f on f.facility_id=i.facility_id
where i.drug_id=26
order by i.qty desc
limit 10;

-- in the city DEADFACE is targeting
select facility_id, city, state 
from facilities
order by facility_id
limit 25;

-- where are they targeting...

select i.qty, f.facility_id, i.locator,
  f.city, f.state
from inventory as i
join facilities as f on f.facility_id=i.facility_id
where i.drug_id=26
order by i.qty desc
limit 25;

select distinct(state)
from facilities; -- can't guess...
-- 

-- https://ghosttown.deadface.io/t/get-after-those-northern-lights/103/7
-- Pheonix

select i.qty, f.facility_id, i.locator,
  f.city, f.state
from inventory as i
join facilities as f on f.facility_id=i.facility_id
where i.drug_id=26 and f.city='Phoenix'
order by i.qty desc
limit 25;

/*
+------+-------------+---------+---------+-------+
| qty  | facility_id | locator | city    | state |
+------+-------------+---------+---------+-------+
| 2740 |         412 | A11B44  | Phoenix | AZ    |
*/

```

- `flag{739-18-9}` ... nope
- `flag{426-12-7}` ... nope

`flag{412-11-44}`

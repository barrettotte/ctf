# order-up

Dr. Flegg prescribed Automeda to a patient in June 2023. What is the order number for this prescription?

Submit the flag as flag{order_num}.

Use the database dump from Aurora Compromise.

## Solution

```sql
select drug_id from drugs where drug_name='Automeda';

select o.order_num, s.staff_id, s.first_name, s.last_name, p.date_prescribed
from orders as o
join prescriptions as p on p.prescription_id=o.order_id
join staff as s on p.doctor_id=s.staff_id
  and s.last_name='Flegg'
join drugs as d on p.drug_id=d.drug_id
  and d.drug_name='Automeda'
  and p.date_prescribed >= '2023-06-01'
  and p.date_prescribed < '2023-07-01'
order by p.date_prescribed desc;
-- H81QEO9CHSN0G2HN

select first_name, last_name
from staff where last_name='Flegg';

```

```sql
select o.order_num
from prescriptions as p
join drugs as d on p.drug_id=d.drug_id and d.drug_name='Automeda'
join orders as o on p.prescription_id=o.prescription_id
join staff as s on p.doctor_id=s.staff_id
  and s.last_name='Flegg'
where p.date_prescribed >= '2023-06-01'
  and p.date_prescribed < '2023-07-01'
order by p.date_prescribed;
-- DYP8AXK3QG9OTPWB
```

`flag{DYP8AXK3QG9OTPWB}`
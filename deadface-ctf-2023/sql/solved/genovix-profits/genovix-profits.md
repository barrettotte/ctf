# genovix-profits

Genovex, a pharmaceutical company, is concerned that DEADFACE will target their company based on 
how much money they made this year on prescriptions at the Aurora Health pharmacy. 
How much money did Genovex make in 2023 based on the Aurora database?

Submit the dollar value as the flag. Example: flag{$1234.56}

Note: Round to the nearest hundredths.

Use the database dump from Aurora Compromise.

## Solution

```sql
select supplier_id from suppliers where supplier_name='Genovex';
-- id=32

select t.total_cost
from transactions as t -- empty?
-- join billing as b on t.billing_id=b.billing_id
-- join patients as p on b.patient_id=p.patient_id
-- join prescriptions ps on ps.patient_id=p.patient_id
-- join drugs as d on d.drug_id=ps.drug_id
-- join suppliers as s on s.supplier_id=d.supplier_id
  -- and s.supplier_name='Genovex';

select round(sum(d.cost), 2)
from drugs as d
join suppliers as s on s.supplier_id=d.supplier_id
  and s.supplier_name='Genovex'
join prescriptions as p on p.drug_id=d.drug_id;
-- 59466.64 ... nope

with x as (
  select d.cost * p.refills as total_cost
  from drugs as d
  join suppliers as s on s.supplier_id=d.supplier_id
    and s.supplier_name='Genovex'
  join prescriptions as p on p.drug_id=d.drug_id
)
select round(sum(total_cost), 2)
from x;
-- 207007.52 ... nope

with x as (
  select d.cost * p.refills as total_cost
  from drugs as d
  join suppliers as s on s.supplier_id=d.supplier_id
    and s.supplier_name='Genovex'
  join prescriptions as p on p.drug_id=d.drug_id
    and date_prescribed >= '2023-01-01'
)
select round(sum(total_cost), 2)
from x;
-- 69964.96 ... nope

with x as (
  select d.cost as total_cost
  from drugs as d
  join suppliers as s on s.supplier_id=d.supplier_id
    and s.supplier_name='Genovex'
  join prescriptions as p on p.drug_id=d.drug_id
    and date_prescribed >= '2023-01-01'
)
select round(sum(total_cost), 2)
from x;
-- 19249.88
```

`flag{$19249.88}`
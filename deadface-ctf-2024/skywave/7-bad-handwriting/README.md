# 7 - Bad Handwriting

One of the technicians performed maintenance on Tower 133 on August 26, 2024, but the technician's handwriting on the repair log cannot be deciphered. What is the employee number of the employee who conducted maintenance on that tower and on that date?

Submit the flag as flag{employee_number}. Example: flag{T123456789}.

## Solution

```sql
select * from Tower_Maintenance where maintenance_date='2024-08-26';
-- +----------------+----------+----------------------------+------------------+---------------+
-- | maintenance_id | tower_id | maintenance_type           | maintenance_date | technician_id |
-- +----------------+----------+----------------------------+------------------+---------------+
-- |            361 |      196 | Component replacement      | 2024-08-26       |           170 |
-- |            434 |       45 | Tower structure inspection | 2024-08-26       |           269 |
-- |            522 |      133 | Miscellaneous              | 2024-08-26       |           323 |
-- +----------------+----------+----------------------------+------------------+---------------+

select * from Technicians where technician_id=323;
```

`flag{T263739990}`

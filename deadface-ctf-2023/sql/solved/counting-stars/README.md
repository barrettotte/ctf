# counting-stars

We know DEADFACE is trying to get their hands on STAR, so it makes sense that they will try to target the doctor 
who prescribes the most STAR from the Aurora database. 
Provide the first and last name and the type of doctor (position name) that prescribed the most STAR from the database.

Submit the flag as flag{FirstName LastName Position}.

For example: flag{John Doe Podiatrist}

Use the database dump from Aurora Compromise.

## Solution

```sql
select drug_id from drugs where drug_name='Starypax';
-- 26

select count(*), prescriptions.doctor_id, staff.first_name, staff.last_name, positions.position_name
from prescriptions
join staff on prescriptions.doctor_id=staff.staff_id
  and prescriptions.drug_id=26
join positions_assigned on positions_assigned.staff_id=staff.staff_id
join positions on positions_assigned.position_id=positions.position_id
group by prescriptions.doctor_id, staff.first_name, staff.last_name, positions.position_name
order by count(*) desc
limit 5;
```

`flag{Alisa MacUchadair Dermatologist}`

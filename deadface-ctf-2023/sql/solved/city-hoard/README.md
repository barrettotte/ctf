# city-hoard

Aurora is asking for help in determining which city has the largest inventory of Remizide based on the Aurora database.

Submit the flag as flag{city}.

Use the database dump from Aurora Compromise.

## Solution

```sql
select inventory.qty, facilities.city, drugs.drug_name
from inventory
join drugs on drugs.drug_id=inventory.drug_id
  and drugs.drug_name='Remizide'
join facilities on inventory.facility_id=facilities.facility_id
order by inventory.qty desc
limit 10;

/*
+------+-----------------+-----------+
| qty  | city            | drug_name |
+------+-----------------+-----------+
| 2999 | Miami           | Remizide  |
| 2996 | Tulsa           | Remizide  |
| 2992 | Seattle         | Remizide  |
| 2991 | Lansing         | Remizide  |
| 2988 | West Palm Beach | Remizide  |
| 2987 | Van Nuys        | Remizide  |
| 2985 | Atlanta         | Remizide  |
| 2979 | Chicago         | Remizide  |
| 2978 | Houston         | Remizide  |
| 2971 | Dallas          | Remizide  |
+------+-----------------+-----------+
*/
```

`flag{Miami}`

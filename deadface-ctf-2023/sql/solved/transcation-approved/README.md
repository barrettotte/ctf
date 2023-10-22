# transaction-approved

Turbo Tactical wants you to determine how many credit cards are still potentially at risk of being used by DEADFACE. 
How many credit cards in the Aurora database are NOT expired before Oct 2023?

Submit the flag as flag{#}.

Use the database dump from Aurora Compromise.

## Solution

```sql
select card_num, exp, ccv from billing limit 5;
/*
+------------------+---------+-----+
| 5108755417799342 | 2025-03 | 758 |
| 5048375263334129 | 2025-10 | 265 |
| 5048372308393210 | 2027-12 | 535 |
| 5048370980730428 | 2025-10 | 466 |
| 5108756545445063 | 2024-04 | 447 |
+------------------+---------+-----+
*/

select count(distinct card_num)
from billing
where exp < '2023-10-01';
-- 1606

select count(distinct card_num)
from billing
where exp >= '2023-10-01';
-- 8785
```

`flag{8785}`
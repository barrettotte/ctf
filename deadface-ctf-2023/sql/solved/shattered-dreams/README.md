# shattered-dreams

DEADFACE is on the brink of selling a patient's credit card details from the Aurora database to a dark web buyer. 
Investigate Ghost Town for potential leads on the victim's identity.

Submit the flag as flag{Firstname Lastname}. Example: flag{John Smith}.

Use the database dump from Aurora Compromise.

## Solution

https://ghosttown.deadface.io/t/we-got-a-potential-buyer/107/3

target sha1 hash -> `911d1fc5930fa5025dbc2d3953c94de9e4773584`

```txt
Awesome. How are you coming up with that SHA1? The patient_id?

No I’m actually including almost the full billing and patient data. I’m just concatenating the following:

    card number
    expiration
    CCV
    patient_id
    patient first name
    patient last name
    patient middle initial
    patient sex
    patient email
    patient address (street, city, state, zip)
    patient dob

no delimiters
```

```sql
with hashes as (
  select p.patient_id, p.first_name, p.last_name,
    sha1(concat(b.card_num, b.exp, b.ccv, 
      p.patient_id, p.first_name, p.last_name, p.middle,
      p.sex, p.email, p.street, p.city, p.state, p.zip, p.dob)) as hash
from billing as b
join patients as p on p.patient_id=b.patient_id
)
select * from hashes
where hash='911d1fc5930fa5025dbc2d3953c94de9e4773584'
limit 10;

/*
+------------+------------+-----------+------------------------------------------+
| patient_id | first_name | last_name | hash                                     |
+------------+------------+-----------+------------------------------------------+
|      16314 | Berton     | Luchetti  | 911d1fc5930fa5025dbc2d3953c94de9e4773584 |
+------------+------------+-----------+------------------------------------------+
*/
```

`flag{Berton Luchetti}`

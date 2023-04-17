# packet-cyclone

**SOLVED**

> Pandora's friend and partner, Wade, is the one that leads the investigation into the relic's location. 
> Recently, he noticed some weird traffic coming from his host. 
> That led him to believe that his host was compromised. 
> After a quick investigation, his fear was confirmed. 
> Pandora tries now to see if the attacker caused the suspicious traffic during the exfiltration phase. 
> Pandora believes that the malicious actor used rclone to exfiltrate Wade's research to the cloud. 
> Using the tool called "chainsaw" and the sigma rules provided, can you detect the usage of rclone from the event logs produced by Sysmon? 
> To get the flag, you need to start and connect to the docker service and answer all the questions correctly.

windows event logs

sigma rules? https://github.com/SigmaHQ/sigma

https://github.com/WithSecureLabs/chainsaw

```sh
git clone https://github.com/countercept/chainsaw.git
rustup update
cargo build --release

~/Downloads/chainsaw/target/release/chainsaw hunt Logs/ -s ./sigma_rules/ --mapping ~/Downloads/chainsaw/mappings/sigma-event-logs-all.yml
# 2 results
```

- email: majmeret@protonmail.com
- password: 
- cloud storage: mega
- ID: 3820
- folder: C:\Users\Wade\Desktop\Relic_location
- folder: exfiltration

`HTB{3v3n_3xtr4t3rr3str14l_B31nGs_us3_Rcl0n3_n0w4d4ys}`

# whats-the-wallet

Ransomware was recently discovered on a system within De Monne’s network courtesy of a DEADFACE member. 
Luckily, they were able to restore from backups. 
You have been tasked with finding the Bitcoin wallet address from the provided sample so that it can be reported to the authorities. 
Locate the wallet address in the code sample and submit the flag as flag{wallet_address}.

https://cyberhacktics.sfo2.digitaloceanspaces.com/DEADFACECTF2023/Challenges/for/for01/Bitcoin.txt

## Solution

```ps1
$encodedScript = @"
function Store-BtcWalletAddress {
    `$global:BtcWalletAddress = [System.Convert]::FromBase64String([System.Text.Encoding]::UTF8.GetBytes('bjMzaGE1bm96aXhlNnJyZzcxa2d3eWlubWt1c3gy'))
}

# Call the function to store the encoded Bitcoin wallet address
Store-BtcWalletAddress

# Access the stored encoded Bitcoin wallet address
Write-Host "Encoded Bitcoin Wallet Address: `$BtcWalletAddress"
"@
```

`bjMzaGE1bm96aXhlNnJyZzcxa2d3eWlubWt1c3gy` from base64 -> `n33ha5nozixe6rrg71kgwyinmkusx2`

`flag{n33ha5nozixe6rrg71kgwyinmkusx2}`
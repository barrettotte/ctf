# malum

Well, it happened. The ransomware event took us out but we are recovering. It's Tuesday now and time to head into the office. As you arrive your boss walks into the SOC with a sigh and look right to you; here we go. He drops a USB on your desk and says "I need you to go through all the logs to find out HOW these guys got valid credentials to attack us". Can you identify the threat vector that was used to gain persistence into the network by reading through security logs? What you find will be the flag.

Submit the flag as flag{flagText}

## Solution

```
Account Whose Credentials Were Used:
	Account Name:		UMFD-1
	Account Domain:		Font Driver Host

```

just looked around and guessed...

`flag{stabBingStabber1}`
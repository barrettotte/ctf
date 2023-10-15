# reminiscence

We've detected unusual network traffic within our network. 
Upon inspection, it turns out that a malicious actor gained access to one of our staff's credentials and logged into the server. 
Could you analyze what actually occurred?

## Solution

Hint: It is necessary to decrypt all of the packets in order to gain a better understanding of what truly occurred during each session. 
In this case, you may need to use a certain tool based on a specific CVE

Discord:

For Reminiscence it was affected by the same CVE as compromised (CVE-2008-0166). 
Due to the predictable PRNG nature, it might be possible to decrypt the SSHv2 packets. 
Fortunately, there are already several appropriate tools available, such as 'ssh_kex_keygen' and 'ssh_decoder.rb'.

- https://github.com/trou/ssh_kex_keygen
- https://github.com/jjyg/ssh_decoder

For a weird reason, the Makefile can't be normally compiled. 
So it must be tinkered first. Part 3-7th question can be fully answered after full packet decryption


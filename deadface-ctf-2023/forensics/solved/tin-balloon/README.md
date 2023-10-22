# tin-balloon

We've discovered that DEADFACE was somehow able to extract a fair amount of data from Techno Global Research Industries. 
We are still working out the details, but we believe they crafted custom malware to gain access to one of TGRI's systems. 
We intercepted a Word document that we believe mentions the name of the malware, in addition to an audio file that was part of the same conversation. We're not sure what the link is between the two files, but I'm sure you can figure it out!

Submit the flag as: flag{executable_name}. Example: flag{malware.exe}.

## Solution

Found in prev task - https://ghosttown.deadface.io/t/tgri-and-lytton-labs/96/17

`Sequence 01.zip`

```sh
strings Untitlednosubject.docx
```

```xml
<encryption xmlns="http://schemas.microsoft.com/office/2006/encryption" xmlns:p="http://schemas.microsoft.com/office/2006/keyEncryptor/password" xmlns:c="http://schemas.microsoft.com/office/2006/keyEncryptor/certificate"><keyData saltSize="16" blockSize="16" keyBits="256" hashSize="64" cipherAlgorithm="AES" cipherChaining="ChainingModeCBC" hashAlgorithm="SHA512" saltValue="ttv56oz..."> <!-- salt turns to garbage i think-->


    <!-- Untitlednosubject.docx at bottom of doc -->
    <dataIntegrity
        encryptedHmacKey="2j26e12rOCPvKZev0gFPoZE0aHV1cDwpCRX5mzIwCokXANzTBnFleppEQyuO2tfTuS5OzZbjanmyCeMBYmlM6A=="
        encryptedHmacValue="e/6wGNurF5xnV8Meh7YAZjjfw2NVb1acnujJOTpn0D9O2Fvukvy4f+NUBOInKgzTDg36hNlforWz5Jwj2/Ez0Q==" />
    <keyEncryptors>
        <keyEncryptor uri="http://schemas.microsoft.com/office/2006/keyEncryptor/password">
            <p:encryptedKey spinCount="100000" saltSize="16" blockSize="16" keyBits="256" hashSize="64"
                cipherAlgorithm="AES" cipherChaining="ChainingModeCBC" hashAlgorithm="SHA512"
                saltValue="1EiusSkMUn9eHlQuJehZfQ==" encryptedVerifierHashInput="WI3sdJ9fJSQCM47Q/2YUGg=="
                encryptedVerifierHashValue="pSVUQ6+iok4K07dM8k8RLLPmUeQClIG9TZfUqoITJQ6XTXoC7s2dsG+HlvtNnFaBbfjxMAhF6edzcfG2fesfWQ=="
                encryptedKeyValue="7dXhNynOfGlCIUvhGB0lQzcc5nhQu3dp9kny3iE7Oc0=" />
        </keyEncryptor>
    </keyEncryptors>
</encryption>
```

opened audio file audacity, switched to spectrogram `./spectrogram.png`
has text `Gr33dK1Lzz@11Wh0Per5u3`   (not sure if 0 or O)

opened in free trial microsoft 365

```txt
We have the ID card of one the brand new employees Alejandro, We now know the location of Techno Global, we have a man on sight that has been tailing him. We believe we can get into the facility at 3 am.

We don’t know how long we can have a foothold on the system but we are going to use Wh1t3_N01Z3.exe to sent out a reverse shell. Be prepared to listen for the signal.
```

`flag{Wh1t3_N01Z3.exe}`

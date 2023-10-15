# iop

I need to hide a secret, so I modified [this](http://www.artpol-software.com/) project for archiving files. 
I haven't implemented extract feature though. 
Pretty sure the archive looks like a normal archive, or is it?

## Solution

Hint: You have the PDB of my custom archiver, make the use of it! Also, it's never wrong to read source codes!

From Discord:

- Do some forensic anaylsis on the custom-archive (by iopManager.exe) and original-archive (ZipArc.exe, can be downloaded by the link given in description), you compare both archive to see the difference
- If you noticed, some of the field in the custom-archive is set to 0 (compressedSize and uncompressSize)
- You can also notice that field fileNameLength is incorrect

By doing comparison, you can easily fix the "custom archive" so that it can be opened using the original ZipArc.exe program. But to extract, you will been the zip password, you can easily find the password in function CZipArcDoc::OpenZipFile since it's hardcoded. After you have succesfully extract the flag file, you will notice that it's still a garbage data, because there's another encryption layer. If you do some reversing in function CZipArcDoc::Extract,  you can see that it calls function CZipArcDoc::DecryptFileA which will lead you to another function. The main encryption function is in CZipArcDoc::EncryptDecryptData. The encrypt function itself is just a basic xor, which means that you can just decrypt it by xoring it back.

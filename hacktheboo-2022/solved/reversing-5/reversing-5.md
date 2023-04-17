# reversing 5

```sh
wireshark trace.pcap &

# packet 5 data:
# 5f558867993dccc99879f7ca39c5e406972f84a3a9dd5d48972421ff375cb18c
```

```sh
file securetransfer
# ELF 65 LSB pie, dynamic, stripped

strings securetransfer
# EVP_EncryptUpdate
# OPENSSL_init_crypto
# EVP_DecryptFinal_ex
# EVP_DecryptInit_ex
# EVP_DecryptUpdate
# EVP_EncryptInit_ex
# EVP_aes_256_cbc
# EVP_CIPHER_CTX_new
# EVP_CIPHER_CTX_free
# EVP_EncryptFinal_ex
#
# ERROR: Socket creation failed
# ERROR: Invalid input address '%s'
# ERROR: Connection failed
# ERROR: Can't open the file '%s'
# ERROR: File too small
# ERROR: File too large
# ERROR: Failed reading the file
# File send...
# ERROR: Socket bind failed
# ERROR: Listen failed
# ERROR: Accept failed
# ERROR: Reading secret length
# ERROR: File send doesn't match length
# File Received...
# Sending File: %s to %s
# Receiving File
# Usage ./securetransfer [<ip> <file>]

chmod +x securetransfer
ltrace ./securetransfer
# nothing

strace ./securetransfer
# nothing of interest?

readelf -a securetransfer
```

```c
// open in Ghidra


EVP_CIPHER * EVP_aes_256_cbc(void) {
  EVP_CIPHER *pEVar1;
  pEVar1 = EVP_aes_256_cbc();
  return pEVar1;
}

int EVP_EncryptInit_ex(EVP_CIPHER_CTX *ctx,EVP_CIPHER *cipher,ENGINE *impl,uchar *key,uchar *iv) {
  int iVar1;
  iVar1 = EVP_EncryptInit_ex(ctx,cipher,impl,key,iv);
  return iVar1;
}

// main
undefined8 FUN_00101dce(int param_1,long param_2) {
  OPENSSL_init_crypto(2,0);
  OPENSSL_init_crypto(0xc,0);
  OPENSSL_init_crypto(0x80,0);

  if (param_1 == 3) {
    printf("Sending File: %s to %s\n",*(undefined8 *)(param_2 + 0x10),*(undefined8 *)(param_2 + 8));
    FUN_00101835(*(undefined8 *)(param_2 + 8),*(undefined8 *)(param_2 + 0x10));   // ENCRYPT ???
  }
  else if (param_1 == 1) {
    puts("Receiving File");
    FUN_00101b37();
  }
  else {
    puts("Usage ./securetransfer [<ip> <file>]");
  }
  return 0;
}
```

```c
// encrypt?
int FUN_00101529(uchar *param_1,int param_2,uchar *param_3) {

  int iVar1;
  EVP_CIPHER *cipher;
  long in_FS_OFFSET;
  int local_50;
  int local_4c;
  char *local_48;
  EVP_CIPHER_CTX *local_40;
  uchar local_38;
  undefined local_37;
  undefined local_36;
  undefined local_35;
  undefined local_34;
  undefined local_33;
  undefined local_32;
  undefined local_31;
  undefined local_30;
  undefined local_2f;
  undefined local_2e;
  undefined local_2d;
  undefined local_2c;
  undefined local_2b;
  undefined local_2a;
  undefined local_29;
  undefined local_28;
  undefined local_27;
  undefined local_26;
  undefined local_25;
  undefined local_24;
  undefined local_23;
  undefined local_22;
  undefined local_21;
  undefined local_20;
  undefined local_1f;
  undefined local_1e;
  undefined local_1d;
  undefined local_1c;
  undefined local_1b;
  undefined local_1a;
  undefined local_19;
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  local_38 = 's';
  local_2f = 0x65;
  local_2e = 0x74;
  local_2d = 0x6b;
  local_1d = 0x74;
  local_1c = 0x69;
  local_37 = 0x75;
  local_36 = 0x70;
  local_22 = 0x6e;
  local_21 = 99;
  local_1b = 0x6f;
  local_32 = 0x65;
  local_31 = 99;
  local_33 = 0x73;
  local_20 = 0x72;
  local_1f = 0x79;
  local_30 = 0x72;
  local_26 = 0x66;
  local_25 = 0x6f;
  local_24 = 0x72;
  local_1a = 0x6e;
  local_2c = 0x65;
  local_2b = 0x79;
  local_2a = 0x75;
  local_29 = 0x73;
  local_28 = 0x65;
  local_27 = 100;
  local_23 = 0x65;
  local_35 = 0x65;
  local_34 = 0x72;
  local_1e = 0x70;
  local_19 = 0x21;
  local_48 = "someinitialvalue";
  local_40 = EVP_CIPHER_CTX_new();
  if (local_40 == (EVP_CIPHER_CTX *)0x0) {
    iVar1 = 0;
  }
  else {
    cipher = EVP_aes_256_cbc();
    
    iVar1 = EVP_EncryptInit_ex(local_40,cipher,(ENGINE *)0x0,&local_38,(uchar *)local_48);
    // local_38 = key = 
    // local_48 = iv  = "someinitialvalue"

    if (iVar1 == 1) {
      iVar1 = EVP_EncryptUpdate(local_40,param_3,&local_50,param_1,param_2);
      if (iVar1 == 1) {
        local_4c = local_50;
        iVar1 = EVP_EncryptFinal_ex(local_40,param_3 + local_50,&local_50);
        if (iVar1 == 1) {
          local_4c = local_4c + local_50;
          EVP_CIPHER_CTX_free(local_40);
          iVar1 = local_4c;
        }
        else {
          iVar1 = 0;
        }
      }
      else {
        iVar1 = 0;
      }
    }
    else {
      iVar1 = 0;
    }
  }
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return iVar1;
}

int EVP_EncryptInit_ex(EVP_CIPHER_CTX *ctx,EVP_CIPHER *cipher,ENGINE *impl,uchar *key,uchar *iv) {
  int iVar1;
  iVar1 = EVP_EncryptInit_ex(ctx,cipher,impl,key,iv);
  return iVar1;
}

```


```txt
setktiupncoecsryrforneyusedeerp!
is this jumbled?

oh lmao yeah

  local_38 = 's';
  local_37 = 'u';
  local_36 = 'p';
  local_35 = 'e';
  local_34 = 'r';
  local_33 = 's';
  local_32 = 'e';
  local_31 = 'c';
  local_30 = 'r';
  local_2f = 'e';
  local_2e = 't';
  local_2d = 'k';
  local_2c = 'e';
  local_2b = 'y';
  local_2a = 'u';
  local_29 = 's';
  local_28 = 'e';
  local_27 = 'd';
  local_26 = 'f';
  local_25 = 'o';
  local_24 = 'r';
  local_23 = 'e';
  local_22 = 'n';
  local_21 = 'c';
  local_20 = 'r';
  local_1f = 'y';
  local_1e = 'p';
  local_1d = 't';
  local_1c = 'i';
  local_1b = 'o';
  local_1a = 'n';
  local_19 = '!';

```

was too lazy to write a script, plugged data into https://www.devglan.com/online-tools/aes-encryption-decryption

AES 256, IV, secret

SFRCe3ZyeVMzQ3VSM19GMUwzX1RSNG5zZjNyfQ== (base 64)


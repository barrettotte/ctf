# hm74

> As you venture further into the depths of the tomb, your communication with your team becomes increasingly disrupted by noise. 
> Despite their attempts to encode the data packets, the errors persist and prove to be a formidable obstacle. 
> Fortunately, you have the exact Verilog module used in both ends of the communication. 
> Will you be able to discover a solution to overcome the communication disruptions and proceed with your mission?

TODO: review writeup

- https://github.com/meashiri/ctf-writeups/blob/main/202303_hackthebox/writeup_hw_hm74.md
- https://cristi075.github.io/HTB-Cyber-Apocalypse-2023-HM74

## Attempt

As you venture further into the depths of the tomb, your communication with your team becomes increasingly disrupted by noise. 
Despite their attempts to encode the data packets, the errors persist and prove to be a formidable obstacle. 
Fortunately, you have the exact Verilog module used in both ends of the communication. 
Will you be able to discover a solution to overcome the communication disruptions and proceed with your mission?

hamming code? https://en.wikipedia.org/wiki/Hamming_code

`nc 68.183.37.122 31187`

```
Captured: 1001100011000001001111001001100111001111100110111011011110001101110100100011000101011101111001000001010001111111000111100011001000011000100100011011011000100111001101000110101011111110011110000010100001000000011100010101110110000111000000010000100111011100110011100111001101010110110101011010011001001010110000011100011001000011100011110000001010100110001110100101111010111111110001111001100010010110001000000101001101110100101101111111001100000011100001110111011101110000010100000011101011100001110000100001111101010010000110001111001010101010001100110110100011101111100011010111111101000100100011101000001100111011110011111100001011010100101101011011111011101001011000001100011100110011001100110100110011000101011110110100100101001100000110000100100110000100001111111011000010001111010000111001100000011100110001010011111111101001110010101110110000001011111101000011001000101011111100110110111010001101111010100000100010000001011011100100011111010001

8e 89 c4 88 07 cb 69 0a e7 35 ee 4a 6f 40 24 53 3f 71 b8 c1 6c 1d e8 bc e1 03 d0 2a a3 4f 8d 44 87 66 54 94 46 e8 1f 18 9d 3d af 4e 5e ae 1f 33 08 0f ae 97 01 4d 55 97 c1 f4 92 c0 c0 4a 01 3f 52 a4 ff d1 7c 59 c1 b7 cc d1 c1 ed 1a 13 cc 2f 6b 21 bb 94 c1 32 df a6 36 55 18 d6 fe 96 b5 a7 83 86 68 6f 1b e6 0f 7a 75 de 0c 25 b6 be 56 b8 e3 0a 08 da 34 ab 71 2c 87 25 8c 39 90 70 95 04 93 31 e4 af 66 1e 55 80 04 31 ec 8e c9 fa bb fc 1c 05 83 e2 2b 9e fd 19 55 f4 34 62 9b 72 92 be dc e5 dd c0 9b 5e 57 95 96 d6 4c 4c c5 c1 83 df e6 52 0e 01 5b 90 34 bd 52 ea 2e 00 26 33 bb 07 44 85 d2 c3 bd cd 6a 50 0e 56 5f 92 67 74 7d af 36 12 fd f7 3e ae 1e 12 85 8b a1 0d 3f 1a 94 61 ea c4 6c af 95 34 16 7c ef 2b a0 2a a9 a8 ea 65 43 95 60 a2 19 64 55 02 78 25 ea ac e6 eb 6e 97 e5 a1 19 91 8d 11 ea d4 84 21 ad 7c 2c 8a 60 ea 77 18 55 82 f8 61 e4 bd 47 a6 2e d2 b1 76 ab 59 66 c3 c0 45 7b c0 f6 63 bb 92 26 3a 91 85 a4 7c de a3 d3 35 87 73 f2 38 cc 7c 72 80 db 4e 8d c1 57 0f 51 ba f2 1a f5 ee 5b a9 e8 e4 75 3a dc c4 84 9c ca 49 5b 08 d9 d7 d4 cd bc 8b a4 cd d6 03 95 8b 23 75 7b df 6c 71 03 7a 9c 5e 86 a2 6b ab 92 85 48 dc c1 ac 28 e9 12 c4 cf ca 38 a4 31 c0 49 08 4b 66 c6 ab a2 e7 74 ce d1
```

```sh
sudo apt-get install iverilog gtkwave

# compile and view simulation
iverilog encoder.sv -o encoder.vvp
vvp encoder.vvp
gtkwave encoder.vcd

./run.sh
``` 

```verilog
assign p0 = data_in[3] ^ data_in[2] ^ data_in[0];
assign p1 = data_in[3] ^ data_in[1] ^ data_in[0];
assign p2 = data_in[2] ^ data_in[1] ^ data_in[0];

assign ham_out = {p0, p1, data_in[3], p2, data_in[2], data_in[1], data_in[0]};

// 5 = 0b0101
// p0 = 
```

https://www.jameswhanlon.com/error-correcting-codes.html

https://www.micron.com/-/media/client/global/documents/products/technical-note/nand-flash/tn2963_ecc_in_slc_nand.pdf

Hamming codes are the most widely used linear block codes. Typically, a Hamming code
is defined as (2n - 1, 2n - n - 1), where:
• n is equal to the number of overhead bits.
• 2n - 1 is equal to the block size.
• 2n - n - 1 is equal to the number of data bits in the block

All Hamming codes can detect three errors and one correct one. Common Hamming
code sizes are (7, 4), (15,11), and (31, 26). All have the same Hamming distance.

https://www.tutorialspoint.com/hamming-code-for-single-error-correction-double-error-detection

odd parity (7-4=3)

https://michaeldipperstein.github.io/hamming.html



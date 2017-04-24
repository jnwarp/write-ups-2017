Cryptography
============

Trivia (Easy)
-------------

- What specific entity was responsible for decrypting the Zimmermann Telegram?
  - Room 40
- How many bytes long is an MD5 hash?
  - 16
- What was the first practical asymmetric cryptosystem created?
  - RSA
- On what day was the Enigma key cracked by the British?
  - 1941/07/09


Stego 1 (Medium)
----------------

- What is the algorithm used to encrypt the flag? (10 pts)


Decoding 1 (Easy)
-----------------

- NTZjbGFzc21pbnV0ZTUw
  - **56classminute50**
    - `echo -n NTZjbGFzc21pbnV0ZTUw | base64 --decode`
- 336964656150454f504c4530
  - 3ideaPEOPLE0
    - `echo -n 336964656150454f504c4530 | xxd -r -p`


Decoding 2 (Easy)
-----------------

- We have recovered a flash drive with an encrypted message and some block of text. We need your help to decode it.
- He cryptic message is 6:1:4 8:3:10 1:7:1 2:2:4 8:11:4 8:4:4 7:9:3 7:7:1 8:13:7 8:13:9. What does it say? (35 pts)
  - `I have the four suspicious samples from the medical company`
    - paragraph:sentence:word


Decoding 3 (Easy)
-----------------

- Police found an picture during a raid and need your help in decoding it.
- What does the message say? (50 pts)
  - `IF I AM CAUGHT, CONTINUE WITHOUT ME. FR0ZEN WILL KNOW WHAT COMES NEXT.`
    - Wingdings decoder
    - http://grompe.org.ru/static/wingdings_gaster.html


Decoding 4 (Easy):
------------------

- APY-VKUX-2868
  - `NCL-IXHK-2868`
    - Caesar (13)
- WLU-RGQT-7337
  - `NCL-IXHK-7337`
    - Caesar (17)


Decoding 5 (Medium):
--------------------

- Our officers have obtained an encrypted message. The forensics team was able to find a file that contains the string, "secret" which was used to encrypt the message. Take it from here and obtain the plaintext message.
- `Zeu @ctas1 vggsklif sevc cgk? Ltnip'k lxsvf wvhe xjvq tdp frc.` (50 pts)
  - `Has @lpha1 reported back yet? Haven't heard from them all day.`
    - Vigenere ("secret")
    - http://rumkin.com/tools/cipher/vigenere.php


Decoding 6 (Hard):
------------------

```
n = 2479
e = 23
c = 1329 75 2233 1050 1087 1329 1668 2211 1050 2196 2196 1746 1573
```

- Our officers have obtained several artifacts from a message that was encrypted with RSA. We need you to decrypt the message and figure out what the hackers are up to.
- What is the value of p (the smaller prime) (25 pts)
  - 37
    - 2479 = 37 * 67
- What is the value of q (the larger prime) (25 pts)
  - 67
- What is the plaintext of the encrypted message? (50 pts)
  - `SKY-RSAC-4419`
    - https://asecuritysite.com/Encryption/rsa
    - https://www.cs.drexel.edu/~introcs/Fa11/notes/10.1_Cryptography/RSA_Express_EncryptDecrypt.html


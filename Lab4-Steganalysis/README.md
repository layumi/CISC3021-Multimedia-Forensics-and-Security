# Lab4 - Steganalysis

1.	Implement the simple steganalysis methods for the LSB-based stegnography, as demonstrated in pages 27-33 of the lecture notes. Note especially the roles played by the plaintext encryption and the random path.

2.	Reproduce the results shown in pages 34-37 and show how the plaintext encryption influences the histogram (see page 37). Also, check the theoretical explanations in page 39, and try to figure out whether they match with your experimental results.

3.	Try exposure image. Could you notice any differences? 

4. Encrytion to cheat the histogram.

Tips: Regarding the encryption, let the binary plaintext be P and a random binary bit sequence be K, where K and P are of the same lengths. The encryption of P can be simply conducted as 

C = P \XOR K

where C is the ciphertext. 

 Think about Why!
<img width="1170" alt="image" src="https://github.com/user-attachments/assets/5c2478b5-96a7-4f49-a863-6c0f3286f00a">


5. Recover from encrytion.

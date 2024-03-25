# Shift Cipher Cryptanalysis : Decrypting Shift Ciphers with Statistics and Frequency Analysis

This repository houses the "Shift Cipher Cryptanalysis" project, a comprehensive cryptanalysis tool designed to decrypt ciphertexts encrypted with shift ciphers. Developed by Harshit Rajpal, Pranav Ghildiyaal, and Purna Sai Madala as part of an academic endeavor, this project embodies the intersection of classical cryptography techniques and modern computational approaches.
This cryptanalysis program is specifically designed to tackle the challenge of deciphering texts encrypted with various forms of shift ciphers. The encrypted texts (ciphertexts) are generated from English dictionary words and spaces, forming sequences that may not necessarily compose meaningful sentences for simplicity.

**Encryption Overview**

The ciphertexts are sequences derived from plaintexts by a series of transformation steps defined by a key sequence. Here, each symbol is either a space or one of the 26 lowercase letters from the English alphabet, without any special characters, punctuation, or uppercase letters.

**Key and Ciphertext Structure**

- **Key**: A sequence of \( t \) numbers, each ranging from 0 to 26.
- **Ciphertext**: A sequence of symbols from the set \{\<space\>, a, ..., z\}.

**Plaintext Dictionary**

The program has access to a plaintext dictionary containing a number \( u \) of \( L \)-symbol candidate plaintexts, which are utilized in the cryptanalysis process.

**Variability in Encryption**

The cryptanalysis challenge involves various parameters, like \( L \), \( u \), and \( t \), and each challenge ciphertext could have been encrypted using a different variant of the encryption scheme, including:
- Shift cipher (where \( t = 1 \))
- Mono-alphabetic substitution cipher (where \( t = 27 \))
- Poly-alphabetic substitution cipher (where \( t \ll 27 \))

**Encryption Mechanism**

The program must decipher the encryption schemes that introduce randomness into the ciphertexts to obscure the plaintext. For poly-alphabetic ciphers, this involves shifting the plaintext symbol \( m[i'] \) by a key-dependent number of positions. The introduction of randomness is controlled by a probability parameter \( \text{prob_of_random_ciphertext} \) and an undisclosed coin generation algorithm.

**Objectives of the Cryptanalysis Program**

The aim is to output the most likely \( L \)-symbol plaintext for any given ciphertext, leveraging the commonalities across the encryption schemes used:

- **Message Space**: Set \{\<space\>, a, ..., z\}\(^L\).
- **Ciphertext Space**: Set \{\<space\>, a, ..., z\}\(^{L+r}\), where \( r \geq 0 \).
- **Key Space**: Set \{0, ..., 26\}\(^t\).


## Mathematical Foundations

One of the key techniques used in our project is the **Chi-Squared Statistic**, which is crucial for frequency analysis in cryptanalysis. The Chi-Squared Statistic (\( \chi^2 \)) formula is given by:

$$
\chi^2 = \sum \frac{(O_i - E_i)^2}{E_i}
$$

where:
- \(O_i\) is the observed frequency of the ith letter in the ciphertext,
- \(E_i\) is the expected frequency of the ith letter in standard English text,
- The summation (\( \sum \)) runs over all possible letters.


The **Levenshtein Distance** measures the minimum number of single-character edits (insertions, deletions, or substitutions) required to change one string into another. It's a critical metric for evaluating the similarity between the decrypted text and potential plaintexts. The formula is given by:

```plaintext
L(a, b) = 
  { 
    max(|a|, |b|)                              if min(|a|, |b|) == 0,
    min( L(a-1, b) + 1, 
         L(a, b-1) + 1, 
         L(a-1, b-1) + δ(a, b) )               otherwise. 
  }

Where `L(a, b)` is the Levenshtein distance between strings `a` and `b`, `|a|` and `|b|` represent the length of `a` and `b` respectively, and `delta(a, b)` is `0` if `a == b` and `1` otherwise (indicating the cost of substituting `a` with `b`).
```


The **Exhaustive Key Search** is a fundamental decryption technique used in our project. This brute-force approach is instrumental in decrypting ciphertexts encrypted with a shift cipher, also known as a Caesar cipher.

The technique involves trying every possible key until the correct one is found. For a shift cipher, which has a limited key space of 26 possible shifts (in the case of the English alphabet), the Exhaustive Key Search method is both practical and guaranteed to find the correct decryption, given enough time.

 **Implementation**

In our cryptanalysis tool, we implement the Exhaustive Key Search as follows:

```plaintext
Function exhaustive_key_search(ciphertext, possible_keys)
  For each key in possible_keys
    decrypted_text = decrypt(ciphertext, key)
    If decrypted_text is valid
      Return decrypted_text
  Return "Decryption failed"
```

## Outcomes 

**Mismatch VS Randomness**

<img width="818" alt="image" src="https://github.com/Pranav-2301/CipherDecryptor-Trio/assets/82222889/6ee8dead-a619-4306-9dfe-4fb9d6892dcc">


**Processing Time VS Randomness**
<img width="772" alt="image" src="https://github.com/Pranav-2301/CipherDecryptor-Trio/assets/82222889/36ddc1cc-4f63-4c9c-9a10-5f24d751488d">



## Importance

Despite its simplicity, it can be computationally expensive and time-consuming, especially for long keys. However, it guarantees that if the key is in the key space, it will be found.

In conjunction with the Chi-Squared Statistic and Levenshtein Distance methods, the Exhaustive Key Search provides a baseline for our decryption process. While the statistical methods help narrow down the key space by identifying the most probable key based on frequency analysis, the brute-force approach ensures that even the most improbable keys are tested, offering a comprehensive solution to the decryption challenge.

This multi-faceted approach allows our tool to tackle various scenarios ranging from simple to complex ciphertexts, providing a robust and reliable means for decrypting and analyzing encrypted texts.


## Acknowledgements

Special thanks to all the contributors who have invested their time and expertise into refining the "Shift Cipher Cryptanalysis" project:

- Harshit Rajpal 
- Pranav Ghildiyaal
- Purna Sai Madala

Their dedication and collaborative spirit have been the backbone of this project's success.


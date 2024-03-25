# CipherDecryptor-Trio : Decrypting Shift Ciphers with Mathematics

This repository presents "CipherDecryptor-Trio", a project by Rajpal, Ghildiyaal, and Madala, which applies mathematical analysis to decrypt shift ciphers. The tool combines exhaustive key search, chi-squared statistics, and Levenshtein distance in a novel approach to cryptanalysis.


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

## Importance

Despite its simplicity, it can be computationally expensive and time-consuming, especially for long keys. However, it guarantees that if the key is in the key space, it will be found.

In conjunction with the Chi-Squared Statistic and Levenshtein Distance methods, the Exhaustive Key Search provides a baseline for our decryption process. While the statistical methods help narrow down the key space by identifying the most probable key based on frequency analysis, the brute-force approach ensures that even the most improbable keys are tested, offering a comprehensive solution to the decryption challenge.

This multi-faceted approach allows our tool to tackle various scenarios ranging from simple to complex ciphertexts, providing a robust and reliable means for decrypting and analyzing encrypted texts.


## Acknowledgements

Special thanks to all the contributors who have invested their time and expertise into refining the "CipherDecryptor-Trio" project:

- Harshit Rajpal 
- Pranav Ghildiyaal
- Purna Sai Madala

Their dedication and collaborative spirit have been the backbone of this project's success.

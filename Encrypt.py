import random
import string

def coin_generation_algorithm():
    """Simulates a coin toss. Adjust the function to use other parameters if needed."""
    return random.random()

def encrypt_shift_cipher(sentence, shift, prob_of_random_ciphertext):
    custom_alphabet = " " + string.ascii_lowercase
    encrypted_text = ""
    message_pointer = 0
    L = len(sentence)

    while message_pointer < L:
        coin_value = coin_generation_algorithm()

        if prob_of_random_ciphertext <= coin_value <= 1:
            # Process and encrypt the character from the message
            if sentence[message_pointer] in custom_alphabet:
                original_index = custom_alphabet.index(sentence[message_pointer])
                shifted_index = (original_index + shift) % len(custom_alphabet)
                encrypted_text += custom_alphabet[shifted_index]
            else:
                encrypted_text += sentence[message_pointer]
            message_pointer += 1
        elif 0 <= coin_value < prob_of_random_ciphertext:
            # Insert a random character into the ciphertext
            random_char = random.choice(custom_alphabet)
            encrypted_text += random_char

    return encrypted_text

# Example usage
if __name__ == "__main__":
    shift_amount = int(input("Enter the shift amount: "))
    sentence_to_encrypt = input("Enter the sentence to encrypt: ").lower()  # Ensure input is lowercase
    randomness = float(input("Enter the randomness probability (0 to 1.0): "))
    cipher_text = encrypt_shift_cipher(sentence_to_encrypt, shift_amount, randomness)
    print(f"Cipher Text: {cipher_text}")

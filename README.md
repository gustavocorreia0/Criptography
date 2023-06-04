# Cryptography in Python

The Python cryptography project is an implementation of popular cryptography algorithms using the Python programming language. The
project's goal is to provide a flexible and easy-to-use library for encrypting and decrypting data, while also exploring fundamental
cryptography concepts.

In this project i used the cipher Rote 13.

The Rote 13 cipher, also known as ROT13, is a simple example of encryption by substitution. This cipher is a variation of the Caesar
cipher, where each letter of the alphabet is replaced by another letter that is 13 positions forward or backward in the alphabet, 
maintaining the same distinction between uppercase and lowercase.

For example, the letter "A" is replaced by the letter "N", "B" is replaced by "O", and so on. When it comes to the letter "Z", the 
substitution returns to the beginning of the alphabet, so "M" is replaced by "Z", "N" by "A", and so on.

The Rote 13 cipher is considered a monoalphabetic substitution cipher because the letter substitution is fixed and does not depend on the 
context or position of the letter in the original message. This makes the cipher quite easy to implement and understand.

Despite its simplicity, the Rote 13 cipher is useful for basic information concealment purposes, especially when strong security is not 
required. It is often used to obscure messages in online forums or word games, adding a simple level of challenge or encryption.

In the Python cryptography project, the Rote 13 cipher was implemented as one of the available algorithms for encrypting and decrypting 
text. Users can provide a message and the corresponding function will replace each letter with the corresponding letter, according to the 
logic of the Rote 13 cipher.

The implementation of the Rote 13 cipher in the project follows the basic principles of modular cryptography, allowing it to be easily 
integrated with other algorithms available in the project. In addition, the project provides usage examples, documentation, and unit 
tests to ensure the functionality and accuracy of the Rote 13 cipher.

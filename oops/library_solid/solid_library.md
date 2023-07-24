After all these years, Mr Smith does not want to rest and wants to solidify his library by following SOLID prinicples.
For doing that he followed the following steps.


Step 1: Single Responsibility Principle (SRP)

Mr. Smith realized the need to have a separate class for managing book displays. He created a "BookDisplay" class to handle the presentation of book information.

Step 2: Open/Closed Principle (OCP)

To accommodate various types of book displays, Mr. Smith used the power of inheritance and polymorphism. He extended the "BookDisplay" class with specialized displays like "TextDisplay" and "GraphicalDisplay."

Step 3: Liskov Substitution Principle (LSP)

The "TextDisplay" and "GraphicalDisplay" classes were designed to be substitutable for the base "BookDisplay" class, ensuring they behaved consistently.

Step 4: Interface Segregation Principle (ISP)

To avoid unnecessary dependencies, Mr. Smith split the "BookDisplay" class into smaller interfaces, allowing the library to use only the methods it required.

Step 5: Dependency Inversion Principle (DIP)

By using interfaces for book display, Mr. Smith ensured that the "Library" class depended on abstractions rather than concrete implementations, promoting flexibility.

With all the SOLID principles in place, Mr. Smith's library became a model of maintainable and scalable code. It enchanted the townspeople with its organized and adaptable design, a true testament to the magic of SOLID programming.


Let's try to code for the same ! 

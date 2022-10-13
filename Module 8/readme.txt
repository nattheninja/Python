Name: Nathalie Agustin - nagusti1
Module 8: Linear Feedback Shift Registers		Due: April 3, 2022 11:59 PM

Approach:
lsfr.py  
- In constructor of LSFR class, set attributes seed and tap
- In bit(), return the bit at specified index
- In step(), take the bit specified in tap and XOR it with leftmost bit from seed. Strip off the first bit of the seed, and append the new XOR'd bit to the end of that. Return the modified seed.
- In __str__() modified print statement to pad zeroes so that output matched homework instructions and included the new XOR value
- In main(), print lsfr output of given seeds and tap

image_encrypter.py
- Import Image from PIL Library and our lsfr
- In constructor of class, set attributes for lsfr and file name
- In open_image(), open the image with the provided filename. Need attribute self.image in order to access modified image later in the code.
- In pixelate(), use Image.load() to convert PNG file to pixels
- In encrypt(), retrieve the image size to get the rows and columns of pixels that are to be iterated over. For every pixel, unpack the RGB values and XOR them with the results of lsfr.step(). Pack the pixels back in to the pixelated image array. 
- In save_image(), separate the received file name into the name of the file and the extension. Save and return the modified image. 
- In main(), set up LSFR and ImageEncrypter instance. Execute pixelate(), encrypt(), and save_image(). Do this as well for the encrypted football.png. Output is an image that appears in the current working directory. 

Known Bugs:
In the ImageEncrypter class, there's an attribute called self.image that is not present in the constructor. It's actually initialized in the open_image() method. It is necessary in order to access the image being modified in pixelate() and encrypt(). I would probably fix it by passing the image file already opened as one of the attributes in the constructor. That way, it's more accessible to the rest of the code that modifies it.

Partner Collaboration:
Did not work with a partner. Not applicable. 
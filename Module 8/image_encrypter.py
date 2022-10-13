# import your LFSR class for use in ImageEncrypter
from lfsr import LFSR
from PIL import Image


class ImageEncrypter:
    # initialize an ImageEncrypter object with an LFSR and image file name
    def __init__(self, lfsr: LFSR, file_name: str):
        self.lfsr = lfsr
        self.file_name = file_name

    # open the image specified by ‘file_name’ in constructor
    def open_image(self, file_name):
        self.image = Image.open(file_name)

    # converts the image to a 2D array of R, G, B triples
    def pixelate(self):
        self.open_image(self.file_name)
        self.pixels = self.image.load()

    # encrypts the 2D pixelated “image” returned from pixelate()
    def encrypt(self):
        # Retrieve number of rows and columns of pixel image
        (x, y) = self.image.size
        for row in range(x):
            for col in range(y):
                # Unpack existing RGB values and XOR with LSFR step
                r, g, b = self.pixels[row, col]
                r = int(self.lfsr.step(), 2) ^ r
                g = int(self.lfsr.step(), 2) ^ g
                b = int(self.lfsr.step(), 2) ^ b
                new_pixels = [r, g, b]
                # Pack "encrypted" pixels
                self.pixels[row, col] = tuple(new_pixels)

    # converts the encrypted 2D pixelated image into an image
    def save_image(self, file_name: str):
        # Name file <file_name>_transform.png
        (name, ext) = file_name.split(".")
        return self.image.save(f"{name}_transform.{ext}")


def main():
    # Initial encrypt of football.png
    lfsr = LFSR(seed="10011010", tap=5)
    encrypt_football = ImageEncrypter(lfsr=lfsr, file_name="football.png")
    encrypt_football.pixelate()
    encrypt_football.encrypt()
    encrypt_football.save_image("football.png")

    # Decrypt encrypted football.png
    lfsr2 = LFSR(seed="10011010", tap=5)
    decrypt_football = ImageEncrypter(lfsr=lfsr2, file_name="football_transform.png")
    decrypt_football.pixelate()
    decrypt_football.encrypt()
    decrypt_football.save_image("football_transform.png")


if __name__ == "__main__":
    main()

class LFSR:
    # Create an LFSR with initial state ‘seed’ and tap ‘tap’
    def __init__(self, seed: str, tap: int):
        self.seed = seed
        self.tap = tap

    # Return the bit at index ‘i’
    def bit(self, i: int):
        return self.seed[-i]

    # Execute one LFSR iteration and return new random number
    def step(self):
        tap = int(self.bit(self.tap))
        xor = int(self.bit(0)) ^ tap
        self.seed = self.seed[1:] + str(xor)
        return self.seed

    # Return string representation of the LFSR and new bit
    def __str__(self):
        return self.step().zfill(10) + " " + self.seed[-1]


# Executable code that invokes LFSR
def main():
    seeds = ["0110100111", "0100110010", "1001011101",
             "0001001100", "1010011101"]
    taps = [2, 8, 5, 1, 7]

    for i in range(len(seeds)):
        print(LFSR(seeds[i], taps[i]))


if __name__ == "__main__":
    main()

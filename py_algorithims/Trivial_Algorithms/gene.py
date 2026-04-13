class CompresedGene:

    def __init__(self, gene: str) -> None:
        self._compress(gene)

    
    def _compress(self, gene: str) -> None:
        self.bit_string: int = 1
        for nucleotides in gene.upper():
            self.bit_string <<= 2
            if nucleotides == 'A':
                self.bit_string |= 0b00
            
            elif nucleotides == 'C':
                self.bit_string |= 0b01
            
            elif nucleotides == 'G':
                self.bit_string |= 0b10
            
            elif nucleotides == 'T':
                self.bit_string |= 0b11

            else:
                return ValueError('invalid Nucleotides{}:'.format(nucleotides))
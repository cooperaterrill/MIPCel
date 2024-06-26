def bin2dec(num: str) -> int:
    return int(num,2)

def dec2bin(num: int, bits: int) -> str:
    return "{0:b}".format(num).zfill(bits)

def create_bin_repr(fields: list[int], sizes: list[int]) -> str:
    res = ""
    for pair in zip(fields,sizes):
        res = res + dec2bin(pair[0], pair[1])
    
    return res

class Instruction:
    def bin_repr(self) -> str:
        raise "Undefined method!"
    
class RType(Instruction):
    sizes = [6,5,5,5,5,6]   
    rt = int()
    rd = int()
    rs = int()
    operation = str()
    shamt = int()

    def bin_repr(self) -> str:
        opcode = 0
        funct = int()
        
        match self.operation:
            case 'ADD':
                funct = 32
            case 'SUB':
                funct = 34 
            case 'MULT':
                funct = 24
            case 'DIV':
                funct = 26
            case 'AND':
                funct = 36
            case 'OR':
                funct = 37
            case 'XOR':
                funct = 38
            case 'SLL':
                funct = 0
            case 'SRL':
                funct = 2
            case _:
                raise "Couldn't' match operation!"

                
        fields = [opcode, self.rs, self.rt, self.rd, self.shamt, funct]

        res = create_bin_repr(fields,self.sizes)
        #print(res)
        return res

    def __init__(self, rs, rt, rd, operation, shamt=0) -> None:
        self.rs = rs
        self.rt = rt
        self.rd = rd
        self.shamt = 0
        self.operation = operation
    
class IType(Instruction): 
    sizes = [6,5,5,16]
    operation = str()
    rs = int()
    rt = int()
    immd = int()

    def bin_repr(self) -> str:
        opcode = int()
        
        match self.operation:
            case 'ADDI':
                opcode = 8
            case 'ANDI':
                opcode = 12
            case 'ORI':
                opcode = 13
            case 'XORI':
                opcode = 14
            case 'BEQ':
                opcode = 4
            case 'BNE':
                opcode = 5
            case 'LW':
                opcode = 34
            case 'SW':
                opcode = 42
            case _:
                raise "Couldn't' match operation!"
        
        fields = [opcode,self.rs,self.rt,self.immd]
        res = create_bin_repr(fields,self.sizes)

        #print(res)
        return res
    
    def __init__(self, rs, rt, operation, immd) -> None:
        self.rs = rs
        self.rt = rt
        self.operation = operation
        self.immd = immd

class JType(Instruction):
    sizes = [6, 26]
    operation = str()
    immd = int()

    def bin_repr(self) -> str:
        opcode = int()
        match self.operation:
            case 'J':
                opcode = 2
            case _:
                raise "Couldn't match operation!"
                
        fields = [opcode, self.immd]
        res = create_bin_repr(fields, self.sizes) 
        
        #print(res)
        return res
    
    def __init__(self, operation, immd) -> None:
        self.operation = operation
        self.immd = immd
        
def main() -> None: 
    add = RType(rs=0,rt=8,rd=2,operation="ADD")
    xori = IType(rs=4,rt=9,operation="XORI",immd=384)
    xori2 = IType(rs=3,rt=13,operation="XORI",immd=1999)
    j = JType(operation='J', immd=420)
    print(bin2dec(add.bin_repr())) 
    print(bin2dec(xori.bin_repr()))
    print(bin2dec(j.bin_repr()))
    print(bin2dec(xori2.bin_repr()))

if __name__ == "__main__":
    main()
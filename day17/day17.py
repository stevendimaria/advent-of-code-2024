class Computer:

    def __init__(self):
        self.register, self.program = self.get_data()
        self.opcode_ptr = 0
        self.opcodes = {
            0: self.adv,
            1: self.bxl,
            2: self.bst,
            3: self.jnz,
            4: self.bxc,
            5: self.out,
            6: self.bdv,
            7: self.cdv
        }
        self.combo_ops = {
            0: 0,
            1: 1,
            2: 2,
            3: 3,
            4: self.register.get('A'),
            5: self.register.get('B'),
            6: self.register.get('C'),
            7: False
        }
        self.output = ''
        self.loops = 0

    def get_data(self):
        with open("input.txt", "r") as file:
            inp = file.read().split("\n")
        register = {}
        program = []
        for line in inp:
            if not line:
                continue
            name, val = line.split(': ')
            if line.startswith('Register'):
                register[name[-1]] = int(val)
            else:
                program = [int(n) for n in val.split(',')]

        return register, program

    def adv(self, op):
        coef = self.register['A'] // (2 ** self.combo_ops[op])
        self.register['A'] = coef

    def bxl(self, op):
        coef = self.register['B'] ^ op
        self.register['B'] = coef

    def bst(self, op):
        self.register['B'] = self.combo_ops[op] % 8

    def jnz(self, op):
        if self.register['A']==0:
            self.opcode_ptr += 2
        else:
            self.opcode_ptr = op

        self.loops += 1

    def bxc(self, op):
        coef = self.register['B'] ^ self.register['C']
        self.register['B'] = coef

    def out(self, op):
        coef = self.combo_ops[op] % 8
        self.output += f",{coef}"

    def bdv(self, op):
        coef = self.register['A'] // (2 ** self.combo_ops[op])
        self.register['B'] = coef

    def cdv(self, op):
        coef = self.register['A'] // (2 ** self.combo_ops[op])
        self.register['C'] = coef

    def refresh_combo_ops(self):
        self.combo_ops[4] = self.register.get('A')
        self.combo_ops[5] = self.register.get('B')
        self.combo_ops[6] = self.register.get('c')

    def run(self, verbose=False):
        while 0<=self.opcode_ptr<len(self.program):
            self.refresh_combo_ops()
            opcode = self.program[self.opcode_ptr]
            operand = self.program[self.opcode_ptr+1]
            operation = self.opcodes[self.program[self.opcode_ptr]]

            operation(self.program[self.opcode_ptr + 1])
            if verbose:
                print(
                      f"Opcode: {opcode}\n"
                      f"Operand: {operand}\n"
                      f"Opcode Ptr: {self.opcode_ptr}\n"
                      f"Operation Name: {operation.__name__}\n"
                      f"Registers: {self.register}\nOutput: {self.output}\n")
            if opcode!=3:
                self.opcode_ptr += 2

    def get_output(self):
        return self.output[1:]
def part1():
    computer = Computer()
    computer.run()
    return computer.get_output()

def part2():
    _c = Computer()
    target = ','.join([str(x) for x in _c.program])

    q = [(0, len(_c.program)-1)]
    while q:
        curr_a, rem = q.pop(0)
        for i in range(8):
            next_a = (curr_a << 3) + i

            computer = Computer()
            computer.register['A'] = next_a
            computer.run()

            ans = computer.get_output()
            if target==ans:
                return next_a
            elif str(computer.program[rem]) == ans[0]:
                q.append((next_a, rem - 1))
            else:
                continue

    return None


if __name__ == "__main__":
    print(f"Part 1 : {part1()}")
    print(f"Part 2 : {part2()}")

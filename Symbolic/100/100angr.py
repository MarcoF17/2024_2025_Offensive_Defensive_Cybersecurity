import angr, claripy

values_addr = 0
class HookConvert(angr.SimProcedure):
    
    def run(self):
        #commands to execute as replacement of the convert
        #we inject directly into the memory the symbolic bitvector
        
        global values_addr
        
        values = []
        for i in range(30):
            var = claripy.BVS(f"var_{i}", 8) #symbolic bitvector of size 8 bits with name var_{i}
            fixed = claripy.BVV(0, 8 * 7) #non-symbolic bitvector of value 0 and length 8*7 bits
            self.state.solver.add(var >= 0)
            self.state.solver.add(var <= 61)
            values.append(var)
            values.append(fixed)
        symbolic_bv = claripy.Concat(*values) # * means all the values of the array
        self.state.memory.store(values_addr, symbolic_bv)
        self.state.globals['symbolic_bv'] = symbolic_bv
        return 0
        

project = angr.Project('./challenge', auto_load_libs = False)
initial_state = project.factory.entry_state(args = ['./challenge', 'AAAAA'])
values_addr = project.loader.find_symbol('values').rebased_addr # = 0x400000 + 0x5080
project.hook_symbol('convert', HookConvert())
simulation = project.factory.simgr(initial_state)
simulation.explore(find = [0x400000 + 0x21C5], avoid = [0x400000 + 0x21CC]) # 0x400000 is the base of the binary ONLY in angr

if simulation.found:
    found = simulation.found[0]
    solution = found.solver.eval(found.globals['symbolic_bv'], cast_to = bytes)
    sol = b''
    for i in range(0, 30*8, 8):
        sol += solution[i].to_bytes(1, byteorder = 'little')
    print(sol) #these are the indexes of the symbols array


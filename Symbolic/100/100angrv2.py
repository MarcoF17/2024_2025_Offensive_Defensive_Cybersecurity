import angr, claripy, string

project = angr.Project('./challenge', auto_load_libs = False)
check_function_addr = project.loader.find_symbol('check').rebased_addr
initial_state = project.factory.blank_state(addr = check_function_addr)

#register setting
initial_state.regs.rsp = 0x600000 #any address will work

#memory setting
values_addr = project.loader.find_symbol('values').rebased_addr # = 0x400000 + 0x5080
values = []
for i in range(30):
    var = claripy.BVS(f"var_{i}", 8) #symbolic bitvector of size 8 bits with name var_{i}
    fixed = claripy.BVV(0, 8 * 7) #non-symbolic bitvector of value 0 and length 8*7 bits
    initial_state.solver.add(var >= 0)
    initial_state.solver.add(var <= 61)
    values.append(var)
    values.append(fixed)
symbolic_bv = claripy.Concat(*values) # * means all the values of the array
initial_state.memory.store(values_addr, symbolic_bv)
initial_state.globals['symbolic_bv'] = symbolic_bv

#parameters setting
#check() does not require any parameter

simulation = project.factory.simgr(initial_state)
simulation.explore(find = [0x400000 + 0x21C5], avoid = [0x400000 + 0x21CC]) # 0x400000 is the base of the binary ONLY in angr

if simulation.found:
    found = simulation.found[0]
    solution = found.solver.eval(found.globals['symbolic_bv'], cast_to = bytes)
    sol = ''
    symbols = string.digits + string.ascii_letters
    for i in range(0, 30*8, 8):
        sol += symbols[solution[i]]
    print(sol) #these are the indexes of the symbols array

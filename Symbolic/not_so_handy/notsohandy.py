import angr, claripy

project = angr.Project('./notsohandy', auto_load_libs = False)
bv = claripy.BVS('arg', 49 * 8) 
initial_state = project.factory.entry_state(args = ['./notsohandy', bv])

initial_state.solver.add(bv >= 64)
#initial_state.solver.add(bv <= 127)

simulation = project.factory.simulation_manager(initial_state)
simulation.explore(find = [0x141F + 0x400000], avoid = [0x1430 + 0x400000])
print(f"simulation: {simulation}, active: {simulation.active}")

if simulation.found:
    found = simulation.found[0]
    print(f"solution: {found.solver.eval(bv, cast_to=bytes)}")

else:
    print("FAIL")
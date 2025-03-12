import claripy
import angr

proj = angr.Project('/home/marcolino/OneDrive/MASTER/Off-Def/Challenges/notsohandy')
sm = proj.factory.simgr()

arg1 = (claripy.BVS('arg1', 45 * 8))
argv = ['./notsohandy', arg1]

state = proj.factory.entry_state(args=argv)
sim = proj.factory.simulation_manager(state)

print(sim, sim.active)
sim.explore(find = [0x141F + 0x400000])
print('BEFORE IF')

if len(sim.found) > 0:
    print('Success')
    found = simgr.found[0]
    print(found.solver.eval(argv[1]))
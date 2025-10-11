# 2024_2025_Offensive_Defensive_Cybersecurity

Course at Politecnico di Milano based on hands-on laboratories on capture-the-flag challenges on different topic about exploiting and mitigating binary vulnerabilities in every-day application.
Challenges are grouped in the following categories:
- Shellcoding
- Mitigations
- Reversing
- Symbolic execution
- Heap exploitation
- Return Oriented Programming
- Kernel vulnerabilities
- Malware
- Race conditions

## Shellcoding
These challenges consist in exploiting a buffer overflow vulnerabilty to execute a custom shellcode. In some cases, the original code of the application already contains a function that prints the flag, so it is enough to overwrite the savedEIP on the stack with the address of that function. In other cases, it is required to write a shellcode to perform the execve("/bin/sh\0") or the open-read-write chain of syscalls to get the flag.

## Mitigations
Pretty similar the the aforementioned challenges but this time some techniques to mitigate the exploitation are implemented, like stack-canary, ASRL, PIE, non-executable-stack.

## Reversing
In this section, the challenges are based on the ability to reverse-engineer an executable file with tools like Ghidra or IDA.

## Symbolic Execution
It is required to run the applications multiple times using z3 or angr to build the flag.

## Heap Exploitation
Using an old version of the libc, these challenges allow to exploit heap management vulnerabilities like double-free or overlapping chunks.

## Return Oriented Programming
Same goal as shellcoding challenges but this time a ROP-chain is required to prepare the system to execute the execve("/bin/sh\0") syscall.

## Kernel vulnerabilities
In this case there are some vulnerabilities in the kernel of the operating system that allow to "hijack" the default syscalls.

## Malware
Two different categories of malware are considered in this section:
- packing -> the "real" code of the application is packed and the decryption is only made at runtime
- code-on-demand -> the vulnerable code is delivered to the application through the sockets
In both cases it is necessary to use tools like gdb to control the flow of instructions execution <br> to get the actual malicious code.

## Race conditions
Bugs in the file system or in process management must be exploiting to get the flags.


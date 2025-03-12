from libdebug import debugger
import string

def sleep_cb(t, handler):
    #print("SLEEP")
    #print(f"Old reg value: {t.regs.rdi}")
    t.regs.rdi = 0x00
    #print(f"New reg value: {t.regs.rdi}")
    
d = debugger("./slow_provola")

flag = "$" * 68
real_flag = ""

m1 = m2 = m3 = m4 = m5 = m6 = m7 = m8 = m9 = m10 = m11 = m12 = m13 = m14 = m15 = m16 = m17 = m18 = m19 = m20 = m21 = m22 = m23 = m24 = m25 = m26 = m27 = m28 = m29 = m30 = \
    m31 = m32 = m33 = m34 = m35 = m36 = m37 = m38 = m39 = m40 = m41 = m42 = m43 = m44 = m45 = m46 = m47 = m48 = m49 = m50 = m51 = m52 = m53 = m54 = m55 = m56 = m57 = m58 = m59 = m60 = \
        m61 = m62 = m63 = m64 = m65 = m66 = m67 = m68 = 0

for i in range(68):
    for c in string.printable:
        new_flag = flag[:i] + c + flag[i+1:]
        #print(f"Tring: {new_flag}")
    
        r = d.run()

        #sleep breakpoints in check_password
        d.bp(0x1A7A, file = "slow_provola", callback = sleep_cb)
        d.bp(0x1B22, file = "slow_provola", callback = sleep_cb)
        d.bp(0x1BCA, file = "slow_provola", callback = sleep_cb)
        d.bp(0x1C72, file = "slow_provola", callback = sleep_cb)
        d.bp(0x1D1A, file = "slow_provola", callback = sleep_cb)
        d.bp(0x1DC2, file = "slow_provola", callback = sleep_cb)
        d.bp(0x1E6A, file = "slow_provola", callback = sleep_cb)
        d.bp(0x1F12, file = "slow_provola", callback = sleep_cb)
        d.bp(0x1FBA, file = "slow_provola", callback = sleep_cb)
        d.bp(0x2062, file = "slow_provola", callback = sleep_cb)
        d.bp(0x210A, file = "slow_provola", callback = sleep_cb)
        d.bp(0x21B2, file = "slow_provola", callback = sleep_cb)
        d.bp(0x225A, file = "slow_provola", callback = sleep_cb)
        d.bp(0x2302, file = "slow_provola", callback = sleep_cb)
        d.bp(0x23AA, file = "slow_provola", callback = sleep_cb)
        d.bp(0x2452, file = "slow_provola", callback = sleep_cb)
        d.bp(0x24FA, file = "slow_provola", callback = sleep_cb)
        d.bp(0x25A2, file = "slow_provola", callback = sleep_cb)
        d.bp(0x264A, file = "slow_provola", callback = sleep_cb)
        d.bp(0x26F2, file = "slow_provola", callback = sleep_cb)
        d.bp(0x279A, file = "slow_provola", callback = sleep_cb)
        d.bp(0x2842, file = "slow_provola", callback = sleep_cb)
        d.bp(0x28EA, file = "slow_provola", callback = sleep_cb)
        d.bp(0x2992, file = "slow_provola", callback = sleep_cb)
        d.bp(0x2A3A, file = "slow_provola", callback = sleep_cb)
        d.bp(0x2AE2, file = "slow_provola", callback = sleep_cb)
        d.bp(0x2B8A, file = "slow_provola", callback = sleep_cb)
        d.bp(0x2C32, file = "slow_provola", callback = sleep_cb)
        d.bp(0x2CDA, file = "slow_provola", callback = sleep_cb)
        d.bp(0x2D82, file = "slow_provola", callback = sleep_cb)
        d.bp(0x2E2A, file = "slow_provola", callback = sleep_cb)
        d.bp(0x2ED2, file = "slow_provola", callback = sleep_cb)
        d.bp(0x2F7A, file = "slow_provola", callback = sleep_cb)
        d.bp(0x3022, file = "slow_provola", callback = sleep_cb)
        d.bp(0x30CA, file = "slow_provola", callback = sleep_cb)
        d.bp(0x3172, file = "slow_provola", callback = sleep_cb)
        d.bp(0x321A, file = "slow_provola", callback = sleep_cb)
        d.bp(0x32C2, file = "slow_provola", callback = sleep_cb)
        d.bp(0x336A, file = "slow_provola", callback = sleep_cb)
        d.bp(0x3412, file = "slow_provola", callback = sleep_cb)
        d.bp(0x34BA, file = "slow_provola", callback = sleep_cb)
        d.bp(0x3562, file = "slow_provola", callback = sleep_cb)
        d.bp(0x360A, file = "slow_provola", callback = sleep_cb)
        d.bp(0x36B2, file = "slow_provola", callback = sleep_cb)
        d.bp(0x375A, file = "slow_provola", callback = sleep_cb)
        d.bp(0x3802, file = "slow_provola", callback = sleep_cb)
        d.bp(0x38AA, file = "slow_provola", callback = sleep_cb)
        d.bp(0x3952, file = "slow_provola", callback = sleep_cb)
        d.bp(0x39FA, file = "slow_provola", callback = sleep_cb)
        d.bp(0x3AA2, file = "slow_provola", callback = sleep_cb)
        d.bp(0x3B4A, file = "slow_provola", callback = sleep_cb)
        d.bp(0x3BE3, file = "slow_provola", callback = sleep_cb)
        d.bp(0x3C7C, file = "slow_provola", callback = sleep_cb)
        d.bp(0x3D15, file = "slow_provola", callback = sleep_cb)
        d.bp(0x3DAE, file = "slow_provola", callback = sleep_cb)
        d.bp(0x3E47, file = "slow_provola", callback = sleep_cb)
        d.bp(0x3EE0, file = "slow_provola", callback = sleep_cb)
        d.bp(0x3F79, file = "slow_provola", callback = sleep_cb)
        d.bp(0x4012, file = "slow_provola", callback = sleep_cb)
        d.bp(0x40AB, file = "slow_provola", callback = sleep_cb)
        d.bp(0x4144, file = "slow_provola", callback = sleep_cb)
        d.bp(0x41DD, file = "slow_provola", callback = sleep_cb)
        d.bp(0x4276, file = "slow_provola", callback = sleep_cb)
        d.bp(0x430F, file = "slow_provola", callback = sleep_cb)
        d.bp(0x43A8, file = "slow_provola", callback = sleep_cb)
        d.bp(0x4441, file = "slow_provola", callback = sleep_cb)
        d.bp(0x44DA, file = "slow_provola", callback = sleep_cb)

        #sleep breakpoints in main    
        d.bp(0x45AF, file = "slow_provola", callback = sleep_cb)
        d.bp(0x45C8, file = "slow_provola", callback = sleep_cb)
        d.bp(0x45E1, file = "slow_provola", callback = sleep_cb)
        d.bp(0x45FA, file = "slow_provola", callback = sleep_cb)

        #for loops breakpoint
        for1 = d.bp(0x1A5E, file = "slow_provola")
        for2 = d.bp(0x1B06, file = "slow_provola")
        for3 = d.bp(0x1BAE, file = "slow_provola")
        for4 = d.bp(0x1C56, file = "slow_provola")
        for5 = d.bp(0x1CFE, file = "slow_provola")
        for6 = d.bp(0x1DA6, file = "slow_provola")
        for7 = d.bp(0x1E4E, file = "slow_provola")
        for8 = d.bp(0x1EF6, file = "slow_provola")
        for9 = d.bp(0x1F9E, file = "slow_provola")
        for10 = d.bp(0x2046, file = "slow_provola")
        for11 = d.bp(0x20EE, file = "slow_provola")
        for12 = d.bp(0x2196, file = "slow_provola")
        for13 = d.bp(0x223E, file = "slow_provola")
        for14 = d.bp(0x22E6, file = "slow_provola")
        for15 = d.bp(0x238E, file = "slow_provola")
        for16 = d.bp(0x2436, file = "slow_provola")
        for17 = d.bp(0x24DE, file = "slow_provola")
        for18 = d.bp(0x2586, file = "slow_provola")
        for19 = d.bp(0x262E, file = "slow_provola")
        for20 = d.bp(0x26D6, file = "slow_provola")
        for21 = d.bp(0x277E, file = "slow_provola")
        for22 = d.bp(0x2826, file = "slow_provola")
        for23 = d.bp(0x28CE, file = "slow_provola")
        for24 = d.bp(0x2976, file = "slow_provola")
        for25 = d.bp(0x2A1E, file = "slow_provola")
        for26 = d.bp(0x2AC6, file = "slow_provola")
        for27 = d.bp(0x2B6E, file = "slow_provola")
        for28 = d.bp(0x2C16, file = "slow_provola")
        for29 = d.bp(0x2CBE, file = "slow_provola")
        for30 = d.bp(0x2D66, file = "slow_provola")
        for31 = d.bp(0x2E0E, file = "slow_provola")
        for32 = d.bp(0x2EB6, file = "slow_provola")
        for33 = d.bp(0x2F5E, file = "slow_provola")
        for34 = d.bp(0x3006, file = "slow_provola")
        for35 = d.bp(0x30AE, file = "slow_provola")
        for36 = d.bp(0x3156, file = "slow_provola")
        for37 = d.bp(0x31FE, file = "slow_provola")
        for38 = d.bp(0x32A6, file = "slow_provola")
        for39 = d.bp(0x334E, file = "slow_provola")
        for40 = d.bp(0x33F6, file = "slow_provola")
        for41 = d.bp(0x349E, file = "slow_provola")
        for42 = d.bp(0x3546, file = "slow_provola")
        for43 = d.bp(0x35EE, file = "slow_provola")
        for44 = d.bp(0x3696, file = "slow_provola")
        for45 = d.bp(0x373E, file = "slow_provola")
        for46 = d.bp(0x37E6, file = "slow_provola")
        for47 = d.bp(0x388E, file = "slow_provola")
        for48 = d.bp(0x3936, file = "slow_provola")
        for49 = d.bp(0x39DE, file = "slow_provola")
        for50 = d.bp(0x3A86, file = "slow_provola")
        for51 = d.bp(0x3B2E, file = "slow_provola")
        for52 = d.bp(0x3BCD, file = "slow_provola")
        for53 = d.bp(0x3C66, file = "slow_provola")
        for54 = d.bp(0x3CFF, file = "slow_provola")
        for55 = d.bp(0x3D98, file = "slow_provola")
        for56 = d.bp(0x3E31, file = "slow_provola")
        for57 = d.bp(0x3ECA, file = "slow_provola")
        for58 = d.bp(0x3F63, file = "slow_provola")
        for59 = d.bp(0x3FFC, file = "slow_provola")
        for60 = d.bp(0x4095, file = "slow_provola")
        for61 = d.bp(0x412E, file = "slow_provola")
        for62 = d.bp(0x41C7, file = "slow_provola")
        for63 = d.bp(0x4260, file = "slow_provola")
        for64 = d.bp(0x42F9, file = "slow_provola")
        for65 = d.bp(0x4392, file = "slow_provola")
        for66 = d.bp(0x442B, file = "slow_provola")
        for67 = d.bp(0x44C4, file = "slow_provola")
        for68 = d.bp(0x455D, file = "slow_provola")

        d.cont()
        
        r.recvuntil(b'password')
        r.sendline(new_flag.encode())
        
        d.wait()
        d.kill()
        
        if for1.hit_count > m1:
            m1 = for1.hit_count
            real_flag += new_flag[0]
            print(f"New flag1: {real_flag}")
            break
            
        if for2.hit_count > m2:
            m2 = for2.hit_count
            real_flag += new_flag[1]
            print(f"New flag2: {real_flag}")
            break   
 
        if for3.hit_count > m3:
            m3 = for3.hit_count
            real_flag += new_flag[2]
            print(f"New flag3: {real_flag}")
            break      
        
        if for4.hit_count > m4:
            m4 = for4.hit_count
            real_flag += new_flag[3]
            print(f"New flag4: {real_flag}")
            break
        
        if for5.hit_count > m5:
            m5 = for5.hit_count
            real_flag += new_flag[4]
            print(f"New flag5: {real_flag}")
            break     
        
        if for6.hit_count > m6:
            m6 = for6.hit_count
            real_flag += new_flag[5]
            print(f"New flag6: {real_flag}")
            break            

        if for7.hit_count > m7:
            m7 = for7.hit_count
            real_flag += new_flag[6]
            print(f"New flag7: {real_flag}")
            break  

        if for8.hit_count > m8:
            m8 = for8.hit_count
            real_flag += new_flag[7]
            print(f"New flag8: {real_flag}")
            break  
        
        if for9.hit_count > m9:
            m9 = for9.hit_count
            real_flag += new_flag[8]
            print(f"New flag9: {real_flag}")
            break  

        if for10.hit_count > m10:
            m10 = for10.hit_count
            real_flag += new_flag[9]
            print(f"New flag10: {real_flag}")
            break  

        if for11.hit_count > m11:
            m11 = for11.hit_count
            real_flag += new_flag[10]
            print(f"New flag11: {real_flag}")
            break  

        if for12.hit_count > m12:
            m12 = for12.hit_count
            real_flag += new_flag[11]
            print(f"New flag12: {real_flag}")
            break  

        if for13.hit_count > m13:
            m13 = for13.hit_count
            real_flag += new_flag[12]
            print(f"New flag13: {real_flag}")
            break  

        if for14.hit_count > m14:
            m14 = for14.hit_count
            real_flag += new_flag[13]
            print(f"New flag14: {real_flag}")
            break  

        if for15.hit_count > m15:
            m15 = for15.hit_count
            real_flag += new_flag[14]
            print(f"New flag15: {real_flag}")
            break  

        if for16.hit_count > m16:
            m16 = for16.hit_count
            real_flag += new_flag[15]
            print(f"New flag16: {real_flag}")
            break  

        if for17.hit_count > m17:
            m17 = for17.hit_count
            real_flag += new_flag[16]
            print(f"New flag17: {real_flag}")
            break  

        if for18.hit_count > m18:
            m18 = for18.hit_count
            real_flag += new_flag[17]
            print(f"New flag18: {real_flag}")
            break  

        if for19.hit_count > m19:
            m19 = for19.hit_count
            real_flag += new_flag[18]
            print(f"New flag19: {real_flag}")
            break  

        if for20.hit_count > m20:
            m20 = for20.hit_count
            real_flag += new_flag[19]
            print(f"New flag20: {real_flag}")
            break  

        if for21.hit_count > m21:
            m21 = for21.hit_count
            real_flag += new_flag[20]
            print(f"New flag21: {real_flag}")
            break  

        if for22.hit_count > m22:
            m22 = for22.hit_count
            real_flag += new_flag[21]
            print(f"New flag22: {real_flag}")
            break  

        if for23.hit_count > m23:
            m23 = for23.hit_count
            real_flag += new_flag[22]
            print(f"New flag23: {real_flag}")
            break  

        if for24.hit_count > m24:
            m24 = for24.hit_count
            real_flag += new_flag[23]
            print(f"New flag24: {real_flag}")
            break  

        if for25.hit_count > m25:
            m25 = for25.hit_count
            real_flag += new_flag[24]
            print(f"New flag25: {real_flag}")
            break  

        if for26.hit_count > m26:
            m26 = for26.hit_count
            real_flag += new_flag[25]
            print(f"New flag26: {real_flag}")
            break  

        if for27.hit_count > m27:
            m27 = for27.hit_count
            real_flag += new_flag[26]
            print(f"New flag27: {real_flag}")
            break  

        if for28.hit_count > m28:
            m28 = for28.hit_count
            real_flag += new_flag[27]
            print(f"New flag28: {real_flag}")
            break  

        if for29.hit_count > m29:
            m29 = for29.hit_count
            real_flag += new_flag[28]
            print(f"New flag29: {real_flag}")
            break  

        if for30.hit_count > m30:
            m30 = for30.hit_count
            real_flag += new_flag[29]
            print(f"New flag30: {real_flag}")
            break  

        if for31.hit_count > m31:
            m31 = for31.hit_count
            real_flag += new_flag[30]
            print(f"New flag31: {real_flag}")
            break  

        if for32.hit_count > m32:
            m32 = for32.hit_count
            real_flag += new_flag[31]
            print(f"New flag32: {real_flag}")
            break  

        if for33.hit_count > m33:
            m33 = for33.hit_count
            real_flag += new_flag[32]
            print(f"New flag33: {real_flag}")
            break  

        if for34.hit_count > m34:
            m34 = for34.hit_count
            real_flag += new_flag[33]
            print(f"New flag34: {real_flag}")
            break  

        if for35.hit_count > m35:
            m35 = for35.hit_count
            real_flag += new_flag[34]
            print(f"New flag35: {real_flag}")
            break  

        if for36.hit_count > m36:
            m36 = for36.hit_count
            real_flag += new_flag[35]
            print(f"New flag36: {real_flag}")
            break  

        if for37.hit_count > m37:
            m37 = for37.hit_count
            real_flag += new_flag[36]
            print(f"New flag37: {real_flag}")
            break  

        if for38.hit_count > m38:
            m38 = for38.hit_count
            real_flag += new_flag[37]
            print(f"New flag38: {real_flag}")
            break  

        if for39.hit_count > m39:
            m39 = for39.hit_count
            real_flag += new_flag[38]
            print(f"New flag39: {real_flag}")
            break  

        if for40.hit_count > m40:
            m40 = for40.hit_count
            real_flag += new_flag[39]
            print(f"New flag40: {real_flag}")
            break  

        if for41.hit_count > m41:
            m41 = for41.hit_count
            real_flag += new_flag[40]
            print(f"New flag41: {real_flag}")
            break  

        if for42.hit_count > m42:
            m42 = for42.hit_count
            real_flag += new_flag[41]
            print(f"New flag42: {real_flag}")
            break  

        if for43.hit_count > m43:
            m43 = for43.hit_count
            real_flag += new_flag[42]
            print(f"New flag43: {real_flag}")
            break  

        if for44.hit_count > m44:
            m44 = for44.hit_count
            real_flag += new_flag[43]
            print(f"New flag44: {real_flag}")
            break  

        if for45.hit_count > m45:
            m45 = for45.hit_count
            real_flag += new_flag[44]
            print(f"New flag45: {real_flag}")
            break  

        if for46.hit_count > m46:
            m46 = for46.hit_count
            real_flag += new_flag[45]
            print(f"New flag46: {real_flag}")
            break  

        if for47.hit_count > m47:
            m47 = for47.hit_count
            real_flag += new_flag[46]
            print(f"New flag47: {real_flag}")
            break  

        if for48.hit_count > m48:
            m48 = for48.hit_count
            real_flag += new_flag[47]
            print(f"New flag48: {real_flag}")
            break  

        if for49.hit_count > m49:
            m49 = for49.hit_count
            real_flag += new_flag[48]
            print(f"New flag49: {real_flag}")
            break  

        if for50.hit_count > m50:
            m50 = for50.hit_count
            real_flag += new_flag[49]
            print(f"New flag50: {real_flag}")
            break  

        if for51.hit_count > m51:
            m51 = for51.hit_count
            real_flag += new_flag[50]
            print(f"New flag51: {real_flag}")
            break  

        if for52.hit_count > m52:
            m52 = for52.hit_count
            real_flag += new_flag[51]
            print(f"New flag52: {real_flag}")
            break  

        if for53.hit_count > m53:
            m53 = for53.hit_count
            real_flag += new_flag[52]
            print(f"New flag53: {real_flag}")
            break  

        if for54.hit_count > m54:
            m54 = for54.hit_count
            real_flag += new_flag[53]
            print(f"New flag54: {real_flag}")
            break  

        if for55.hit_count > m55:
            m55 = for55.hit_count
            real_flag += new_flag[54]
            print(f"New flag55: {real_flag}")
            break  

        if for56.hit_count > m56:
            m56 = for56.hit_count
            real_flag += new_flag[55]
            print(f"New flag56: {real_flag}")
            break  

        if for57.hit_count > m57:
            m57 = for57.hit_count
            real_flag += new_flag[56]
            print(f"New flag57: {real_flag}")
            break  

        if for58.hit_count > m58:
            m58 = for58.hit_count
            real_flag += new_flag[57]
            print(f"New flag58: {real_flag}")
            break  

        if for59.hit_count > m59:
            m59 = for59.hit_count
            real_flag += new_flag[58]
            print(f"New flag59: {real_flag}")
            break  

        if for60.hit_count > m60:
            m60 = for60.hit_count
            real_flag += new_flag[59]
            print(f"New flag60: {real_flag}")
            break  

        if for61.hit_count > m61:
            m61 = for61.hit_count
            real_flag += new_flag[60]
            print(f"New flag61: {real_flag}")
            break  

        if for62.hit_count > m62:
            m62 = for62.hit_count
            real_flag += new_flag[61]
            print(f"New flag62: {real_flag}")
            break  

        if for63.hit_count > m63:
            m63 = for63.hit_count
            real_flag += new_flag[62]
            print(f"New flag63: {real_flag}")
            break  

        if for64.hit_count > m64:
            m64 = for64.hit_count
            real_flag += new_flag[63]
            print(f"New flag64: {real_flag}")
            break  

        if for65.hit_count > m65:
            m65 = for65.hit_count
            real_flag += new_flag[64]
            print(f"New flag65: {real_flag}")
            break  

        if for66.hit_count > m66:
            m66 = for66.hit_count
            real_flag += new_flag[65]
            print(f"New flag66: {real_flag}")
            break  

        if for67.hit_count > m67:
            m67 = for67.hit_count
            real_flag += new_flag[66]
            print(f"New flag67: {real_flag}")
            break  

        if for68.hit_count > m68:
            m68 = for68.hit_count
            real_flag += new_flag[67]
            print(f"New flag68: {real_flag}")
            break  
        

print(f"FLAG: {real_flag}")
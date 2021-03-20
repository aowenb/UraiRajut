def urai(n):
    urai = [] # temporary list untuk stack values
    for i in range(0,len(n)): # iterasi printing untuk panjang input
        urai.append(n[0:i+1]) # append semua urutan printing
    return ''.join(urai) # join list untuk print string dan tidak list

import itertools as it

def rajut(n):
    x = len(n)
    counter_len = 0 # counter untuk panjang input
    counter = 0 # counter untuk berberapa kali iterasi tambahan
    for i in range(1,len(n)):
        counter_len = counter_len + i # untuk iterasi 1 + 2 + 3 + 4 ... etc
        counter = counter + 1 # untuk isi counter interasi tambahan
        if counter_len == len(n): # jika iterasi counter_len sudah terpenuhi berhenti
            break
    return n[counter_len - counter::] 
    # jika sudah tau panjang input sebelum di urai, kita bisa cari index untuk mulai print


print(len('ppupurpurwpurwapurwadpurwadhpurwadhipurwadhikpurwadhika'))

print('\n')
print(urai('code'))
print(urai('python'))
print(urai('purwadhika'))
print('\n')
print(rajut('ccocodcode'))
print(rajut('ppypytpythpythopython'))
print(rajut('ppupurpurwpurwapurwadpurwadhpurwadhipurwadhikpurwadhika'))
#LRU
def MRU(main_mem,cache,rep_cache,page_fault,hit):
    for i in range(0,len(cache)):
        cache[i]=main_mem[i]
        page_fault=page_fault+1
        rep_cache[i]=rep_cache[i]+1


    for i in range(len(cache),len(main_mem)):
        if(main_mem[i] in cache):
            hit = hit+1
            c=cache.index(main_mem[i])
            rep_cache[c]=max(rep_cache)+1
        elif(main_mem[i] not in cache):
            page_fault = page_fault + 1
            cache[rep_cache.index(max(rep_cache))]=main_mem[i]
            rep_cache[rep_cache.index(max(rep_cache))]=max(rep_cache)+1
    print("MRU")
    print("Page Faults:",page_fault)
    print("Total Hits:",hit)

def LRU(main_mem,cache,rep_cache,page_fault,hit):
    for i in range(0,len(cache)):
        cache[i]=main_mem[i]
        page_fault=page_fault+1
        rep_cache[i]=rep_cache[i]+1


    for i in range(len(cache),len(main_mem)):
        if(main_mem[i] in cache):
            hit=hit+1
            c=cache.index(main_mem[i])
            rep_cache[c]=max(rep_cache)+1
        elif( main_mem[i] not in cache):
            cache[rep_cache.index(min(rep_cache))]=main_mem[i]
            rep_cache[rep_cache.index(min(rep_cache))]=max(rep_cache)+1
            page_fault = page_fault+1
    print("LRU")
    print("Page Faults:",page_fault)
    print("Total Hits:",hit)

def FIFO(main_mem,cache,pointer,page_fault,hit):
    for i in range(0, len(cache)):
        cache[i] = main_mem[i]
        page_fault +=1

    for i in range(len(cache),len(main_mem)):
        if main_mem[i] in cache:
            hit += 1
        else:
            page_fault+= 1
            cache[pointer]=main_mem[i]
            pointer=(pointer+1)%4
    
    print("FIFO")
    print("Page Faults:",page_fault)
    print("Total Hits:",hit)


def min_occur(main_mem,cache):
    c=0
    lis=list()
    for i in range(0,len(cache)):
        for j in main_mem:
            if cache[i]==j:
                c=c+1
        lis.insert(i,c)
        c=0
    return(lis)
def Optimal(main_mem,cache,page_fault,hit):
    for i in range(0,len(cache)):
        cache[i]=main_mem[i]
        page_fault = page_fault+1


    for i in range(len(cache),len(main_mem)):
        if(main_mem[i] in cache):
            hit=hit+1
        elif(main_mem[i] not in cache):
            l=min_occur(main_mem[i:],cache)
            cache[l.index(min(l))]=main_mem[i]
            page_fault=page_fault+1
    print("Optimal")
    print("Page Faults:",page_fault)
    print("Total Hits:",hit)

main_mem=[7,0,1,2,0,3,0,4,2,3,0,3,2,3]
cache=[-1]*4
rep_cache=[1,2,3,4]
pointer=0
page_fault=0
hit=0

MRU(main_mem,cache,rep_cache,page_fault,hit)
print("\n")
LRU(main_mem,cache,rep_cache,page_fault,hit)
print("\n")
FIFO(main_mem,cache,pointer,page_fault,hit)
print("\n")
Optimal(main_mem,cache,page_fault,hit)


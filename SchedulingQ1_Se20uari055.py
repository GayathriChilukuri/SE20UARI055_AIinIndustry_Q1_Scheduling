def fcfs(at,bt):
    wtd = {}
    tat = []
    wt = []
    d = {}
    for i in range(len(at)):
        d[at[i]] = bt[i]
    atsort = sorted(at)
    btsort = []
    for i in atsort:
        btsort.append(d[i])
    present = 0
    for i in range(len(atsort)):
        present = present + btsort[i]
        wtd[atsort[i]] = present - atsort[i] - btsort[i]
    for i in at:
        wt.append(wtd[i])
    for i in range(len(wt)):
        tat.append(wt[i]+bt[i])
    return wt,tat


def sjf(at, bt):
    wt = [0] * len(at)
    tat = [0] * len(at)
    n = len(at)
    completed = [False] * n
    total_time = 0
    remaining_bt = bt.copy()
    while True:
        min_bt = float('inf')
        shortest = -1
        for i in range(n):
            if not completed[i] and at[i] <= total_time and remaining_bt[i] < min_bt:
                min_bt = remaining_bt[i]
                shortest = i
        if shortest == -1:
            break
        completed[shortest] = True
        total_time += bt[shortest]
        wt[shortest] = total_time - at[shortest] - bt[shortest]
        tat[shortest] = wt[shortest] + bt[shortest]
    return wt, tat


def ps(at, bt, priority):
    n = len(at)
    wt = [0] * n
    tat = [0] * n
    processes = [(i, at[i], bt[i], priority[i]) for i in range(n)]
    processes.sort(key=lambda x: x[3])
    total_time = 0
    for i in range(n):
        process_id, arrival_time, burst_time, _ = processes[i]
        if arrival_time > total_time:
            total_time = arrival_time
        wt[process_id] = total_time - arrival_time
        total_time += burst_time
        tat[process_id] = wt[process_id] + burst_time
    return wt, tat


def rr(at, bt, quantum):
    n = len(at)
    wt = [0] * n
    tat = [0] * n
    remaining_bt = bt.copy()
    time = 0
    while any(remaining_bt):
        for i in range(n):
            if remaining_bt[i] > 0:
                if remaining_bt[i] <= quantum:
                    time += remaining_bt[i]
                    wt[i] = time - at[i] - bt[i]
                    remaining_bt[i] = 0
                else:
                    time += quantum
                    remaining_bt[i] -= quantum
                tat[i] = wt[i] + bt[i]
    return wt, tat

def avgwt(wt):
    return sum(wt)/len(wt)

def avgtat(tat):
    return sum(tat)/len(tat)

# input
at = [0,4,5,6]
bt = [24,3,3,12]
p = [3,1,4,2]

# fcfs
wt,tat = fcfs(at,bt)
wtfcfs = avgwt(wt)
tatfcfs = avgtat(tat)

# sjf
wt,tat = sjf(at,bt)
wtsjf = avgwt(wt)
tatsjf = avgtat(tat)

# ps
wt,tat = ps(at,bt,p)
wtps = avgwt(wt)
tatps = avgtat(tat)

# rr
wt,tat = rr(at,bt,4)
wtrr = avgwt(wt)
tatrr = avgtat(tat)

print([wtfcfs,wtsjf,wtps,wtrr])
print([tatfcfs,tatsjf,tatps,tatrr])

# for this question by looking at the average waiting time, we can tell that round robin 
# is the most efficient scheduling method to solve this problem
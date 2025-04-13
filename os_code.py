# Quantum Time (QT) calculation

def calculate_quantum_time(SRQ):
    n = len(SRQ)     # Number of processes in Sorted Ready Queue
    index = 0.8 * n     # Getting index for 80th percentile

    if (index % 1 != 0):    #If index is not an integer, round to nearest number
        index = round(index)
        
    QT = SRQ[index - 1]     # Quantum time
    return QT

Queue = [12, 45, 67, 23, 89, 34, 56, 78, 90, 10, 350, 101]
print("Queue: ", Queue)

SRQ = sorted(Queue)
print("SRQ: ", SRQ)

QT = calculate_quantum_time(SRQ)
print("Quantum Time: ",QT)
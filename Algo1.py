import queue


# queue set up steps 1-3
class processes:
    def __init__(self, burst, id):
        self.burst = burst
        self.id = id
        def __str__(self):
            return f"{self.burst}({self.id})"
process = processes(100,314682)

srq = queue.PriorityQueue()
srq.put(process.burst, process.id)


def E_Round_robin(srq):

    # processing
    flag = True
    while(flag == True):
        # qt calculations steps 4/5
        number_process = srq.qsize()
        qt = QT_calculation(srq)
        #step 7
        executing = srq.get()
        print("executing first process: " + executing)
        #step 31/32
        if (executing.burst > qt):    
            executing.burst -= qt
            srq.put(executing.burst, executing.id)
            #step 9-13
            if (executing.burst <= (qt/3)):
                srq.get()
                #step 24/26
                if (srq.qsize() == 0):
                    flag = False
                
                #step 14-23
                else:
                    fbt = srq.get()
                    if (fbt <= (qt/3)):
                        srq.put(executing.burst, executing.id)

                    else:
                        #step 24/26
                        if (srq.qsize() == 0):
                            flag = False

        else:
            #step 24/26
            if (srq.qsize() == 0):
                flag = False
            





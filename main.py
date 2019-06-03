import sys
from Simulator import Simulator
    
if __name__ == "__main__":
    the_lambda = 1

    for scheduler in range(1,6):
        if scheduler is 1:
            print("Running FCFS Scheduler")
            while the_lambda < 31:
                sim = Simulator(scheduler, the_lambda, .06, 0, 10000)
                sim.run()
                sim.generateReport()
                the_lambda += 1
            the_lambda = 1

        elif scheduler is 2:
            print("Running SRTF Scheduler ")
            while the_lambda < 31:
                sim = Simulator(scheduler, the_lambda, .06, 0, 10000)
                sim.run()
                sim.generateReport()
                the_lambda += 1
            the_lambda = 1

        elif scheduler is 3:
            print("Running HRRN Scheduler")
            while the_lambda < 31:
                sim = Simulator(scheduler, the_lambda, .06, 0, 10000)
                sim.run()
                sim.generateReport()
                the_lambda += 1
            the_lambda = 1

        elif scheduler is 4:
            print("Running RR Scheduler")
            while the_lambda < 31:
                sim = Simulator(scheduler, the_lambda, .06, .01, 10000)
                sim.run()
                sim.generateReport()
                the_lambda += 1
            the_lambda = 1

        elif scheduler is 5:
            print("Running RR Scheduler")
            while the_lambda < 31:
                sim = Simulator(scheduler-1, the_lambda, .06, .2, 10000)
                sim.run()
                sim.generateReport()
                the_lambda += 1
            the_lambda = 1

        else:
            print("Invalid input.")
        scheduler += 1
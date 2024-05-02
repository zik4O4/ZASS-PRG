
    # To run Jarvis
import multiprocessing


def startVA():
        # Code for process 1
        print("Process 1 is running.")
        from main import startVA
        startVA()
    
    # To run hotword
def listenHotword():
        # Code for process 2
        print("Process 2 is running.")
        from moteur.features import word_detection
        word_detection()



    # Start both processes
if __name__ == '__main__':
        p1 = multiprocessing.Process(target=startVA)
        p2 = multiprocessing.Process(target=listenHotword)
        p1.start()
        p2.start()
        p1.join()

        if p2.is_alive():
            p2.terminate()
            p2.join()

        print("system stop")  
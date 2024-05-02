
import multiprocessing
# to start VA
def start_zass():
    print("runing zass Apk")
    from main import startVA
    startVA()


# to run the voice assest
def start_word_detection():
    print("start by word_detection") 
    from moteur.features import word_detection
    word_detection() 

if __name__=="__main__":
    p1=multiprocessing.Process(target=start_zass)    
    p2=multiprocessing.Process(target=start_word_detection)   
    p1.start() 
    p1.start()
    p1.join

    if p2.is_alive():
        p2.terminate
        p2.join 

    print("system was stoped")    
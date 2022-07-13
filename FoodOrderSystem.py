from Queue import Queue
from threading import Thread
from time import sleep

queue = Queue()

def placeOrder(list):
    for order in list:
        print("Order placed for ", order)
        queue.enque(order)
        sleep(0.5)
    
def serveOrder():
    while not queue.isEmpty():
        order = queue.deque()
        print(order," served")
        sleep(2)

def main():
    orders = ['pizza','samosa','pasta','biryani','burger']
    arg = [orders]
    threadPlace = Thread(target=placeOrder,args=arg)
    threadServe = Thread(target=serveOrder)

    threadPlace.start()
    sleep(1)
    threadServe.start()

    threadPlace.join()
    threadServe.join()
    print("BYE")
    
if __name__ == "__main__":
    main()

##### OUTPUT ######
# Order placed for  pizza
# Order placed for  samosa
# Order placed for  pasta
# pizza  served
# Order placed for  biryani
# Order placed for  burger
# samosa  served
# pasta  served
# biryani  served
# burger  served
# BYE
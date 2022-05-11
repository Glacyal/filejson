from datetime import datetime
import time

if __name__ == '__main__':
    print("START")
    c = 1
    while (True) :
        s=datetime.today().strftime('%H:%M %d-%m-%Y')+"----"+datetime.today().strftime('%M')+"----"+datetime.today().strftime('%M')[1]
        print(s)
        timestamp = datetime.today().strftime('%M')[1]
        if (timestamp == "0") :
            print("Sono Dentro")
            timestamp = datetime.today().strftime('%H:%M %d-%m-%Y')
            print(timestamp)
            time.sleep(540)
            print("Fine attesa 540")
            if c % 36 == 0 :
                print("BBB")
            c += 1
        else :
            time.sleep(10)
from settings import *
from models import *
from mongoengine import connect

def baseN(num,b,numerals="abcdefghijklmnopqrstuvwxyz"):
    return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])

def main():
    connect(MONGODB_DB, host=MONGODB_HOST)
    print "Conected!"
    
    i = 0
    
    while True:
        
        val = baseN(i,26)
        obj = Domain(ccTLD="br",dpn="com",domain=val)
        obj.save()
        
        print "Val:" + baseN(i,26) 
        i=i+1
    
        if(i>10000000): break

    

if __name__ == "__main__":
    main()    

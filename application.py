from settings import *
from models import *
from mongoengine import connect

connect(MONGODB_DB, host=MONGODB_HOST)

    

if __name__ == "__main__":
    app.run()
#    app.run(host='0.0.0.0')

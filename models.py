from mongoengine import MongoEngine
from datetime import datetime

db = MongoEngine()
 
class Record(db.Document):
    IP = db.StringField()

class MXRecord(db.Document):
    Priority = db.IntField()
    Value = db.StringField()

class NSRecord(db.Document):
    TTL = db.IntField()
    Value = db.StringField()
 
class Domain(db.Document):
    ccTLD = db.StringField()
    dpn = db.StringField()
    domain = db.StringField()
    
    date_created = db.DateTimeField()
    
    date_update = db.DateTimeField(default=datetime.now)
    active = db.BooleanField(default=False)
    
    MX = db.ListField(db.EmbeddedDocumentField(MXrecord))
    NS = db.ListField(db.EmbeddedDocumentField(NSRecord))
    TXT = db.ListField(db.StringField()) 
    
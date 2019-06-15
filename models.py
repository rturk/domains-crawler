from mongoengine import *
from datetime import datetime

#db = MongoEngine()
 
class Record(Document):
    IP = StringField()

class MXRecord(EmbeddedDocument):
    Priority = IntField()
    Value = StringField()

class NSRecord(EmbeddedDocument):
    TTL = IntField()
    Value = StringField()
 
class Domain(Document):
    tld = StringField()
    dpn = StringField()
    domain = StringField()
    
    date_created = DateTimeField()
    
    date_update = DateTimeField(default=datetime.now)
    active = BooleanField(default=False)
    
    MX = ListField(EmbeddedDocumentField(MXRecord))
    NS = ListField(EmbeddedDocumentField(NSRecord))
    TXT = ListField(StringField()) 
    
    meta = {
        'indexes': ['active', 
                    {'fields': ['ccTLD','dpn','domain'], 'unique': True}]
    }    

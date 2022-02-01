from email.policy import default
from app import db

class Business(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    street = db.Column(db.String, nullable=False)
    city = db.Column(db.String ,nullable=False)
    state = db.Column(db.String ,nullable=False)
    zipcode = db.Column(db.String ,nullable=False)
    website = db.Column(db.String, nullable=True)
    category = db.Column(db.String, nullable=False)
    like_count = db.Column(db.Integer, default=0)
    
    
    
    def to_dic(self):
        return{
            "id": self.id, 
            "name": self.name,
            "street": self.street,
            "city": self.city,
            "state": self.state,
            "zipcode": self.zipcode,
            "website": self.website,
            "category": self.category,
            "like_count": self.like_count
        }
    
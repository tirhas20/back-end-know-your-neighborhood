from app import db

class Business(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    street = db.Column(db.String, nullable=False)
    city = db.Column(db.String ,nullable=False)
    state = db.Column(db.String ,nullable=False)
    zipcode = db.Column(db.String ,nullable=False)
    website = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    
    def to_dic(self):
        return{
            "id": self.id, 
            "name": self.name,
            "street": self.street,
            "city": self.city,
            "state": self.state,
            "zipcode": self.zipcode,
            "website": self.website,
            "category": self.category
        }
    def to_dic_zipcode(self):
        return{
            # "id":self.id,
            "zipcode":self.zipcode
        }
    def to_dic_category(self):
        return{
            # "id":self.id,
            "category":self.category
        }
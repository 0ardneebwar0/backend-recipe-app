from api import db


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    ratings = db.Column(db.Integer, nullable=False, default=0)
    favorite = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, name, ingredients, instructions,  ratings, favorite):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.ratings = ratings
        self.favorite = favorite
        

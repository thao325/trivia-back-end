from app import db 

# creates db tables based on models defined
# db.create_all()

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prompt = db.Column(db.String(255), nullable=False)
    choice_1 = db.Column(db.String(255), nullable=False)
    choice_2 = db.Column(db.String(255), nullable=False)
    choice_3 = db.Column(db.String(255), nullable=False)
    choice_4 = db.Column(db.String(255), nullable=False)
    correct_answer = db.Column(db.String(255), nullable=False)


    # converts instances of Question class to JSON 
    # to transfer data btw frontend & backend
    def to_dict(self):
        return {
            'id': self.id,
            'prompt': self.prompt,
            'choice_1': self.choice_1,
            'choice_2': self.choice_2,
            'choice_3': self.choice_3,
            'choice_4': self.choice_4,
            'correct_answer': self.correct_answer
        }
        
        

    
from app import db 


'''
Question

'''
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    prompt = db.Column(db.String)
    choice_1 = db.Column(db.String)
    choice_2 = db.Column(db.String)
    choice_3 = db.Column(db.String)
    choice_4 = db.Column(db.String)
    correct_answer = db.Column(db.String)
    # score = db.Column(db.Integer, default=0)


    # converts instances of Question class to JSON 
    # to transfer data from backend to frontend
    def to_dict(self):
        return {
            'id': self.id,
            'prompt': self.prompt,
            'choices': {
                '1': self.choice_1,
                '2': self.choice_2,
                '3': self.choice_3,
                '4': self.choice_4
            },
            'correct_answer': self.correct_answer
        }
        
    # takes JSON data, converts into a Python object of the `Question` class
    # to transfer data from frontend to backend
    @classmethod
    def from_dict(cls, data):
        return cls(
            prompt=data['prompt'],
            choice_1=data['choices']['1'],
            choice_2=data['choices']['2'],
            choice_3=data['choices']['3'],
            choice_4=data['choices']['4'],
            correct_answer=data['correct_answer']
        )

    
        

'''
Category
'''


# class Category(db.Model):
#     __tablename__ = 'categories'

#     id = Column(Integer, primary_key=True)
#     type = Column(String)

#     def __init__(self, type):
#         self.type = type

#     def format(self):
#         return {
#             'id': self.id,
#             'type': self.type
#         }
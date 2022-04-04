from db import db

class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    title = db.Column(db.String(30))
    content = db.Column(db.String(255)) # For now, focus on text content
    pvr = db.Column(db.Integer)     # pvr = positive vote ratio
    comments = db.Column(db.String(30))
    shares = db.Column(db.Integer)
    
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.pvr = 0
        self.comments = []
        self.shares = 0

    def json(self):
        return {
            "id": self.id, 
            "user_id": self.user_id,
            "title": self.title,
            "content": self.content,
            "pvr": self.pvr,
            "comments": self.comments,
            "shares": self.shares
        }

    def save_post(self):
        db.session.add(self)
        db.session.commit()

    def delete_post(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
        
    @classmethod
    def find_by_title(cls, title):
        return cls.query.filter_by(title=title).first()

    @classmethod
    def fing_by_user_id(cls, user_id):
        return cls.query.filter_by(user_id=user_id).first()



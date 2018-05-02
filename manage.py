# -*- encoding=UTF-8 -*-

from nowstagram import app,db
from flask_script import Manager
from nowstagram.models import User,Image,Comment
import random
from sqlalchemy import or_,and_
manager = Manager(app)

def get_image_url():
    return 'http://images.nowcoder.com/head/'+str(random.randint(0,1000))+'m.png'

@manager.command
def init_database():
    db.drop_all()
    db.create_all()
    for i in range(0,100):
        db.session.add(User('User'+str(i+1),'a'+str(i)))
        for j in range(0,3):
            db.session.add(Image(get_image_url(),i+1))
            for k in range(0,3):
                db.session.add(Comment('This is a comment'+str(k),3*i+j+1,i+1))
    db.session.commit()

    print 1,User.query.all()
    print 2,User.query.get(3)
    print 3,User.query.filter_by(id=5).all()
    print 4,User.query.filter(User.username.endswith('0')).limit(3).all()
    print 5,User.query.filter(and_(User.id>88,User.id<90)).all()
    print 6,User.query.paginate(page=1,per_page=11).items

    image = Image.query.get(1)
    print 8,image.user

    User.query.filter_by(id=2).update({'username':'[new2]'})
    db.session.commit()

    for i in range(50,100,2):
        comment = Comment.query.get(i+1)
        db.session.delete(comment)
    db.session.commit()



if __name__ == '__main__':
    manager.run()

from sqlalchemy import Table, Column, Integer,String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine('sqlite:///:memory:', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

#back_ref 를 사용하는 경우

class Parent(Base) : 
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    description = Column(String)

    def __repr__(self):
        return f"Parent : {self.id} , Description : {self.description}"


class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('parent.id'))
    description = Column(String)
    parent = relationship('Parent', backref='children')
    
    def __repr__(self):
        return f"Child : {id} , Description : {self.description}, Parent_id : {self.parent_id} "

# 스키마에 따른 테이블 생성
Base.metadata.create_all(engine) 

parent1 = Parent(id=1, description='Jone')
child1_of_parent1 = Child(id=1, description="Jone's baby ONE", parent_id =1)
child2_of_parent1 = Child(id=2, description="Jone's baby TWO", parent_id =1)

session.add_all([parent1, child1_of_parent1, child2_of_parent1] )
session.commit()


# Parent 목록
db_parent = session.query(Parent).one()


#db 상에 있는 child 출력
for child in db_parent.children :
    print(child)

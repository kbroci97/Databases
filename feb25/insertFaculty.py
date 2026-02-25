from sqlmodel import Session
from models import Faculty, engine 

f1 = Faculty(firstName = 'Christopher', lastName = 'Mansour')
f2 = Faculty(firstName = 'Mahesh', lastName = 'Maddumala')
f3 = Faculty(firstName = 'Chad', lastName = 'Redmond', age = 60)

with Session(engine) as session:
    session.add(f1)
    session.add(f2)
    session.add(f3)
    session.commit()


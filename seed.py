from app import app
from models import db, Cupcake

db.drop_all()
db.create_all()

c1 = Cupcake(
    flavor="cherry",
    size="large",
    rating=5,
)

c2 = Cupcake(
    flavor="chocolate",
    size="small",
    rating=9,
    image="https://natashaskitchen.com/wp-content/uploads/2021/04/Chocolate-Cupcakes-5-728x1092.jpg"
)

db.session.add_all([c1, c2])
db.session.commit()
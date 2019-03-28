from app import db
from app import Table, MenuItem, Order


db.create_all()


def create_tables(max_number):

    '''Create 10 Table objects, and commit to database.'''

    for i in range(max_number):
        table = Table()
        db.session.add(table)
    db.session.commit()




def create_menu_items(name, price, img):
    '''Create a few menu items.'''
    item = MenuItem(
        name = name,
        price = price,
        img = img
        )

    db.session.add(item)
    db.session.commit()


create_tables(10)
create_menu_items("Tea", 10, "https://img.etimg.com/thumb/msid-66851392,width-643,imgsize-483975,resizemode-4/do-you-have-a-habit-of-drinking-tea-it-can-lower-fracture-risk.jpg")
create_menu_items("Musli With Berries", 100, "http://www.abolitionistvegansociety.org/wp-content/uploads/2015/04/Vegan_DIY_Muesli_Mix.jpg")
create_menu_items("Hot Dog", 50, "https://media.daysoftheyear.com/20171223110023/hot-dog-day2.jpg")
create_menu_items("Egg and Beans", 20, "https://healthynibblesandbits.com/wp-content/uploads/2015/10/Fried-Egg-Breakfast-FF.jpg")
create_menu_items("Salmon", 200, "https://food.fnr.sndimg.com/content/dam/images/food/fullset/2011/7/26/1/CN1B01_oven-baked-salmon_s4x3.jpg.rend.hgtvcom.616.462.suffix/1382545141944.jpeg")

import os
from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sc'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRAC_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class product(db.Model):
    __tablename__= "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    size = db.Column(db.Text)
    price = db.Column(db.Integer)


def __init__(self, name, size, price):
    self.name = name
    self.size = size
    self.price = price
def __repr__(self):
    return "{self.name}, {self.size}, {self.price}"

db.create_all()
db.session.commit()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/itempage/sweatpants.html', methods=['POST', 'GET'])
def sweatpants():
    if request.method == 'POST':
        add = product(name = "sweatpants", size = request.form['size'], price = "45")
        db.session.add(add)
        db.session.commit()
        return redirect(url_for('cart'))
    else:
        return render_template('/itempage/sweatpants.html')

@app.route('/itempage/hoodie.html', methods=['POST', 'GET'])
def hoodie():
    if request.method == 'POST':
        add = product(name = "hoodie", size = request.form['size'], price = "65")
        db.session.add(add)
        db.session.commit()
        return redirect(url_for('cart'))
    else:
        return render_template('/itempage/hoodie.html')

@app.route('/itempage/tshirt1.html', methods=['POST', 'GET'])
def tshirt1():
    if request.method == 'POST':
        add = product(name = "embroidered t-shirt", size = request.form['size'], price = "40")
        db.session.add(add)
        db.session.commit()
        return redirect(url_for('cart'))
    else:
        return render_template('/itempage/tshirt1.html')


@app.route('/itempage/tshirt2.html', methods=['POST', 'GET'])
def tshirt2():
    if request.method == 'POST':
        add = product(name = "t-shirt", size = request.form['size'], price = "35")
        db.session.add(add)
        db.session.commit()
        return redirect(url_for('cart'))
    else:
        return render_template('/itempage/tshirt2.html')

@app.route('/itempage/jacket.html', methods=['POST', 'GET'])
def jacket():
    if request.method == 'POST':
        add = product(name = "jacket", size = request.form['size'], price = "70")
        db.session.add(add)
        db.session.commit()
        return redirect(url_for('cart'))
    else:
        return render_template('/itempage/jacket.html')

@app.route('/itempage/flannel.html', methods=['POST', 'GET'])
def flannel():
    if request.method == 'POST':
        add = product(name = "flannel", size = request.form['size'], price = "65")
        db.session.add(add)
        db.session.commit()
        return redirect(url_for('cart'))
    else:
        return render_template('/itempage/flannel.html')

@app.route('/itempage/shorts.html', methods=['POST', 'GET'])
def shorts():
    if request.method == 'POST':
        add = product(name = "shorts", size = request.form['size'], price = "40")
        db.session.add(add)
        db.session.commit()
        return redirect(url_for('cart'))
    else:
        return render_template('/itempage/shorts.html')

@app.route('/itempage/leggings.html', methods=['POST', 'GET'])
def leggings():
    if request.method == 'POST':
        add = product(name = "leggings", size = request.form['size'], price = "45")
        db.session.add(add)
        db.session.commit()
        return redirect(url_for('cart'))
    else:
        return render_template('/itempage/leggings.html')

@app.route('/templates/cart.html', methods=['POST', 'GET'])
def cart():
    if request.method == 'POST':
        return redirect(url_for('checkout'))
    return render_template('cart.html', product = product.query.all())

def clear_data(session):
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        session.execute(table.delete())
    session.commit()

@app.route('/templates/checkout.html', methods=['POST', 'GET'])
def checkout():
    if request.method == 'POST':
        clear_data(db.session)
        return redirect(url_for('home'))
    return render_template('checkout.html')

@app.route('/templates/guide.html')
def guide():
    return render_template('guide.html')

@app.route('/templates/help.html')
def help():
    return render_template('help.html')

@app.route('/templates/blog.html')
def blog():
    return render_template('blog.html')




if __name__ == '__main__':
    app.run(debug=True)





'''
sources used:
https://gist.github.com/vkotovv/6281951
'''
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import gc

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
db = SQLAlchemy(app)

# Model for contact
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)

with app.app_context():
    db.create_all()

# Homepage displaying all contacts
@app.route('/')
def index():
    contacts = Contact.query.all()
    return render_template('index.html', contacts=contacts)

# Add a new contact
@app.route('/add', methods=['GET', 'POST'])
def add_contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        
        new_contact = Contact(name=name, email=email, phone=phone)
        db.session.add(new_contact)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_contact.html')

# Edit an existing contact
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_contact(id):
    contact = Contact.query.get_or_404(id)
    if request.method == 'POST':
        contact.name = request.form['name']
        contact.email = request.form['email']
        contact.phone = request.form['phone']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit_contact.html', contact=contact)

# Delete a contact
@app.route('/delete/<int:id>')
def delete_contact(id):
    contact = Contact.query.get_or_404(id)
    db.session.delete(contact)
    db.session.commit()
    return redirect(url_for('index'))

def get_gc_stats():
    gc.collect()  # Force a garbage collection
    stats = gc.get_stats()
    
    # Example of aggregating statistics based on observed structure
    if stats:
        total_collections = sum(stat.get('collections', 0) for stat in stats)
        total_uncollectable = sum(stat.get('uncollectable', 0) for stat in stats)
        return {
            'total_collections': total_collections,
            'total_uncollectable': total_uncollectable,
            'stats': stats
        }
    else:
        return {
            'total_collections': 'N/A',
            'total_uncollectable': 'N/A',
            'stats': 'N/A'
        }

@app.route('/gc_stats')
def gc_stats():
    stats = get_gc_stats()
    return render_template('gc_debug.html', stats=stats)

if __name__ == '__main__':
    app.run(debug=True)
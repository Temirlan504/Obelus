from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
)
from flask_sqlalchemy import SQLAlchemy
from os import path

app = Flask(__name__)

db = SQLAlchemy()
DB_NAME = "site.db"
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
db.init_app(app)

# Models
class Course(db.Model):
    def __init__(self, course_name, image_file):
        self.course_name = course_name
        self.image_file = image_file

    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(
        db.String(50),
        nullable=False
    )
    image_file = db.Column(
        db.String(20),
        nullable=False
    )
    units = db.relationship(
        'Unit',
        backref='course',
        lazy=True
    )


class Unit(db.Model):
    def __init__(self, unit_name, image_file, course_id):
        self.unit_name = unit_name
        self.image_file = image_file
        self.course_id = course_id

    id = db.Column(db.Integer, primary_key=True)
    unit_name = db.Column(
        db.String(50),
        nullable=False
    )
    image_file = db.Column(
        db.String(20),
        nullable=False
    )
    course_id = db.Column(
        db.Integer,
        db.ForeignKey('course.id'),
        nullable=False
    )


# Home page (Courses page)
@app.route("/")
def index():
    return render_template(
        "index.html",
        courses=Course.query.all()
    )


# Units page by course id
@app.route("/units/<int:course_id>")
def units(course_id):
    return render_template(
        "units.html",
        course=Course.query.get_or_404(course_id),
        units=Unit.query.filter_by(course_id=course_id).all()
    )


# Admin panel for courses (add courses)
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        course_name = request.form.get('course_name')
        image_file = request.form.get('image_file')

        new_course = Course(course_name=course_name, image_file=image_file)
        db.session.add(new_course)
        db.session.commit()

        return redirect(url_for('admin'))

    return render_template(
        'admin.html',
        courses=Course.query.all()
    )


# Route for deleting courses
@app.route('/delete_course/<int:course_id>', methods=['POST'])
def delete_course(course_id):
    course = Course.query.get_or_404(course_id)
    
    db.session.delete(course)
    db.session.commit()
    
    return redirect(url_for('admin'))


# Admin panel for units (add units)
@app.route('/admin_add_units/<int:course_id>', methods=['GET', 'POST'])
def admin_add_units(course_id):
    course = Course.query.get_or_404(course_id)
    if request.method == 'POST':
        unit_name = request.form.get('unit_name')
        image_file = request.form.get('image_file')

        new_unit = Unit(
            unit_name=unit_name,
            image_file=image_file,
            course_id=course_id
        )
        db.session.add(new_unit)
        db.session.commit()

        return redirect(url_for('admin_add_units', course_id=course_id))

    return render_template(
        'admin_add_units.html',
        units=Unit.query.filter_by(course_id=course_id).all(),
        course_id=course_id,
        course=course
    )


# Route for deleting units
@app.route('/delete_unit/<int:unit_id>', methods=['POST'])
def delete_unit(unit_id):
    unit = Unit.query.get_or_404(unit_id)
    
    db.session.delete(unit)
    db.session.commit()
    
    return redirect(url_for('admin_add_units', course_id=unit.course_id))


# Create database (or update it)
# def create_database(app):
#     if not path.exists('/' + DB_NAME):
#         with app.app_context():
#             db.create_all()
#         print('Created Database!')


if __name__ == "__main__":
    # create_database(app)
    app.run(debug=True)

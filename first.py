from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

import os

project_root=os.path.dirname(os.path.realpath(__file__))
dbfile=os.path.join(project_root,'test.db')

imgfile=os.path.join('static','kl')
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+dbfile
app.config['UPLOAD_FOLDER'] = imgfile

db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	text = db.Column(db.String(80), unique=False, nullable=False)

	def __repr__(self):
		return "{}".format(self.text)

	def __str__(self):
		return unicode(self).encode('utf-8')

	def __unicode__(self):
		return self.text



@app.route('/')
def hello_world():
	users = User.query.all()
	imgk=os.path.join(app.config['UPLOAD_FOLDER'], 'im.jpg')
	return render_template('view.html', all_users=reversed(users), imgg=imgk)

@app.route('/write')
def write_db():
	textin=request.args.get('text1')
	user=User(text=textin)
	print(textin)
	db.session.add(user)
	db.session.commit()
	users = User.query.all()
	imgk=os.path.join(app.config['UPLOAD_FOLDER'], 'im.jpg')
	return render_template('view.html',all_users=reversed(users), imgg=imgk)


@app.route('/home')
def hello_home():
        users = User.query.all()
        imgk=os.path.join(app.config['UPLOAD_FOLDER'], 'im.jpg')
        return render_template('view.html', all_users=reversed(users), imgg=imgk)

'''

@app.route('/get')
def get_db():
	users = User.query.all()
	# print(all_text)
	return render_template('out.html', all_users=users)

'''



if __name__ == '__main__':
	app.run(host='0.0.0.0',port='8080')

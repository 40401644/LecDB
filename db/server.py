from flask import Flask, render_template, jsonify, request, flash
import sqlite3, json 

app = Flask(__name__)
# app.secret_key="aaa"

@app.route('/')
def indexPage():
	return render_template("student.html")

@app.route('/save',methods=['GET','POST'])
def saveStudent():
	print("saving student" + request.method)
	error = ''
	if request.method == 'POST':
		try:
			print(request.form)
			name = request.form['Name']
			phy = int(request.form['Physics'])
			che = int(request.form['Chemistry'])
			math = int(request.form['Mathematics'])
		except ValueError:
			error = "data input error"
			return render_template('student.html',error=error)
		try:
			with sqlite3.connect("student.db") as con:
				cur = con.cursor()
				cur.execute("insert into StudentNew(Name,Physics,Chemistry,Math) values(?,?,?,?)",(name,phy,che,math))
				con.commit()
				msg = "saving"
				print("saving record")
				return redirect(url_for("flaskMessage.html",msg=msg))

		except:
			con.rollback()
		finally:
			con.close()
			return render_template("student.html",error=error)
	return render_template("student.html",error=error)

@app.route('/allStudents')
def studentInformation():
	con = sqlite3.connect("C:/Users/X541UJ/LecDB/db/student.db")
	cur = con.cursor()
	cur.execute("select * from StudentNew")
	rows = cur.fetchall()
	print(rows)
	# return render_template("student.html")
	return json.dumps(rows)

if __name__ == "__main__":
	app.run(host="0.0.0.0",debug=True)
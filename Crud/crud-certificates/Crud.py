from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
import sys
# initializations
app = Flask(__name__)

# Mysql Connection
app.config['MYSQL_HOST'] = sys.argv[1] 
app.config['MYSQL_USER'] = sys.argv[2]
app.config['MYSQL_PASSWORD'] = sys.argv[3]
app.config['MYSQL_DB'] = 'crud_certificates'
mysql = MySQL(app)

# settings
app.secret_key = "mysecretkey"

# routes
@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM domains')
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', domains = data)

@app.route('/add_domain', methods=['POST'])
def add_domain():
    if request.method == 'POST':
        fulldomain = request.form['fulldomain']
        expiration_date = request.form['expiration_date']
        description = request.form['description']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO domains (fulldomain,  expiration_date, description) VALUES (%s,%s,%s)", (fulldomain,  expiration_date, description))
        mysql.connection.commit()
        flash('Domain Added successfully')
        return redirect(url_for('Index'))

@app.route('/edit/<id>', methods = ['POST', 'GET'])
def get_domain(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM domains WHERE id = %s', (id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit-domain.html', domain = data[0])

@app.route('/update/<id>', methods=['POST'])
def update_domain(id):
    if request.method == 'POST':
        fulldomain = request.form['fulldomain']
        expiration_date = request.form['expiration_date']
        description = request.form['description']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE domains
            SET fulldomain = %s,
                description = %s,
                expiration_date = %s
            WHERE id = %s
        """, (fulldomain, description,  expiration_date, id))
        flash('Domain Updated Successfully')
        mysql.connection.commit()
        return redirect(url_for('Index'))

@app.route('/delete/<string:id>', methods = ['POST','GET'])
def delete_domain(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM domains WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Domain Removed Successfully')
    return redirect(url_for('Index'))

# starting the app
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=3000, debug=True)

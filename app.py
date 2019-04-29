from flask import Flask, request, render_template
import datetime
import sqlite3
import sqlite3 as sql

# Receive SMS with Python (Proovl + Flask + Ngrok)
#1. Download receivesms.zip (3 files - app.py , db for messages and html file.)
#2. Unzip to Documents, open Terminal and type: cd ~/documents/receivesms
#3. Run command: FLASK_APP=app.py flask run
#4. You will see: Running on http://127.0.0.1:5000/ copy this link to browser
#5. Run ngrok with port 5000: ./ngrok http 5000
#You will see: Forwarding https://xec8av6e4.ngrok.io -> http://localhost:5000
#6. Go to Proovl, open Number settings and type https://xec8av6e4.ngrok.io (your ngrok link) to URL forwarding.
#7. Done! Send SMS to your dedicated number. All received messages located here: http://127.0.0.1:5000 and saved to messages.db
#Flask installation: http://flask.pocoo.org/docs/1.0/installation
#Ngrok installation: https://ngrok.com/download
#Proovl SMS numbers: https://www.proovl.com

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def process_data():
  if request.method == 'POST':
     number = request.form['from']
     text = request.form['text']
     date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
     if number:
        with sql.connect("messages.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO messages (date,number,text) VALUES (?,?,?)",(date,number,text) )       
        return "Number:{} Text:{}".format(number, text)
     if not number:
        return "No data"
  else:
  		
   		con = sql.connect("messages.db")
   		con.row_factory = sql.Row
   		cur = con.cursor()
   		cur.execute("select * from messages ORDER BY id DESC")
   		rows = cur.fetchall();
   		return render_template('msg.html',rows = rows)


if __name__ == '__main__':
    app.run(debug=True)

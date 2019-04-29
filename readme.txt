== Instruction ==
Receive SMS with Python (Proovl + Flask + Ngrok)
Open account with Proovl. Install Flask and Ngrok.
1. Download receivesms.zip (3 files - app.py , db for messages and html file.)
2. Unzip to Documents, open Terminal and type: cd ~/documents/receivesms
3. Run command: FLASK_APP=app.py flask run
4. You will see: Running on http://127.0.0.1:5000/ copy this link to browser
5. Run ngrok with port 5000: ./ngrok http 5000
You will see your personal link: Forwarding https://xec8av6e4.ngrok.io -> http://localhost:5000
6. Go to Proovl, open Number settings and type https://xec8av6e4.ngrok.io (your ngrok link) to URL forwarding.
7. Done! Send SMS to your dedicated number. All received messages located here: http://127.0.0.1:5000 and saved to messages.db

Flask installation: http://flask.pocoo.org/docs/1.0/installation
Ngrok installation: https://ngrok.com/download
Proovl SMS numbers: https://www.proovl.com
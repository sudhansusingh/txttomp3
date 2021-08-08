from flask import Flask, render_template, request,send_file
from gtts import gTTS 
from playsound import playsound
import os
app=Flask(__name__)

@app.route('/')
def hello():
	return render_template("index.html")

@app.route('/converted', methods=['POST'])
def converted():
	text=request.form['input_text']
	language = 'en' 
	myobj = gTTS(text=text, lang=language, slow=False) 
	myobj.save("welcome.mp3") 
	path="welcome.mp3"
	return send_file(path , as_attachment=True)
	#os.system("start welcome.mp3")

	


if __name__ == '__main__':
    app.run(debug=True)



from flask import Flask, render_template, request,redirect 
import speech_recognition as sr
#import necessary modules to create this application

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    transcript = "" #empty string to store the transcript in
    if request.method == "POST":
        print("FORM DATA RECEIVED")

        if "file" not in request.files:
            return(redirect(request.url))
        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)
        if file:
            recognizer = sr.Recognizer()
            audioFile = sr.AudioFile(file)
            with audioFile as source:
                data = recognizer.record(source)
            transcript = recognizer.recognize_google(data, key=None)
            #uses google speech cloud to transcribe the speech into text
            

    return render_template("index.html",transcript=transcript) #returns the text to the user

if __name__ == "__main__":
    app.run(debug=True, threaded=True)


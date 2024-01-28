from flask import Flask, render_template, request
import openai
import speech_recognition as sr
import pyttsx3

app = Flask(__name__)
engine = pyttsx3.init()
listener = sr.Recognizer()
openai.api_key = "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"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process_command', methods=['POST'])
def process_command():
    command = request.form['command']
    choice = int(request.form['choice'])
    model = "text-davinci-003"

    completion = openai.Completion.create(
        model=model,
        prompt=command,
        max_tokens=1000,
        temperature=0.5,
        n=1,
        stop=None
    )
    response = completion.choices[0].text

    if choice == 1:
        return response
    elif choice == 2:
        engine.say(response)
        engine.runAndWait()
        return response


if __name__ == '__main__':
    app.debug = True
    app.run(port=8000)  # Change the port number to a different one, e.g., 8000
    app.run()
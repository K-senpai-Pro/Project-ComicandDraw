from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# สำหรับเก็บเรื่องที่ส่ง
stories = []

@app.route('/')
def home():
    return render_template('index.html', stories=stories)

@app.route('/submit', methods=['POST'])
def submit_story():
    story_content = request.form['story']
    stories.append(story_content)  # บันทึกเรื่องลงใน list
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

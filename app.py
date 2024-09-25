from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# สำหรับเก็บเรื่องที่ส่ง
stories = []
visitor_count = 0  # ตัวแปรนับจำนวนผู้เข้าชม

@app.route('/')
def home():
    global visitor_count
    visitor_count += 1  # เพิ่มจำนวนผู้เข้าชม
    return render_template('index.html', stories=stories, visitor_count=visitor_count)

@app.route('/submit', methods=['POST'])
def submit_story():
    story_content = request.form['story']
    stories.append(story_content)  # บันทึกเรื่องลงใน list
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

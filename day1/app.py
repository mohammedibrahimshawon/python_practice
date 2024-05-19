from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

fire_size = 10
fire_intensity = [random.randint(1, 5) for _ in range(fire_size)]

@app.route('/')
def index():
    return render_template('index.html', fire_intensity=fire_intensity)

@app.route('/extinguish', methods=['POST'])
def extinguish():
    global fire_intensity
    position = int(request.form['position'])
    if 0 <= position < fire_size:
        fire_intensity[position] = max(0, fire_intensity[position] - 1)
    return jsonify({'fire_intensity': fire_intensity})

if __name__ == '__main__':
    app.run(debug=True)

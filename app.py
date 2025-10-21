from flask import Flask, render_template_string, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Jenkins CI/CD on k3s</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f4f8;
                text-align: center;
                margin-top: 100px;
            }
            h1 {
                color: #333;
            }
            p {
                font-size: 18px;
                color: #666;
            }
        </style>
    </head>
    <body>
        <h1>🚀 Welcome to Jenkins CI/CD on k3s!</h1>
        <p>Your deployment is up and running.</p>
    </body>
    </html>
    """)

@app.route('/healthz')
def healthz():
    return "OK", 200

@app.route('/readyz')
def readyz():
    return "READY", 200


@app.route('/file')
def show_file_content():
    try:
        with open('./konda.txt', 'r') as f:
            content = f.read()
        return content
    except Exception as e:
        return f"Error reading file: {e}", 500

@app.route('/image')
def show_image ():
    image_url = url_for('static', filename='plan.png')
    image_url2 = url_for('static', filename='ALB-proxys.gif')
    return render_template_string("""
        <html>
            <head><title>Image Viewer</title></head>
            <body>
                <h2>Here’s your image:</h2>
                <img src="{{ image_url }}" alt="My Image" width="400">
                <img src="{{ image_url2 }}" alt="My Image" width="400">
            </body>
        </html>
    """, image_url=image_url, image_url2=image_url2)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

from flask import Flask, render_template, request, jsonify
from flask_mail import Mail, Message
import os

app = Flask(__name__)

# --- Email configuration (optional for now) ---
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USERNAME=os.getenv('EMAIL_USER'),
    MAIL_PASSWORD=os.getenv('EMAIL_PASS'),
)

mail = Mail(app)

# --- Routes ---
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    # For now, just print (we'll wire up email sending later)
    print(f"📩 New message from {name} ({email}): {message}")
    return jsonify({"status": "success", "message": "Message sent successfully!"})

# --- Main entry point ---
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

# app.py

from flask import Flask, render_template, request, redirect, url_for
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)

# Replace with your email server details
EMAIL_HOST = 'smtp.yourserver.com'
EMAIL_PORT = 587
EMAIL_USER = 'your_email@example.com'
EMAIL_PASSWORD = 'your_password'


def send_email(article_type):
    # Email configuration
    msg = MIMEMultipart()
    msg['From'] = EMAIL_USER
    msg['To'] = 'editor@example.com'  # Replace with actual editor's email
    msg['Subject'] = 'New Article Submission'

    # Email body
    body = f"A new {article_type} article has been submitted."

    msg.attach(MIMEText(body, 'plain'))

    # Connect to SMTP server and send email
    with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASSWORD)
        server.send_message(msg)


# Sample data for editorial board and advisors
editorial_members = ['John Doe', 'Jane Smith', 'Michael Johnson']
advisory_members = ['Emily Brown', 'David Lee', 'Sarah Adams']

# Route for index page


@app.route('/')
def index():
    return render_template('index.html')

# Route for about page


@app.route('/about')
def about():
    return render_template('about.html')

# Route for editorial board page


@app.route('/editorial-board')
def editorial_board():
    return render_template('editorial_board.html', members=editorial_members)

# Route for advisors page


@app.route('/advisors')
def advisors():
    return render_template('advisors.html', members=advisory_members)

# Route for submissions page


@app.route('/submissions')
def submissions():
    return render_template('submissions.html')

# Route for citation page


@app.route('/citation')
def citation():
    return render_template('citation.html')

# Route for formatting page


@app.route('/formatting')
def formatting():
    return render_template('formatting.html')

# Route for contact page


@app.route('/contact')
def contact():
    return render_template('contact.html')

# Route for article submission form


@app.route('/submit-article', methods=['GET', 'POST'])
def submit_article():
    if request.method == 'POST':
        article_type = request.form['article_type']

        # Send email to editorial board
        send_email(article_type)

        return redirect(url_for('submission_success'))

    return render_template('submission.html')

# Route for submission success page


@app.route('/submission-success')
def submission_success():
    return 'Article submitted successfully!'


if __name__ == '__main__':
    app.run(debug=True)

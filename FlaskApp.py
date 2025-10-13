from flask import Flask, render_template

class FlaskApp:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.add_url_rule('/', self.home)
        self.app.add_url_rule('/help', self.help)
        self.app.add_url_rule('/control', self.control)
        self.app.add_url_rule('/author', self.author)

    def home(self):
        return render_template('index.html')
    
    def help(self):
        return render_template('help.html')
   
    def control(self):
        return render_template('control.html')
    
    def author(self):
        return render_template('author.html')
    
    def run(self):
        self.app.run()
import jinja2
import os
import webapp2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(template_dir))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('OpeningScreen.html')
        self.response.out.write(template.render())

class GameHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('CityScrolling.html')
        self.response.out.write(template.render())

class WinHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('win.html')
        self.response.out.write(template.render({"score":self.request.get('score',0)}))

class LoseHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('lose.html')
        self.response.out.write(template.render({"score":self.request.get('score',0)}))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/AdventureBob', GameHandler),
    ('/win', WinHandler),
    ('/lose', LoseHandler)
], debug=True)

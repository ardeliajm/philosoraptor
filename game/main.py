import jinja2
import os
import webapp2

jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))# this little bit sets jinja's relative directory to match the directory name(dirname) of the current __file__, in this case, helloworld.py

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.redirect("/static/CityScrolling.html")

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

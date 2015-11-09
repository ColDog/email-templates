from jinja2 import Environment, PackageLoader
from premailer import Premailer


class Builder:
    def __init__(self, out_file):
        self.env = Environment(loader=PackageLoader('builder', 'templates'))
        self.out_file = out_file

        # provides a template helper to turn a list into a list of pairs
        self.env.filters['pairs'] = lambda l: [l[i:i + 2] for i in range(0, len(l), 2)]

    # inlines css using premailer with my specific configuration, namely, must
    # keep classes so responsiveness can work.
    def premailer(self, html):
        return Premailer(html, base_url=None, remove_classes=False).transform()

    # creates a string of rendered html
    def render(self, elements):
        body = ''

        # loop through given elements and render respective template with options
        for element in elements:
            template = self.env.get_template(element['template'])   # gets the template
            body += template.render(element['options'])             # renders the template

        layout = self.env.get_template('body.html')     # get layout template
        output = layout.render(body=body)               # render into layout
        return self.premailer(output)

    # writes the rendered string to the specified file
    def write(self, elements):
        output = self.render(elements)          # builds the html string
        with open(self.out_file, "w") as html:  # writes the html to a file
            html.write(output)

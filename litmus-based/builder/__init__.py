from jinja2 import Environment, PackageLoader
from premailer

class Builder:
    def __init__(self, out_file):
        self.env = Environment(loader=PackageLoader('builder', 'templates'))
        self.out_file = out_file

        # provides a template helper to turn a list into a list of pairs
        self.env.filters['pairs'] = lambda l: [l[i:i + 2] for i in range(0, len(l), 2)]

    def build(self, elements):
        body = ''

        for element in elements:
            template = self.env.get_template(element['template'])
            body += template.render(element['options'])

        layout = self.env.get_template('body.html')
        return layout.render(body=body)

    def write(self, elements):
        f = open(self.out_file, "w")
        out = self.build(elements)
        f.write(out)
        f.close()

from jinja2 import Environment, PackageLoader


class Builder:
    def __init__(self):
        self.env = Environment(loader=PackageLoader('app', 'templates'))

        # provides a template helper to turn a list into a list of pairs
        self.env.filters['pairs'] = lambda l: [l[i:i + 2] for i in range(0, len(l), 2)]

    def build(self, opts):
        elements = opts['elements']
        body = ''

        for element in elements:
            template = self.env.get_template(element['template'])
            body += template.render(element['options'])

        layout = self.env.get_template('body.html')
        return layout.render(body=body, title=opts.get('title'), intro=opts.get('intro'))

    def write(self, elements):
        f = open("output.html", "w")
        out = self.build(elements)
        f.write(out)

builder = Builder()

# Sample options that can generate an email. Each dictionary contains the template it should render
# and then the options to be included in that template. The following is a sample email that can be
# created.
builder.write({
    'title': 'Title',
    'intro': 'This is the introduction which will appear first thing after the subject line',
    'elements': [
        {
            'template': 'dark-hero.html',
            'options': {
                'image': 'images/hero.png',
                'title': 'Freedom to Create',
                'content': """
                    Dear customer,

                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed varius, leo a ullamcorper feugiat, ante purus sodales justo, a faucibus libero lacus a est.

                    Sed varius, leo a ullamcorper feugiat, ante purus sodales justo, a faucibus libero lacus a est. Aenean at mollis ipsum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed varius, leo a ullamcorper feugiat, ante purus sodales justo, a faucibus libero lacus a est.

                    Sincerely,<br>Colin Walker
                """
            }
        },
        {
            'template': 'full-hero.html',
            'options': {
                'image': 'https://cms-media.skiomusic.com/wp-content/uploads/sites/3/2015/09/29200035/SKIO-Music_Biking_Burning_Man_edited.jpg'
            }
        },
        {
            'template': 'announcement.html',
            'options': {
                'image': 'https://cdn.tutsplus.com/webdesign/uploads/legacy/tuts/341_wf/tool-balsamiq.png',
                'title': 'The best product ever made'
            }
        },
        {
            'template': 'letter.html',
            'options': {
                'content': """
                        Dear customer,

                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed varius, leo a ullamcorper feugiat, ante purus sodales justo, a faucibus libero lacus a est.

                        Sed varius, leo a ullamcorper feugiat, ante purus sodales justo, a faucibus libero lacus a est. Aenean at mollis ipsum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed varius, leo a ullamcorper feugiat, ante purus sodales justo, a faucibus libero lacus a est.

                        Sincerely,<br>Colin Walker
                    """
            }
        },
        {
            'template': 'notifications.html',
            'options': {
                'notifications': [
                    {'image': 'https://cms-media.skiomusic.com/wp-content/uploads/sites/3/2015/09/29200035/SKIO-Music_Biking_Burning_Man_edited.jpg', 'title': 'Test', 'content': 'If the application enables the Loop Controls, its possible to use break and continue in loops. When break is reached, the loop is terminated.'},
                    {'image': 'https://cms-media.skiomusic.com/wp-content/uploads/sites/3/2015/09/29200035/SKIO-Music_Biking_Burning_Man_edited.jpg', 'title': 'Test', 'content': 'If the application enables the Loop Controls, its possible to use break and continue in loops. When break is reached, the loop is terminated.'},
                    {'image': 'https://cms-media.skiomusic.com/wp-content/uploads/sites/3/2015/09/29200035/SKIO-Music_Biking_Burning_Man_edited.jpg', 'title': 'Test', 'content': 'If the application enables the Loop Controls, its possible to use break and continue in loops. When break is reached, the loop is terminated.'},
                ]
            }
        },
        {
            'template': 'hero.html',
            'options': {
                'image': 'https://cms-media.skiomusic.com/wp-content/uploads/sites/3/2015/09/29200035/SKIO-Music_Biking_Burning_Man_edited.jpg',
                'alt': 'hero-image',
                'title': 'This is a really cool title',
                'caption': 'This is a caption',
                'button': 'Learn More'
            }
        },
        {
            'template': 'news.html',
            'options': {
                'articles': [
                    {'image': 'https://cms-media.skiomusic.com/wp-content/uploads/sites/3/2015/09/29200035/SKIO-Music_Biking_Burning_Man_edited.jpg', 'title': 'Test', 'content': 'If the application enables the Loop Controls, its possible to use break and continue in loops. When break is reached, the loop is terminated; if continue is reached, the processing is stopped and continues with the next iteration.'},
                    {'image': 'https://cms-media.skiomusic.com/wp-content/uploads/sites/3/2015/09/29200035/SKIO-Music_Biking_Burning_Man_edited.jpg', 'title': 'Test', 'content': 'If the application enables the Loop Controls, its possible to use break and continue in loops. When break is reached, the loop is terminated; if continue is reached, the processing is stopped and continues with the next iteration.'},
                    {'image': 'https://cms-media.skiomusic.com/wp-content/uploads/sites/3/2015/09/29200035/SKIO-Music_Biking_Burning_Man_edited.jpg', 'title': 'Test', 'content': 'If the application enables the Loop Controls, its possible to use break and continue in loops. When break is reached, the loop is terminated; if continue is reached, the processing is stopped and continues with the next iteration.'},
                ]
            }
        },
        {
            'template': 'articles.html',
            'options': {
                'articles': [
                    {'image': 'https://cms-media.skiomusic.com/wp-content/uploads/sites/3/2015/09/29200035/SKIO-Music_Biking_Burning_Man_edited.jpg', 'title': 'Test', 'content': 'If the application enables the Loop Controls, its possible to use break and continue in loops. When break is reached, the loop is terminated; if continue is reached, the processing is stopped and continues with the next iteration.'},
                    {'image': 'https://cms-media.skiomusic.com/wp-content/uploads/sites/3/2015/09/29200035/SKIO-Music_Biking_Burning_Man_edited.jpg', 'title': 'Test', 'content': 'If the application enables the Loop Controls, its possible to use break and continue in loops. When break is reached, the loop is terminated; if continue is reached, the processing is stopped and continues with the next iteration.'},
                    {'image': 'https://cms-media.skiomusic.com/wp-content/uploads/sites/3/2015/09/29200035/SKIO-Music_Biking_Burning_Man_edited.jpg', 'title': 'Test', 'content': 'If the application enables the Loop Controls, its possible to use break and continue in loops. When break is reached, the loop is terminated; if continue is reached, the processing is stopped and continues with the next iteration.'},
                ]
            }
        },
        {
            'template': 'receipt.html',
            'options': {
                'title': 'Your Receipt',
                'description': 'This is an official reciept from SKIO Music',
                'total': '$ 1,000,000',
                'order': [
                    {'name': 'Milk', 'price': '$ 11.00'},
                    {'name': 'Milk', 'price': '$ 11.00'},
                    {'name': 'Milk', 'price': '$ 11.00'},
                    {'name': 'Milk', 'price': '$ 11.00'},
                ]
            }
        }
    ]
})



from builder import Builder

builder = Builder('dark-hero.html')

builder.write([
    {
        'template': 'dark-hero.html',
        'options': {
            'image': 'http://s30.postimg.org/4h73cnl7l/hero.png',
            'title': 'Freedom to Create',
            'content': """
                Dear customer,
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed varius, leo a ullamcorper feugiat, ante purus sodales justo, a faucibus libero lacus a est.
                Sed varius, leo a ullamcorper feugiat, ante purus sodales justo, a faucibus libero lacus a est. Aenean at mollis ipsum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed varius, leo a ullamcorper feugiat, ante purus sodales justo, a faucibus libero lacus a est.
                Sincerely,<br>Colin Walker
            """
        }
    }
])

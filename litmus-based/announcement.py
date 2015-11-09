from builder import Builder

builder = Builder('announcement.html')

builder.write([
    {
        'template': 'header.html',
        'options': {
            'intro': 'This is the introduction which will appear first thing after the subject line',
            'logo_image': 'https://cms-media.skiomusic.com/wp-content/uploads/sites/4/2015/10/29033923/skio-logo-white.png',
            'logo_alt': 'Skio Music',
            'tagline': 'Discover Music, Build Contracts and Find Collaborators'
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
        'template': 'footer.html',
        'options': {
            'links': [
                {'url': '#', 'image': 'http://icons.iconarchive.com/icons/brainleaf/round-social/128/youtube-icon.png'},
                {'url': '#', 'image': 'http://icons.iconarchive.com/icons/brainleaf/round-social/128/facebook-icon.png'},
            ]
        }
    },
])

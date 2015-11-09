from builder import Builder

builder = Builder('articles.html')

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
        'template': 'articles.html',
        'options': {
            'articles': [
                {'image': 'https://cdn0.iconfinder.com/data/icons/superuser-web-kit/512/686909-user_people_man_human_head_person-512.png', 'title': 'Test', 'content': 'Someone has done something.'},
                {'image': 'https://cdn0.iconfinder.com/data/icons/superuser-web-kit/512/686909-user_people_man_human_head_person-512.png', 'title': 'Test', 'content': 'Someone has done something.'},
                {'image': 'https://cdn0.iconfinder.com/data/icons/superuser-web-kit/512/686909-user_people_man_human_head_person-512.png', 'title': 'Test', 'content': 'Someone has done something.'},
                {'image': 'https://cdn0.iconfinder.com/data/icons/superuser-web-kit/512/686909-user_people_man_human_head_person-512.png', 'title': 'Test', 'content': 'Someone has done something.'},
                {'image': 'https://cdn0.iconfinder.com/data/icons/superuser-web-kit/512/686909-user_people_man_human_head_person-512.png', 'title': 'Test', 'content': 'Someone has done something.'},
                {'image': 'https://cdn0.iconfinder.com/data/icons/superuser-web-kit/512/686909-user_people_man_human_head_person-512.png', 'title': 'Test', 'content': 'Someone has done something.'},
            ]
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
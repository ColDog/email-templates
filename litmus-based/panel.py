from builder import Builder

builder = Builder('panel.html')

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
        'template': 'panel.html',
        'options': {
            'title': 'Thank You For Signing Up!',
            'content': """
            Hello Person,
            This is an announcement made inside a panel.
            Here is where you would tell people about what you can do for them.
            """,
            'button': 'Check it out',
        }
    },
    {
        'template': 'panel.html',
        'options': {
            'title': 'Need Help?',
            'content': """
            Our help section can help you with anything and everything.
            """,
            'button': 'Get Help',
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

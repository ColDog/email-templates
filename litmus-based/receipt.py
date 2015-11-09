from builder import Builder

builder = Builder('receipt.html')

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
        'template': 'receipt.html',
        'options': {
            'title': 'Thank You For Your Purchase',
            'description': 'This is an official reciept from SKIO Music',
            'total': '$ 1,000,000',
            'order': [
                {'name': 'Milk', 'price': '$ 11.00'},
                {'name': 'Milk', 'price': '$ 11.00'},
                {'name': 'Milk', 'price': '$ 11.00'},
                {'name': 'Milk', 'price': '$ 11.00'},
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

from builder import Builder

builder = Builder('newsletter.html')

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
        'template': 'hero.html',
        'options': {
            'image': 'http://s13.postimg.org/onrn1n72f/big_hero1.png',
            'title': 'The best product ever made',
            'button': 'Go',
        }
    },
    {
        'template': 'news.html',
        'options': {
            'articles': [
                {'image': 'https://cms-media.skiomusic.com/wp-content/uploads/sites/3/2015/09/29200035/SKIO-Music_Biking_Burning_Man_edited.jpg', 'button': 'button', 'title': 'Test', 'content': 'If the application enables the Loop Controls, its possible to use break and continue in loops. When break is reached, the loop is terminated; if continue is reached, the processing is stopped and continues with the next iteration.'},
                {'image': 'https://cms-media.skiomusic.com/wp-content/uploads/sites/3/2015/09/29200035/SKIO-Music_Biking_Burning_Man_edited.jpg', 'button': 'button', 'title': 'Test', 'content': 'If the application enables the Loop Controls, its possible to use break and continue in loops. When break is reached, the loop is terminated; if continue is reached, the processing is stopped and continues with the next iteration.'},
                {'image': 'https://cms-media.skiomusic.com/wp-content/uploads/sites/3/2015/09/29200035/SKIO-Music_Biking_Burning_Man_edited.jpg', 'button': 'button', 'title': 'Test', 'content': 'If the application enables the Loop Controls, its possible to use break and continue in loops. When break is reached, the loop is terminated; if continue is reached, the processing is stopped and continues with the next iteration.'},
            ]
        }
    },
    {
        'template': 'notifications.html',
        'options': {
            'notifications': [
                {'image': 'http://www.myiconfinder.com/uploads/iconsets/256-256-64273d52c282e3b26d2d0968d08b9d8d.png', 'subtitle': 'Jan 4 2015', 'title': 'Event Name', 'content': 'This is a notification about something happening at a certain time.'},
                {'image': 'http://www.myiconfinder.com/uploads/iconsets/256-256-64273d52c282e3b26d2d0968d08b9d8d.png', 'subtitle': 'Jan 4 2015', 'title': 'Event Name', 'content': 'This is a notification about something happening at a certain time.'},
                {'image': 'http://www.myiconfinder.com/uploads/iconsets/256-256-64273d52c282e3b26d2d0968d08b9d8d.png', 'subtitle': 'Jan 4 2015', 'title': 'Event Name', 'content': 'This is a notification about something happening at a certain time.'},
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

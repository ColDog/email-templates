from builder import Builder

builder = Builder('kitchen-sink.html')

builder.write({
    'title': 'Title',
    'intro': 'This is the introduction which will appear first thing after the subject line',
    'elements': [
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
                'title': 'This is a cool panel',
                'content': """
                Hello Everyone,

                This is an announcement made inside a panel.
                """,
                'button': 'Check it out',
            }
        },
        {
          'template': 'header.html',
             'options': {
                'intro': 'This is the first line that will show up right after the subject.',
                'logo_image': 'https://cms-media.skiomusic.com/wp-content/uploads/sites/4/2015/10/29033923/skio-logo-white.png',
                'logo_alt': 'Skio Music'

             }
        },
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

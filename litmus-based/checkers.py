from builder import Builder

builder = Builder('checkers.html')

builder.write([
    {
        'template': 'checkered.html',
        'options': {
            'articles': [
                {'image': 'https://cms-media.skiomusic.com/wp-content/uploads/sites/3/2015/09/29200035/SKIO-Music_Biking_Burning_Man_edited.jpg', 'button': 'Read', 'bg_color': '#E1A6C3', 'title': 'Test', 'content': 'If the application enables the Loop Controls, its possible to use break and continue in loops. When break is reached, the loop is terminated; if continue is reached, the processing is stopped and continues with the next iteration.'},
                {'image': 'https://cms-media.skiomusic.com/wp-content/uploads/sites/3/2015/09/29200035/SKIO-Music_Biking_Burning_Man_edited.jpg', 'button': 'Read', 'bg_color': '#ADC2EB', 'title': 'Test', 'content': 'If the application enables the Loop Controls, its possible to use break and continue in loops. When break is reached, the loop is terminated; if continue is reached, the processing is stopped and continues with the next iteration.'},
                {'image': 'https://cms-media.skiomusic.com/wp-content/uploads/sites/3/2015/09/29200035/SKIO-Music_Biking_Burning_Man_edited.jpg', 'button': 'Read', 'bg_color': '#E1A6C3', 'title': 'Test', 'content': 'If the application enables the Loop Controls, its possible to use break and continue in loops. When break is reached, the loop is terminated; if continue is reached, the processing is stopped and continues with the next iteration.'},
                {'image': 'https://cms-media.skiomusic.com/wp-content/uploads/sites/3/2015/09/29200035/SKIO-Music_Biking_Burning_Man_edited.jpg', 'button': 'Read', 'bg_color': '#7094DB', 'title': 'Test', 'content': 'If the application enables the Loop Controls, its possible to use break and continue in loops. When break is reached, the loop is terminated; if continue is reached, the processing is stopped and continues with the next iteration.'},
            ]
        }
    }
])

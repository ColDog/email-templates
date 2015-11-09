# Email Templates

This repository contains a sample of my work done on creating email templates. There are two relevant packages: The Zurb folder has the work that I have done with the Zurb foundation tempates, while the builder folder has the work I have done with another templating system from Litmus.

##### Quickstart Summary
The following links are some of the templates I've built. I focused more on building components that I've seen in various places and in my research for this project. As a result, the emails are not direct copies of certain emails, but the components I think are pretty common and reusable.

1. Announcement: http://rawgit.com/coldog/email-templates/master/litmus-based/announcement.html
2. List of Articles: http://rawgit.com/coldog/email-templates/master/litmus-based/articles.html
3. Dark Full Hero: http://rawgit.com/coldog/email-templates/master/litmus-based/dark-hero.html
4. Newsletter: http://rawgit.com/coldog/email-templates/master/litmus-based/newsletter.html
5. Basic Intro: http://rawgit.com/coldog/email-templates/master/litmus-based/panel.html
5. Sales Receipt: http://rawgit.com/coldog/email-templates/master/litmus-based/receipt.html

I liked the Zurb templates as they were easy to design and the markup was nice, but they seemed to fall flat in testing. It even says on their homepage that they don't support Outlook. So I tried the 'framework' from Zurb called Ink, but I found that it didn't do so well on Gmail although it improved on Outlook. I ended up doing most of the work above with Litmus templates https://litmus.com/resources/free-responsive-email-templates. See below for my reasoning.

### Overview

#### Zurb
I took some screenshots of the work I was doing to make it easier to take a quick glance, they are in zurb/screenshots.

I found the Zurb templates really easy to understand and fun to work with, but not as universal as far as their rendering across different clients. They admit that they cannot render on Outlook at all in the notes below the templates, but I also found out that they do not render well on Gmail as well.

I then tried Ink, which is like a front end CSS framework but for emails. This is like the original templates but built out more. This became less intuitive for building because the markup was very strange especially for just trying to center text. Outlook was better on the tests, but Gmail still wasn't working for me.

#### Litmus
This is a collection of templates from Litmus, the company that owns the market as far as email testing goes, so I think they should be able to write some pretty good templates. The markup for these was absolutely awful, but it is way more consistent across different email clients. Most of the difficulty with the markup is that it uses tables for almost everything, even a button becomes a table. The upside is it just works on everything I've tested it on, whereas Zurb's templates have not lived up to that.

I also ended up building a build script in Python to inline the CSS, and while I was at it, I converted my components I was building into template files that can be mashed up together based on a dictionary. The litmus-based/builder folder contains the Builder class. You will notice each template in the `litmus-based` folder has a corresponding script with the dictionary that built it. I mainly did this to make it easier to keep track of the components and add dummy markup but I think it could be very useful down the road for keeping things maintainable.

It means you can build an email with the following script:

```python
from builder import Builder

builder = Builder('output-file.html')

# this will write the html to 'output-file.html'. 
# We can use `builder.build()` to create a string of html.
builder.write([
    {
        'template': 'header.html',  # this is the template that will be selected
        'options': {                # it will be rendered with these options
            'intro': 'This is the introduction which will appear first thing after the subject line',
            'logo_image': 'img.png',
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
])
```

### Conclusion

Overall, I would recommend going in the direction of the Litmus templates, I think they are just simply much more robust. The downside is that they are hard to work with because of the markup structure. But when you refactor them into separate templates that can be easily combined I think they are much easier to deal with. Despite this, I would love to work with Zurb's templates and would try and implement some of the features of the Litmus templates like bulletproof buttons to make the Zurb templates more universal.

# Email Templates

This repository contains a sample of my work done on creating email templates. There are two relevant packages: The Zurb folder has the work that I have done with the Zurb foundation tempates, while the builder folder has the work I have done with another templating system from Litmus.

## Zurb Templates
I took some screenshots of the work I was doing to make it easier to take a quick glance, they are in zurb/screenshots.

I found the Zurb templates really easy to understand and fun to work with, but not as universal as far as their rendering across different clients. They admit that they cannot render on Outlook at all in the notes below the templates, but I also found out that they do not render well on Gmail as well.

I then tried Ink, which is like a front end CSS framework but for emails. This is like the original templates but built out more. This became less intuitive for building because the markup was very strange especially for just trying to center text. Overall, Outlook was better on the tests, but Gmail still wasn't working for me.


## Slate from Litmus
You can see an example page with all of the built out elements so far. Check out the page at: 
    https://rawgit.com/coldog/email-templates/master/builder/output.html

This is a collection of templates from Litmus, the company that owns the market as far as email testing goes, so I think they should be able to write some pretty good templates. The markup for these was absolutely awful, but it is way more consistent across different email clients.

Overall, tables have much more support than any other HTML element in email clients it seems. So it is better if everything is a table, that's the approach taken by the Litmus templates. Everything from buttons to just standard markup is a table. It is absolutely awful to write but it does work. I believe they are the people behind the 'bulletproof buttons' which are buttons that work on every client. Zurb's buttons simply just don't seem to work when I tested them.

I wrote a small little python program that can basically mash up different templates and elements based on the Litmus templates. For example, you can write something like this:

```python
builder.write({
    'title': 'Title',
    'intro': 'This is the introduction line',
    'elements': [
        {
            'template': 'dark-hero.html',
            'options': {
                'image': 'images/hero.png',
                'title': 'Welcome',
                'content': """
                    Dear Customer,
                    
                    This is a letter.

                    Sincerely,
                    
                    Colin Walker
                """
            }
        },
        {
            'template': 'full-hero.html',
            'options': {
                'image': 'images/hero.png'
            }
        },
```

Which will create an html email with two hero images and some text.

## Conclusion

### Overview

Overall, I would recommend going in the direction of the Litmus templates, I think they are just simply much more robust. The downside is that they are hard to work with because of the markup structure. But when you refactor them into separate templates that can be easily combined I think they are much easier to deal with.

Despite this, I would love to work with Zurb's templates and would try and implement some of the features of the Litmus templates like bulletproof buttons to make the Zurb templates more universal.

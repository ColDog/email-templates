# Email Templates

This repository contains a sample of my work done on creating email templates. There are two relevant packages: The Zurb folder has the work that I have done with the Zurb foundation tempates, while the builder folder has the work I have done with another templating system from Litmus.

## Zurb Templates
I found the Zurb templates really easy to understand and fun to work with, but not as universal as far as their rendering across different clients. They admit that they cannot render on Outlook at all in the notes below the templates, but I also found out that they do not render well on Gmail as well.

I then tried Ink, which is like a front end CSS framework but for emails. This is like the original templates but built out more. This became less intuitive for building because the markup was very strange especially for just trying to center text. Overall, Outlook was better on the tests, but Gmail still wasn't working for me.

## Slate from Litmus
This is a collection of templates from Litmus, the company that owns the market as far as email testing goes, so I think they should be able to write some pretty good templates. The markup for these was absolutely awful, but it is way more consistent across different email clients.

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
Overall, I would recommend going in the direction of the Litmus templates, I think they are just simply much more robust. The downside is that they are hard to work with because of the markup structure. But when you refactor them into separate templates that can be easily combined
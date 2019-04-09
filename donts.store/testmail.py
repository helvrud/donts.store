#~ from django.core.mail import send_mail

#~ send_mail(
    #~ 'Subject here',
    #~ 'Here is the message.',
    #~ 'sales@donts.store',
    #~ ['helvrud@gmail.com'],
    #~ fail_silently=False,
#~ )
from post_office import mail

mail.send(
    ['helvrud@gmail.com'],
    'sales@donts.store',
    subject='My email',
    message='Hi there!',
    html_message='Hi <strong>there</strong>!',
)
mail.send_queued()

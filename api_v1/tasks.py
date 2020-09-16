from celery import shared_task
from django.core.mail import send_mail, EmailMessage
from time import sleep
from main.constants import *



@shared_task
def message_send_task(name, email, message):
    subject = 'Message from %s' % name
    content = MAIL_CONTENT_MESSAGE.format(name, message, email)
    send_mail_task.delay(
        subject = subject,
        content = content,
        from_email = 'noreply@industry.gov.tm',
        to = ['info@industry.gov.tm'],
    )
    return True

@shared_task
def send_mail_task(subject, content, from_email, to, attached = None):
    msg = EmailMessage(subject, content, from_email, to)
    msg.content_subtype = 'html'
    if attached is not None:
        msg.attach_file(os.path.join(settings.MEDIA_ROOT, attached))
        
    try:
        msg.send(fail_silently = True)
        logger.info('E-mail is successfully sended to %s' % to)
    except:
        logger.error('Sending e-mail is failed')
        logger.exception('func: send_mail_task; msg: Catched exception')
        return False
    return True
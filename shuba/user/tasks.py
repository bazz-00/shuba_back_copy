from django.template.loader import get_template
from django.core import mail
from shuba.celery import app



@app.task
def send_register_email_task(user_id):
    from user.models import User

    user = User.objects.get(id=user_id)
    print("TASK", user)
    plaintext = get_template("email/register_email.txt")
    htmly     = get_template("email/register_email.html")
    d = {"user": user}
    subject = "Welcome SHUBA"
    text_content = plaintext.render(d)
    html_content = htmly.render(d)
    msg = mail.EmailMultiAlternatives(subject, text_content, to=[user.email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()




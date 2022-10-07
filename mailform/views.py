from django.shortcuts import render
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

# Create your views here.
def mailfunction(sender_mail, 
sender_password, 
mail_receiver,
subject
):

# message header
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender_mail
    msg['To'] = mail_receiver
# message in the html format
    html = """
    <html>
    <body>
        {0}
    </body>
    </html>
    """.format(subject)
    # setting the message
    htmlmsg = MIMEText(html, 'html')
    msg.attach(htmlmsg)
    # configuration of the smpt
    s = smtplib.SMTP_SSL('smtp.gmail.com')
    s.login(sender_mail, sender_password)

    s.sendmail(
            sender_mail, mail_receiver, msg.as_string()
        )
    return msg


# function that render to form.html
def home(request):
    if request.method == 'POST':
        sender_mail = request.POST['sender_email']
        sender_password=request.POST['sender_pass']        
        # sender_mail = 'akeemtolanifatai@gmail.com'
        # sender_password='hakeem1@@'
# Create the container (outer) email message.
        # msg = MIMEMultipart()
#         msg['Subject'] = 'Our family reunion'
#         # me == the sender's email address
#         # family = the list of all recipients' email addresses
#         msg['From'] = sender_mail
#         msg['To'] = 'akeemtolanifatai@gmail.com'
#         # msg['To'] = ', '.join('akeemtolanifatai@gmail.com')
#         msg.preamble = 'Our family reunion'

# # to = ["person1@example.com", "person2@example.com", "person3@example.com"]
#         s = smtplib.SMTP('smtp.gmail.com')
#         s.sendmail(sender_mail, 'akeemtolanifatai@gmail.com', msg.as_string())
#         s.quit()


        # msg = MIMEMultipart()
        # msg['Subject'] = 'Our family reunion'
        # # me == the sender's email address
        # # family = the list of all recipients' email addresses
        # msg['From'] = sender_mail
        # msg['To']
        # server=smtplib.SMTP('smtp.gmail.com', '465')#465
        s = smtplib.SMTP_SSL('smtp.gmail.com')
        # SMTP port (25, 465, 587)
        
# uncomment if interested in the actual smtp conversation
# s.set_debuglevel(1)
# do the smtp auth; sends ehlo if it hasn't been sent already
        s.login(sender_mail, sender_password)
        # server.starttls()
        # authEmail = server.login(sender_mail, sender_password)
        # print('akeem', authEmail)
        # receiver_mail = request.POST['receiver_email']
        # subject = request.POST['subject']
        # mailfunction(sender_mail, sender_password, receiver_mail, subject)


    return render(request, 'form.html')
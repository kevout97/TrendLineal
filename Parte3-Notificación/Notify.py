import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

COMMASPACE = ', '
# Define params
rrdpath = '/home/escom/PycharmProjects/TrendLineal1/RRD/'
pngpath = '/home/escom/PycharmProjects/TrendLineal1/IMG/'
fname = 'trend.rrd'

mailsender = "dummycuenta3@gmail.com"
mailreceip = "dummycuenta3@gmail.com"
mailserver = 'smtp.gmail.com: 587'
password = 'Secreto123'

def send_alert_attached(subject):
    """ Will send e-mail, attaching png
    files in the flist.
    """
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = mailsender
    msg['To'] = mailreceip
    fp = open(pngpath+'deteccion.png', 'rb')
    img = MIMEImage(fp.read())
    fp.close()
    msg.attach(img)
    mserver = smtplib.SMTP(mailserver)
    mserver.starttls()
    # Login Credentials for sending the mail
    mserver.login(mailsender, password)

    mserver.sendmail(mailsender, mailreceip, msg.as_string())
    mserver.quit()

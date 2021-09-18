import webbrowser


def open_mail(recipient,subject,body):
    webbrowser.open('mailto:?to=' + recipient + '&subject=' + subject + '&body=' + body, new=1,)
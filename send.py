import os
import sys
import smtplib
import datetime
import argparse
import random
import string
import urllib2
from os.path import basename
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.mime.application import MIMEApplication

#TODO: Multiple Attachments
#TODO: Logger for output
#TODO: Journal for mails


DEFAULT_MAIL_BODY = "Test mail from python"
PHISHING_MAIL_BODY = '<a href="http://this-is-confident.com/login.php" target="http://www.google.com" rel="noopener noreferrer" data-auth="NotApplicable" id="LPlnk555674" previewinformation="1">http://this-is-confident.com/login.php</a>'


def log(*a):
    print "[dimako]", "".join(map(str,a))


class DefaultConfig(object):
    def __init__(self):
        self.smtp_server = 'smtp.gmail.com'
        self.smtp_port = 587
        self.username = 'avanan.lab'
        self.password = 'AvananLab123'
        self.fromaddr = "avanan.lab@gmail.com"
        self.toaddr = "user1@avdima.onmicrosoft.com"

    def __repr__(self):
        return "smtp_server:{}\nsmtp_port:{}\nusername:{}\npassword:{}\nfromaddr:{}\ntoaddr:{}".format(
            smtp_server, smtp_port, username, password, fromaddr, toaddr
        )


class MailSender(object):
    def __init__(self, config=None):
        if config:
            self.config = config
        else:
            self.config = DefaultConfig()

    @staticmethod
    def create_subject():
        words_url = 'https://raw.githubusercontent.com/paritytech/wordlist/master/res/wordlist.txt'
        words_response = urllib2.urlopen(words_url)
        words_raw = words_response.read()
        words = words_raw.split()
        # random_str = ''.join(random.choice(string.ascii_lowercase) for _ in range(8))
        random_str = '{}_{}'.format(random.choice(words), random.choice(words))
        return "testmail {:%d/%m/%Y %H%M} {}".format(datetime.datetime.now(), random_str)

    def create_msg(self, to_addr, from_addr=None, files_list=None, is_phishing=False):
        conf = self.config
        msg = MIMEMultipart()
        msg['From'] = from_addr or conf.fromaddr
        msg['To'] = ', '.join(to_addr or conf.toaddr)
        msg['Subject'] = self.create_subject()
        body = PHISHING_MAIL_BODY if is_phishing else DEFAULT_MAIL_BODY
        log("Mail body: {}".format(body))
        msg.attach(MIMEText(body, 'html'))

        for filename in files_list:
            # Attach a file
            try:
                part = MIMEApplication(open(filename, "rb").read())
            except IOError as e:
                log("[ERROR] File not found: {}".format(basename(filename)))
                continue

            # After the file is closed
            part['Content-Disposition'] = 'attachment; filename="%s"' % basename(filename)
            msg.attach(part)

        log("Files attached: {}".format(files_list))

        return msg

    def send_mail(self, to_addr=None, from_addr=None, files_list=None, is_phishing=False):
        conf = self.config

        # Mail Message
        msg = self.create_msg(to_addr, from_addr, files_list=files_list, is_phishing=is_phishing)

        server = smtplib.SMTP()

        try:
            rv = server.connect(conf.smtp_server, conf.smtp_port)
            # log("Connected to {} on port {}. rv={}".format(conf.smtp_server, conf.smtp_port, rv))
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(conf.username, conf.password)
            # log("Logged in as {}".format(conf.username))
            server.sendmail(msg['From'], msg['To'], msg.as_string())
            log('From: {}'.format(msg['From']))
            log('To: {}'.format(msg['To']))
            log('Subject: {}'.format(msg['Subject']))

        except smtplib.SMTPException as e:
            print "Something went wrong. Code: {}\n{}".format(e[0], e[1])

        finally:
            rv = server.quit()
            # log("Connection closed. rv={}".format(rv))


def main():
    config = DefaultConfig()

    parser = argparse.ArgumentParser(description='Quickly send and email from CLI.')
    parser.add_argument('files', help='files to send', nargs='+')
    parser.add_argument('-t', '--to', help='mail recipients', nargs='+')
    parser.add_argument('-f', '--from', help='mail sender', required=False)
    parser.add_argument('--phishing', action='store_true', help='Send phishing mail')

    args = vars(parser.parse_args())

    files_list = args['files']
    to_addr = args['to']
    from_addr = args['from']
    is_phishing = args['phishing']

    # #PYCALLGRAPH TEST
    # from pycallgraph import PyCallGraph
    # from pycallgraph.output import GraphvizOutput
    # from pycallgraph import GlobbingFilter
    # from pycallgraph import Config as CGConfig
    # cg_config = CGConfig(max_depth=10)
    # cg_config.trace_filter = GlobbingFilter(exclude=['email*', 'smtplib*', 'urllib*', 'ssl*'])
    # graphviz = GraphvizOutput(output_file='12345.png')
    #
    # with PyCallGraph(output=graphviz, config=cg_config):
    #     sender = MailSender(config)
    #     sender.send_mail(files_list=files_list, is_phishing=is_phishing)

    sender = MailSender(config)
    sender.send_mail(to_addr=to_addr, from_addr=from_addr, files_list=files_list, is_phishing=is_phishing)

    return 0


if __name__ == '__main__':
    exit(main())

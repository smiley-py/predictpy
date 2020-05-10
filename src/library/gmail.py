from datetime import datetime
import imaplib
import email
import base64
import html2text
from os import path


class CustomGmail():
    def __init__(self):
        self.msg = ''
        self.m = imaplib.IMAP4_SSL('imap.gmail.com', 993)
        self.m.login('itmonitoringcommunity@gmail.com','MonitoringCommunity18')
        self.m.select('inbox')
        self.filter = '(FROM "oguzkaragoz@gmail.com" SUBJECT "write")'
    
    def __del__(self):
        self.m.close()
        self.m.logout()

    def read_email_from_gmail(self):    
        result, data = self.m.uid('search', self.filter)
        # print(result,data)

        if result=='OK':
            for num in data[0].split():
                result,data = self.m.uid('fetch',num,'RFC822')
                if result == 'OK':
                    message = email.message_from_string(
                        data[0][1].decode("utf-8"))
                    
                    dt = datetime.fromtimestamp(email.utils.mktime_tz(email.utils.parsedate_tz(message['Date'])))

                    res = {
                        'From' : email.utils.parseaddr(message['From'])[1],
                        'From name' : email.utils.parseaddr(message['From'])[0],
                        'Time' : dt.isoformat(),
                        'To' : message['To'],
                        'Subject' : message["Subject"],
                        'Text' : '',
                        'File' : None 
                    }

                    for part in message.walk():
                        if part.get_content_maintype() == 'multipart':
                            continue
                        if part.get_content_maintype() == 'text':
                            # reading as HTML (not plain text)

                            _html = part.get_payload(decode = True).decode("utf-8")
                            _html = str(_html).replace('\r', '').replace('\n', '')
                            res['Text'] = html2text.html2text(_html).replace('\n','')                            

                        elif part.get_content_maintype() == 'application' and part.get_filename():
                            fname = path.join("your/folder", part.get_filename())
                            attachment = open(fname, 'wb')
                            attachment.write(part.get_payload(decode = True))
                            attachment.close()
                            if res['File']:
                                res['File'].append(fname)
                            else:
                                res['File'] = [fname]

                    print(res)


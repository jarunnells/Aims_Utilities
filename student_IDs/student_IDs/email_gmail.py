import os
import smtplib
import datetime
from configparser import ConfigParser
from email.headerregistry import Address
from email.message import EmailMessage

'''
Local Debug Email Server:

$ python3 -m smtpd -c DebuggingServer -n localhost:1025
'''


class EmailGmail:

    def __init__(self, type_, files=None):
        self.cfg = ConfigParser().read('config.ini')
        self.type_ = type_
        self.files = files
        self.init_vars(self.cfg)

    def init_vars(self, cfg):
        self.DISPLAY = cfg['GMAIL'].get('DISPLAY', None)
        self.LOCAL = cfg['GMAIL'].get('LOCAL', None)
        self.DOMAIN = cfg['GMAIL'].get('DOMAIN', None)
        self.SERVER = cfg['GMAIL'].get('SERVER', None)
        self.PORT = cfg['GMAIL'].get('PORT', None)
        self.PORT_SSL = cfg['GMAIL'].get('PORT_SSL', None)
        self.SENDER = Address(display_name=self.DISPLAY,
                              username=self.LOCAL,
                              domain=self.DOMAIN,
                              addr_spec=f'{self.LOCAL}@{self.DOMAIN}'
                              )
        self.RECIPIENTS = [Address(display_name='Ann Z',
                                   username='localpart',
                                   domain=self.DOMAIN,
                                   addr_spec=f'localpart@{self.DOMAIN}'
                                   ),
                           Address(display_name='Game Room',
                                   username='GameRoom',
                                   domain=self.DOMAIN,
                                   addr_spec=f'GameRoom@{self.DOMAIN}'
                                   )
                           ]
        self.STUDENTS = ['student_01@aims.edu',
                         'student_02@aims.edu',
                         'student_03@aims.edu',
                         'student_04@aims.edu'
                         ]
        self.SUBJECT = f"{cfg['DEFAULT'].get('SUBJECT', '')} - {datetime.datetime.now()}"
        self.BODY_IMG = cfg['DEFAULT'].get('BODY_IMG', '')
        self.BODY_STUDENT = cfg['DEFAULT'].get('BODY_STUDENT', '')
        
        self.files = ['zip_file_01.zip', 'zip_file_02.zip']

    def email_init(self):
        # MESSAGE HEADER
        self.message = EmailMessage()
        self.message['Subject'] = self.SUBJECT
        self.message['From'] = self.SENDER

        if self.type_ == 'attachment':
            self.message['To'] = ", ".join(self.RECIPIENTS)
        else:
            self.message['Bcc'] = ", ".join(self.STUDENTS)

        # MESSAGE BODY - PLAIN TEXT
        self.message.set_content(
            self.BODY_IMG if self.type_ == 'attachment' else self.BODY_STUDENT)

        # MESSAGE BODY - HTML ALTERNATIVE
        self.message.add_alternative(f"""\
        <!DOCTYPE html>
        <html>
            <body>
                <h3 style="color:Crimson;">...HEADING...</h3>
                <p style="color:SlateGray;">{self.BODY_IMG if self.type_ == 'attachment' else self.BODY_STUDENT}</p>
            </body>
        </html>
        """, subtype='html')

        if self.type_ == 'attachment':
            # ATTACHMENTS
            for file in self.files:
                with open(file, 'rb') as f:
                    self.f_data = f.read()
                    self.f_name = f.name
            self.message.add_attachment(data=self.f_data,
                                        maintype='application',
                                        subtype='zip',
                                        # subtype='octet-stream',
                                        filename=self.f_name
                                        )

    def email_send(self):
        with smtplib.SMTP_SSL(host=self.SERVER, port=self.PORT_SSL) as self.smtp:
            # LOGIN
            self.smtp.login(self.cfg['GMAIL'].get('USER', None),
                            self.cfg['GMAIL'].get('PASS', None)
                            )
            # SEND EMAIL
            self.smtp.send_message(self.message)

if __name__ == '__main__':
    main()

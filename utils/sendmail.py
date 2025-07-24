import smtplib,ssl
import yaml

class SendMail:
    """
    A class to handle sending emails.
    """
    def __init__(self, subject, message, from_email, recipient_list):
        self.subject = subject
        self.message = message
        self.from_email = from_email
        self.recipient_list = recipient_list
        self.context = ssl.create_default_context()
        self.config = self.load_email_config()
        print(self.config)
    
    def load_email_config(self):
        """
        Load email configuration from a YAML file.
        """
        with open('./configs/email.yaml', 'r') as file:
            return yaml.safe_load(file)


    def send(self):
        """
            Sending the email.
        """
        try:
            server = smtplib.SMTP(self.config['server'], self.config['port'])
            server.starttls()
            server.login(self.config['email']['user'], self.config['email']['password'])    
            server.sendmail(self.from_email, self.recipient_list, f"Subject: {self.subject}\n\n{self.message} ")
            return "Email sent successfully"
        except Exception as e:
            return  f"Error sending email: {e}"
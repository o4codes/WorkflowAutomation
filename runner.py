from core.tasks import SendEmail, SendSMS

send_email_task = SendEmail("email@mail.com")
send_sms_task = SendSMS("07068360667")

send_email_task.attach_observer(send_sms_task)

send_email_task.execute()
send_email_task.notify()
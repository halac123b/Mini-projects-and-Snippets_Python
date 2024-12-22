import mailtrap

mail = mailtrap.Mail(
    sender=mailtrap.Address(email="hello@demomailtrap.com", name="Mailtrap Test"),
    to=[mailtrap.Address(email="halac123b@gmail.com")],
    subject="You are awesome!",
    text="Congrats for sending test email with Mailtrap!",
    category="Integration Test",
)

client = mailtrap.MailtrapClient(token="********4760")
response = client.send(mail)

print(response)
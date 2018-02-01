from gmail import GMail, Message

"c4e.201708@gmail.com"

gmail = GMail("adneytan@gmail.com","tangocanh123")
html_template = ('''<p><strong>Dear Ta Anh</strong>,&nbsp;</p>
<p>&nbsp;</p>
<p>This morning I have a {{sickness}}</p>
<p>I cannot attend your <strong>lecture</strong> today=</p>
<p><em><strong>Best regards,</strong></em></p>
<p>A</p>
<p><span style="text-decoration: underline;"><strong>Anh</strong></span></p>
'''
)

sickness_list = ["stomach", "headache","toothache", "earache"]
from random import choice
sickness = choice(sickness_list)
html_content = html_template.replace("{{sickness}}", sickness)
msg = Message("Nghi om", to="taanh1999gha@gmail.com", html=html_content)

from gmail import GMail, Message

import datetime
now = datetime.datetime.now()

gmail = GMail("adneytan@gmail.com", "tangocanh123")

html_content = ''' <p><em>Dear Professor,</em></p>
<p>I'm afraid I <strong>wasn't able to</strong> <strong>attend tomorrow lecture</strong> due to my <strong>illness</strong>. I have a headache right now and I cannot move in balance, even though I took medicine last night</p>
<p class="ui_qtext_para">I hope to be well soon and be back in school to catch up with what you've taught so far.</p>
<p class="ui_qtext_para">Yours sincerely,</p>
<p class="ui_qtext_para">Anh</p>
<p>Anh Ta</p>
'''


msg = Message("Notice from Anh TA",to="taanh1999gha@gmail.com", html=html_content)

if now.hour > 7:
    gmail.send(msg)

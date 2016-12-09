import base64
import httplib2

from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

from apiclient.discovery import build
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client import tools


# Path to the client_secret.json file downloaded from the Developer Console
CLIENT_SECRET_FILE = 'client_secret.json'

# Check https://developers.google.com/gmail/api/auth/scopes for all available scopes
OAUTH_SCOPE = 'https://www.googleapis.com/auth/gmail.compose'

# Location of the credentials storage file
STORAGE = Storage('gmail.storage')

# Start the OAuth flow to retrieve credentials
flow = flow_from_clientsecrets(CLIENT_SECRET_FILE, scope=OAUTH_SCOPE)
http = httplib2.Http()

# Try to retrieve credentials from storage or run the flow to generate them
credentials = STORAGE.get()
if credentials is None or credentials.invalid:
  credentials = tools.run_flow(flow, STORAGE, http=http)

# Authorize the httplib2.Http object with our credentials
http = credentials.authorize(http)

# Build the Gmail service from discovery
gmail_service = build('gmail', 'v1', http=http)

# create a message to send

me = "jbrookstone@gmail.com"
you = "julian.brookstone@vanwealth.co.za"

message = MIMEMultipart('alternative')
message['to'] = you
message['from'] = me
message['subject'] = "Test Email HTML"

text = "the following message is HTML"
html = """\
<div dir=3D"ltr"><div class=3D"gmail_default" style=3D"font-family:verdana,=
sans-serif;font-size:small;color:rgb(68,68,68)"><p style=3D"color:rgb(34,34=
,34);font-family:arial,sans-serif;font-size:12.8px">Hello there Julian ,<br=
><span style=3D"font-size:12.8px"><br>We=E2=80=99ve got some big news -=C2=
=A0</span><span style=3D"font-size:12.8px">another grand gathering of .gifs=
 is on the horizon</span><span style=3D"color:rgb(68,68,68);font-family:ver=
dana,sans-serif;font-size:small">!=E2=80=8B</span></p><p></p><p style=3D"co=
lor:rgb(34,34,34);font-family:arial,sans-serif">This time we will be curati=
ng a theme for our exhibition, happening=C2=A030 June 2016=C2=A0<br>at Knex=
T Art Gallery on Harrington Street<span style=3D"color:rgb(68,68,68);font-f=
amily:verdana,sans-serif">=E2=80=8B.=E2=80=8B</span><font color=3D"#000000"=
><span style=3D"font-family:verdana,sans-serif">=C2=A0<a href=3D"https://ww=
w.facebook.com/events/1734969563422866/" target=3D"_blank" data-saferedirec=
turl=3D"https://www.google.com/url?hl=3Den&amp;q=3Dhttps://www.facebook.com=
/events/1734969563422866/&amp;source=3Dgmail&amp;ust=3D1463780033747000&amp=
;usg=3DAFQjCNGAzufbMQP-TxVBgUvYl5sfq3umRg">Check out the Facebook event.</a=
></span></font></p><p style=3D"color:rgb(34,34,34);font-family:arial,sans-s=
erif"><img src=3D"https://ci6.googleusercontent.com/proxy/pnzqtLD_MqBQjOc6B=
hiGdCCUTvzze3BFhwXP9nUsGwSjS2spAumldVMIexA3zwOjCTezMwx-Qi7DBhV5t_a1Z6SnOJ1h=
JYBX9BCcXiwhRX-YUeEId_OSA_-3W29GzyycQtix9gHxRuOMg1VY_4OsIECgovZY-6E=3Ds0-d-=
e1-ft#http://66.media.tumblr.com/e62f0b86dda69933e45293ccb543e321/tumblr_o7=
340xTab41v4rpnpo2_r1_500.gif" width=3D"344" height=3D"344" style=3D"font-si=
ze:12.8px;margin-right:0px"></p><p style=3D"color:rgb(34,34,34);font-family=
:arial,sans-serif"><b style=3D"font-size:xx-large;background-color:rgb(255,=
242,204)"><font color=3D"#0000ff">inreallife.gif</font></b><font size=3D"6"=
><span style=3D"background-color:rgb(255,242,204)">=C2=A0<br></span></font>=
<font style=3D"font-size:12.8px"><span style=3D"font-size:small"><br>Use dr=
awings, animations, photos of your=C2=A0</span></font><span style=3D"color:=
rgb(0,0,0);font-family:verdana,sans-serif">toasters</span><span style=3D"co=
lor:rgb(0,0,0)">, 3D models, collage, code, or any other=C2=A0</span><span =
style=3D"color:rgb(0,0,0)">medium you can or can=E2=80=99t imagine, to inte=
rpret this theme how you wish.<br></span><b style=3D"color:rgb(0,0,0);font-=
size:12.8px"><br>Submission Deadline: 24/06/16<br></b><b style=3D"color:rgb=
(0,0,0);font-size:12.8px">Submission Details to follow soon<br></b><span st=
yle=3D"color:rgb(0,0,0);font-size:12.8px"><b><br></b>We=E2=80=99ve got a sp=
ecial place in our hearts for all previously featured artists and we=E2=80=
=99d love for you t</span><span style=3D"color:rgb(0,0,0);font-size:12.8px"=
>o be a part of=C2=A0</span><span style=3D"font-family:verdana,sans-serif;c=
olor:rgb(68,68,68)">=E2=80=8Bthis=E2=80=8B=C2=A0</span><span style=3D"color=
:rgb(0,0,0);font-size:12.8px">event.=C2=A0</span><span style=3D"color:rgb(0=
,0,0);font-size:12.8px">After all, where would we be without you!<br></span=
><span style=3D"color:rgb(0,0,0);font-size:12.8px"><br>You=E2=80=99ll be he=
aring more from us in the coming weeks - consider this a heads up to get yo=
ur gears=C2=A0</span><font color=3D"#000000" style=3D"font-size:12.8px">tur=
ning and churning up some .gif goodnes</font><span style=3D"color:rgb(0,0,0=
);font-family:verdana,sans-serif">=E2=80=8Bs!=E2=80=8B</span></p></div><div=
><div><div dir=3D"ltr"><div><div dir=3D"ltr"><div dir=3D"ltr"><div dir=3D"l=
tr"><div dir=3D"ltr"><div dir=3D"ltr"><div dir=3D"ltr"><div><div dir=3D"ltr=
"></div></div><div><div dir=3D"ltr"><div dir=3D"ltr"><table border=3D"0" ce=
llspacing=3D"0" cellpadding=3D"0" style=3D"font-size:12.8px;border-collapse=
:collapse;border:none"><tbody><tr><td width=3D"94" valign=3D"top" style=3D"=
width:70.65pt;padding:0cm 5.4pt"><table border=3D"0" cellspacing=3D"0" cell=
padding=3D"0" style=3D"font-size:12.8px;border-collapse:collapse;border:non=
e"><tbody><tr style=3D"height:64.3pt"><td width=3D"85" valign=3D"top" style=
=3D"width:63.9pt;padding:0in 5.4pt;height:64.3pt"><p style=3D"margin-bottom=
:0.0001pt"><img src=3D"https://ci4.googleusercontent.com/proxy/TMTONrMNPYM1=
0XeHq8H9jKQ6UDtBomvdf5dZhrbgTXh-a1aDUgEzx3xGI-olOHFnbvoCZZ5RnqgXDcub9FCJM9J=
QWOyWRJpgfdkRUAwbBXKSJhqxQHBYZQ8G84VKJLjkLpMC-XBwzUGoP4jqjIGvKkLdtcEY_JZwqJ=
EWclx-BKQ3XsHs8g5_gaMCndooHSg_i-D84zxUz8WFIYA=3Ds0-d-e1-ft#https://docs.goo=
gle.com/uc?export=3Ddownload&amp;id=3D0B4aIS_d818wER2l2WEpGcFpRWU0&amp;revi=
d=3D0B4aIS_d818wEM0theDV0NEhCUnlJVDRxclFFVDJPYVJnVmNRPQ" width=3D"197" heig=
ht=3D"200" style=3D"font-size:12.8px">=C2=A0</p></td><td width=3D"144" vali=
gn=3D"top" style=3D"width:1.5in;padding:0in 5.4pt;height:64.3pt"><p style=
=3D"margin-bottom:0.0001pt"><br><br></p><p style=3D"margin-bottom:0.0001pt"=
><b style=3D"font-family:arial,helvetica,sans-serif"><span style=3D"color:r=
gb(153,153,153)"><font size=3D"4">Regards<br></font></span></b><b style=3D"=
font-size:12.8px;font-family:arial,helvetica,sans-serif"><font size=3D"6" c=
olor=3D"#ffff00" style=3D"background-color:rgb(159,197,232)">exhibit.gif=C2=
=A0<br></font></b><b style=3D"font-size:12.8px;font-family:arial,helvetica,=
sans-serif"><span style=3D"color:rgb(166,166,166)"><font size=3D"1">The Tea=
m=C2=A0</font></span></b></p><p style=3D"margin-bottom:0.0001pt"><b style=
=3D"font-size:12.8px"><span style=3D"font-size:9pt;color:rgb(31,73,125)"><b=
r></span></b><span style=3D"background-color:rgb(255,255,255)"><b><font col=
or=3D"#0b5394">Facebook</font></b></span> =C2=A0 <b><font color=3D"#6fa8dc"=
>Tumblr</font></b><b style=3D"font-size:12.8px"><span style=3D"font-size:9p=
t;color:rgb(31,73,125)"><br></span></b></p></td></tr></tbody></table><p sty=
le=3D"margin-bottom:12pt;background-image:initial;background-repeat:initial=
">=C2=A0</p><p style=3D"margin-bottom:12pt;background-image:initial;backgro=
und-repeat:initial">






</p><p style=3D"margin-bottom:12pt;background-image:initial;background-repe=
at:initial">=C2=A0</p>

</td><td width=3D"507" valign=3D"top" style=3D"width:380.15pt;padding:0cm 5=
.4pt"><font size=3D"1"><br><br><br><br><br></font><p style=3D"margin-bottom=
:0.0001pt"><br></p><p style=3D"margin-bottom:0.0001pt"><br></p><p style=3D"=
margin-bottom:0.0001pt"><br></p><div><b style=3D"font-size:12.8px"><font co=
lor=3D"#ffffff" size=3D"4" style=3D"background-color:rgb(255,0,255)"><br></=
font></b></div></td></tr></tbody></table></div></div></div></div></div></di=
v></div></div></div></div></div></div></div>
</div>
"""

#recoding the MIME types of both parts - text/plain and text/html
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html', "utf-8")

#attach parts into message container
message.attach(part1)
message.attach(part2)

body = {'raw': base64.urlsafe_b64encode(message.as_string().encode("utf-8"))}

# send it
try:
  message = (gmail_service.users().messages().send(userId="me", body=body).execute())
  print('Message Id: %s' % message['id'])
  print(message)
except Exception as error:
  print('An error occurred: %s' % error)
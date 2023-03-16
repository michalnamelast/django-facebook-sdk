# django-facebook-sdk

Create you facebook app at https://developers.facebook.com
Get the App ID and App secret from Settings > Basic
Set your app mode 'Live' # No required on localhost
Install the Facebook Login product 
Settings > Basic > Site URL: https://www.your-website.com/


Clone the repo
RUN python -m venv "venv"
source venv/bin/activate
pip -r install requirements.txt

website > facebook_logging > views.py

FACEBOOK_APP_ID = 'YOUR APP ID' # don't forget ''
FACEBOOK_APP_SECRET = 'YOUR APP SECRET' # don't forget ''
FACEBOOK_REDIRECT_URI = 'https://www.your-website.com/facebook-login-callback/'  # http or https, don't forget about '/' at the end


Place exatly same FACEBOOK_REDIRECT_URI in Facebook app > Facebook Login > Settings > Valid OAuth Redirect URIs
Hope it will helpfull

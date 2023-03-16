from django.shortcuts import render, redirect
from django.urls import reverse


FACEBOOK_APP_ID = 'YOUR APP ID'
FACEBOOK_APP_SECRET = 'YOUR APP SECRET'
FACEBOOK_REDIRECT_URI = 'https://www.your-website.com/facebook-login-callback/'


def index(request):
    return render(request, 'index.html', {})


def facebook_login(request):
    redirect_uri = FACEBOOK_REDIRECT_URI
    login_url = 'https://www.facebook.com/v12.0/dialog/oauth?client_id={}&redirect_uri={}&state={}'.format(
        FACEBOOK_APP_ID, redirect_uri, 'some-random-string')

    return redirect(login_url)


def facebook_login_callback(request):
    # Extract the access token from the Facebook API response
    code = request.GET.get('code')
    redirect_uri = FACEBOOK_REDIRECT_URI
    token_url = 'https://graph.facebook.com/v12.0/oauth/access_token?client_id={}&redirect_uri={}&client_secret={}&code={}'.format(
        FACEBOOK_APP_ID, redirect_uri, FACEBOOK_APP_SECRET, code)

    response = requests.post(token_url)
    data = response.json()
    access_token = data.get('access_token')

    # Use the access token to make requests to the Facebook API
    graph = facebook.GraphAPI(access_token=access_token)
    user_info = graph.get_object('me', fields='id,email,first_name,last_name')

    # # You can now use user_info to create or authenticate a user in your system
    print('Username:', user_info.get('first_name'))
    print('Lastname:', user_info.get('last_name'))
    print('Email:', user_info.get('email'))

    # Redirect the user to the appropriate page
    return redirect('/')
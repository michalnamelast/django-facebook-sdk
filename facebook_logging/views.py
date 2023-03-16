from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login


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
    user_id = user_info.get('id')
    first_name = user_info.get('first_name')
    last_name = user_info.get('last_name')
    email = user_info.get('email')
    user = User.objects.filter(pk=user_id)
    if not user:
        user = User.objects.create(
            pk=user_id,
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        user.save()

    login(request, user[0])

    # Redirect the user to the appropriate page
    return redirect('/')
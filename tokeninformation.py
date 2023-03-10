import requests
import json

SCOPE_DESCRIPTIONS = {
    'analytics:read:extensions': 'View analytics for your extensions',
    'analytics:read:games': 'View analytics for your games',
    'bits:read': 'View bits information',
    'channel:edit:commercial': 'Run commercials on your channel',
    'channel:manage:broadcast': 'Manage your channel broadcasts',
    'channel:manage:extensions': 'Manage your channel extensions',
    'channel:manage:polls': 'Manage your channel polls',
    'channel:manage:predictions': 'Manage your channel predictions',
    'channel:manage:redemptions': 'Manage your channel rewards',
    'channel:manage:schedule': 'Manage your channel schedule',
    'channel:manage:videos': 'Manage your channel videos',
    'channel:read:editors': 'View your channel editors',
    'channel:read:hype_train': 'View your hype train events',
    'channel:read:polls': 'View your channel polls',
    'channel:read:predictions': 'View your channel predictions',
    'channel:read:redemptions': 'View your channel rewards',
    'channel:read:stream_key': 'View your stream key',
    'channel:read:subscriptions': 'View your channel subscriptions',
    'clips:edit': 'Manage your clips',
    'clips:read': 'View your clips',
    'moderation:read': 'View your moderation events',
    'moderation:write': 'Manage your moderation events',
    'openid': 'Authenticate using OpenID Connect',
    'user:edit': 'Change your user information',
    'user:edit:password': 'Change your user password',
    'user:manage:blocked_users': 'Manage your blocked users',
    'user:read:broadcast': 'View your broadcasts and VODs',
    'user:read:follows': 'View your follows',
    'user:read:subscriptions': 'View your subscriptions',
    'channel:moderate': 'Moderate your channel',
    'chat:edit': 'Edit your chat settings',
    'chat:read': 'Read messages in your chat',
    'whispers:edit': 'Edit your whisper settings',
    'whispers:read': 'Read whispers sent to you',
    'user:edit:follows': 'Edit who you follow',
    'user:read:email': 'View your email address',
    'channel:read:automod_message': 'View your AutoMod messages',
    'user:read:editors': 'View your channel editors',
    'user:read:stream_key': 'View your stream key',
    'channel:read:teams': 'View your channel teams',
    'user:edit:oauth:client-credentials': 'Manage your applications',
    'channel:manage:teams': 'Manage your channel teams',
    'user:manage:extensions': 'Manage your extensions',
    'user:manage:blocked_users:edit: Follow your blocked users'
    'moderation:manage:automod': 'Manage your AutoMod settings',
    'moderator:manage:automod': 'Manage AutoMod for your channels',
    'user:edit:follows': 'Edit who you follow',
    'channel:manage:broadcast:rerun': 'Run reruns of your broadcasts',
    'channel:read:redemptions': 'View your channel rewards',
    'clips:edit:owned': 'Edit your owned clips',
    'user:edit:broadcast': 'Start and stop broadcasts',
    'user:edit:redemptions': 'Create and delete your rewards',
    'user:read:email:edit': 'View and edit your email address',
    'bits:manage': 'Manage your bits',
    'channel:read:achievements': 'View your channel achievements',
    'channel:read:subscriptions:edit': 'View and edit your channel subscriptions',
    'user:edit:channels': 'Manage your channel list',
    'user:edit:communities': 'Manage your communities',
    'user:edit:subcriptions:edit': 'Edit your subscriptions',
    'user:manage:channels': 'Manage your channels',
    'user:manage:communities': 'Manage your communities',
    'user:read:channels': 'View your channels',
    'user:read:subscriptions:edit': 'View and edit your subscriptions',
    'moderator:read:shield_mode': 'Get information about Shield Mode and Shield Mode settings in channels where you have the moderator role',
    'moderator:manage:shield_mode': 'Manage Shield Mode and Shield Mode settings in channels where you have the moderator role'
    
}

def get_scope_descriptions(scopes):
    descriptions = []
    for scope in scopes:
        if scope in SCOPE_DESCRIPTIONS:
            descriptions.append(SCOPE_DESCRIPTIONS[scope])
        else:
            descriptions.append(scope)
    return descriptions

def get_token_info(token):
    url = 'https://id.twitch.tv/oauth2/validate'
    headers = {'Authorization': f'OAuth {token}'}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print('Error retrieving token info')
        return
    token_info = json.loads(response.text)
    return token_info

while True:
    try:
        token = input('Enter your Twitch OAuth token: ')
        if token == 'exit':
            break
        token_info = get_token_info(token)
        if token_info is not None:
            print(f'Token information for user {token_info["login"]}:')
            print(f'User ID: {token_info["user_id"]}')
            print(f'Expires in: {token_info["expires_in"]} seconds')
            print('Permissions/Scopes:')
            scope_descriptions = get_scope_descriptions(token_info['scopes'])
            for i, scope in enumerate(scope_descriptions):
                print(f' {i+1}. {scope}')
    except Exception as e:
        print(f'Error: {str(e)}')

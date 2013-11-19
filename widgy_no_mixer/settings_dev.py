DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'widgy_db',
    }
}

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

# Hijack all emails and send them to the BANDIT_EMAIL address
EMAIL_BACKEND = 'bandit.backends.smtp.HijackSMTPBackend'
BANDIT_EMAIL = 'plee@fusionbox.com'

# Dev DSN Value
SENTRY_DSN = ''

# Tell raven to report errors even when debug is True
RAVEN_CONFIG = {
    'register_signals': True,
}

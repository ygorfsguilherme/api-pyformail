import environ
env = environ.Env()

FROM_EMAIL = env('FROM_EMAIL')
TO_EMAIL = env('TO_MAIL')
PASS_EMAIL = env('PASS_EMAIL')
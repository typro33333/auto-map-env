# Detect key
# Define the string have secret key

secret_key = ['KEY','SECRET', 'PASSWORD', 'SECRET_KEY', 'ACCESS_KEY', 'KEY', 'CLIENT_SECRET', 'SECRET', 'PASSWORD', 'TOKEN']
def detect_secret_manual_simple(key):
  for i in secret_key:
    if i in key:
      return True
  return False
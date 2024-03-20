import os

# Define the database location inside the 'utils' folder
DB_PATH = os.path.join(os.path.dirname(__file__), "db")

# We try to match the render hostname first
BASE_URL = os.environ.get("RENDER_EXTERNAL_HOSTNAME")

# We need a base URL for Twilio to talk to:
# If you're self-hosting and have an open IP/domain, set it here or in your env.
# Ensure the base url is set in the following format: subdomain.domain.com
if not BASE_URL:
    BASE_URL = os.environ.get("BASE_URL")
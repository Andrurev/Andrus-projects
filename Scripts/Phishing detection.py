# Import the required libraries
import email
import urllib

# Parse the email message
msg = email.message_from_string(raw_msg)

# Extract the sender's email address
sender = msg["From"]

# Check for common phishing indicators
if "https://" not in msg["Subject"]:
    print("Suspicious subject line")
if "unsubscribe" not in msg["List-Unsubscribe"]:
    print("Suspicious List-Unsubscribe header")
if "http://" in sender or ".com" in sender:
    print("Suspicious sender email address")

# Extract the URLs from the email body
body = msg.get_payload()
urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', body)

# Check the URLs for potential phishing
for url in urls:
    try:
        # Check the domain name in the URL
        domain = urllib.parse.urlparse(url).netloc
        if "example.com" not in domain:
            print("Suspicious URL: " + url)
    except:
        # Ignore invalid URLs
        pass
This script uses the email and urllib libraries to parse the email message and extract the sender's email address, the subject line, and the URLs from the email body. It then checks for common phishing indicators, such as a suspicious subject line, a suspicious sender email address, or a suspicious List-Unsubscribe header. It also checks the URLs for potential phishing by comparing the domain names in the URLs against a trusted domain name (e.g. example.com).

You can modify the script to add additional checks for phishing indicators, and to customize the trusted domain name. You can also use this script as part of a larger email filtering system to automatically identify and block phishing emails.

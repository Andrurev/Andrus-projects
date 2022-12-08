# Import the required libraries
import splunklib.client as client
import splunklib.results as results

# Create a new Splunk client
service = client.connect(
    host="splunk_server_hostname",
    port=8089,
    username="splunk_username",
    password="splunk_password"
)

# Define the search query
query = 'search index=my_index * | head 5'

# Run the search and get the results
results = service.jobs.oneshot(query, exec_mode="blocking")

# Loop through the results and print them
for result in results.results():
    print(result)

# Create a new alert
alert = service.saved_searches.create(
    "My Alert",
    query,
    "*/15 * * * *"
)

# Set the alert to run automatically
alert.update(
    action.email="my_email@example.com",
    action.email.sendresults="True"
)

# Disconnect from the Splunk server
service.disconnect()

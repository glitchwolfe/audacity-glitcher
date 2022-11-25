# Import the module:
import pipeclient
# Create a client instance:
client = pipeclient.PipeClient()
# Send a command:
client.write("Command", timer=True)
# Read the last reply:
print(client.read())
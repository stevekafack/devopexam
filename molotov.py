#section 1.4
import json
import molotov

@molotov.scenario(100)  # Define the number of concurrent users for the load test
async def scenario(session):
    async with session.get('http://example.com/api/endpoint') as response:
        data = await response.json()

        # Check if the response status is 200
        if response.status == 200:
            # Perform additional checks on the JSON response if needed
            # ...

            # Print the response data
            print(data)

# open a terminal navigateto this python file and run the below command Molotov will execute the load test scenario with the specified number of concurrent users.
# molotov load_test.py
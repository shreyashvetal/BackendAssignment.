==========================================================================================================
Project Name: Backend Assignment
==========================================================================================================
Installation

Create a Python 3 virtual environment.
"python3 -m venv venv"
Activate the virtual environment.

On macOS and Linux:
"source venv/bin/activate"
On Windows:
"venv\Scripts\activate"

Install project dependencies using pip.
"pip install -r req.txt"

Configure your PostgreSQL database details in the settings.py file.

Apply database migrations.
"python manage.py migrate"

==========================================================================================================
Running the Project

Start the Django development server.
"python manage.py runserver"
The server will be available at http://127.0.0.1:8000.

API Authentication and Whitelisting
Before executing the API requests, please note that the "user/create" and "user/generate_token" APIs are exempted from JWT token authentication for now, 
considering that IP whitelisting will be implemented for requests. The current settings allow all IPs to access the APIs. You can restrict access by providing a list of 
allowed IPs in the ALLOWED_HOSTS setting.
==========================================================================================================

API Curl Requests
1 create user API :
curl --location 'http://localhost:8000/api/v1/user/create/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username":"shreyash",
    "email":"shreyasvetal99@gmail.com",
    "password":"test"
}'

2. generate authentication token for user :
curl --location 'http://localhost:8000/api/v1/user/generate_token/' \
--header 'Content-Type: application/json' \
--data '{
    "username":"shreyash",
    "password":"test"
}'

3. create post API :
curl --location 'http://localhost:8000/api/v1/post/create/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk3Mjg0OTQ0LCJpYXQiOjE2OTcyODEzNDQsImp0aSI6ImNhZDVjN2RkY2UwMDRmNWRiMzYxMmYxODJhMzIyMzBlIiwidXNlcl9pZCI6MX0.aMVjhOEqwCVxmvey0cOiE935-fP3pacswauBXdTAdGM' \
--data '{
    "title":"test",
    "content":"testing1"
}'
Please ensure that you replace the Authorization header in the "Create Post API" request with a valid JWT token as per your use case.
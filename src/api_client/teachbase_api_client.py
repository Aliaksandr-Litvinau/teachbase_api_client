import requests

from config import settings


class TeachbaseClient:
    def __init__(self):
        self.client_id = settings.CLIENT_ID
        self.client_secret = settings.CLIENT_SECRET
        self.base_url = settings.TEACHBASE_API_BASE_URL
        self.access_token = None

    def authorize(self):
        """
        Obtains an access token from Teachbase API using the OAuth2 authorization flow
        """
        url = 'https://go.teachbase.ru/oauth/token'
        payload = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'grant_type': 'client_credentials'
        }
        response = requests.post(url, data=payload)
        response.raise_for_status()
        self.access_token = response.json()['access_token']

    def get(self, endpoint):
        """
        Sends a GET request to Teachbase API with the given endpoint and returns the response JSON.
        """
        url = f"{self.base_url}{endpoint}"
        headers = {"Authorization": f"Bearer {self.access_token}"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def post(self, endpoint, data):
        """
        Sends a POST request to Teachbase API with the given endpoint and data and returns the response JSON.
        """
        url = f"{self.base_url}{endpoint}"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json",
        }
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()

    def get_courses(self):
        """
        Retrieves the list of courses from Teachbase API
        """
        return self.get("/endpoint/v1/courses")

    def get_course_details(self, course_id):
        """
        Gets the detailed view of a course
        """
        return self.get(f"/endpoint/v1/courses/{course_id}")

    def create_user(self, request):
        """
        Creates a new user
        """
        return self.post("/endpoint/v1/users/create", request)

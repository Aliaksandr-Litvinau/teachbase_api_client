import unittest
from unittest.mock import patch
from teachbase_api_client import TeachbaseClient


class TestTeachbaseClient(unittest.TestCase):

    @patch('requests.post')
    def test_authorize_returns_access_token(self, mock_post):
        # Set up the mock response for requests.post
        mock_post.return_value.json.return_value = {'access_token': 'test_token'}

        # Initialize a TeachbaseClient object
        client = TeachbaseClient()

        # Call the authorize method
        client.authorize()

        # Assert that the access_token attribute of the object is not None
        self.assertIsNotNone(client.access_token)

    @patch('requests.get')
    def test_get_courses_returns_list_of_courses(self, mock_get):
        # Set up the mock response for requests.get
        mock_get.return_value.json.return_value = [{'id': 1, 'name': 'Course 1'}, {'id': 2, 'name': 'Course 2'}]

        # Initialize a TeachbaseClient object and authorize it
        client = TeachbaseClient()

        # Call the get_courses method
        courses = client.get_courses()

        # Assert that the returned value is a list with the expected number of elements
        self.assertIsInstance(courses, list)
        self.assertEqual(len(courses), 2)

        # Assert that each element of the list is a dictionary with the expected keys
        for course in courses:
            self.assertIsInstance(course, dict)
            self.assertIn('id', course)
            self.assertIn('name', course)

    @patch('requests.post')
    def test_post_returns_valid_json_response(self, mock_post):
        # Set up the mock response for requests.post
        mock_post.return_value.json.return_value = {'status': 'success', 'message': 'User created successfully'}

        # Initialize a TeachbaseClient object and authorize it
        client = TeachbaseClient()

        # Call the post method with a sample request and endpoint
        endpoint = '/endpoint/v1/users/create'
        data = {'name': 'John Doe', 'email': 'johndoe@example.com'}
        response = client.post(endpoint, data)

        # Assert that the returned value is a dictionary with the expected keys and values
        self.assertIsInstance(response, dict)
        self.assertEqual(response['status'], 'success')
        self.assertEqual(response['message'], 'User created successfully')

    @patch('requests.get')
    def test_get_course_details_returns_valid_response(self, mock_get):
        # Set up the mock response for requests.get
        mock_get.return_value.json.return_value = {'id': 123, 'name': 'Introduction to Python'}

        # Initialize a TeachbaseClient object and authorize it
        client = TeachbaseClient()

        # Call the get_course_details method with a valid course_id
        course_id = 123
        response = client.get_course_details(course_id)

        # Assert that the returned value is a dictionary with the expected keys and values
        self.assertIsInstance(response, dict)
        self.assertEqual(response['id'], 123)
        self.assertEqual(response['name'], 'Introduction to Python')

    @patch('requests.get')
    def test_get_course_sessions_returns_valid_response(self, mock_get):
        # Set up the mock response for requests.get
        mock_get.return_value.json.return_value = [{'id': 123, 'name': 'Session 1'}, {'id': 456, 'name': 'Session 2'}]

        # Initialize a TeachbaseClient object and authorize it
        client = TeachbaseClient()

        # Call the get_course_sessions method with a valid course_id
        course_id = 789
        response = client.get_course_sessions(course_id)

        # Assert that the returned value is a list with at least one element
        self.assertIsNotNone(response)
        self.assertIsInstance(response, list)
        self.assertGreaterEqual(len(response), 1)

    @patch('requests.post')
    def test_register_user_for_session(self, mock_post):
        # Set up the mock response for requests.post
        mock_post.return_value.json.return_value = {
                "id": 3,
                "name": "Fantastic Steel Table",
                "started_at": "2016-07-27T16:26:21.286+03:00",
                "finished_at": "2016-07-30T16:26:21.287+03:00",
                "course_id": 3,
                "infinitely": True,
                "access_type": "open",
                "finished": False,
                "navigation": None,
                "apply_url": "http://go.teachbase.ru/course_sessions/sleek-rubber-pants-07-27/apply",
                "deadline_soon": True,
                "assignments_count": 0,
                "deadline_type": 0,
                "slug": "sleek-rubber-pants-07-27",
                "period": 10,
                "labels": [
                    {
                        "id": 5,
                        "name": "Beauty & Home",
                        "group_id": None
                    }
                ],
                "course": {
                    "id": 0,
                    "account_id": 0,
                    "name": "string",
                    "created_at": "2016-07-20T14:54:31.903+03:00",
                    "updated_at": "2016-07-20T14:54:31.903+03:00",
                    "owner_id": 0,
                    "owner_name": "string",
                    "thumb_url": "string",
                    "cover_url": "string",
                    "description": "string",
                    "last_activity": "2016-07-20T14:54:31.903+03:00",
                    "total_score": 0,
                    "total_tasks": 0,
                    "unchangeable": True,
                    "include_weekly_report": True,
                    "content_type": 0,
                    "types": [
                        {
                            "id": 1,
                            "name": "Lorem ipsum",
                            "created_at": "2016-07-20T14:54:31.903+03:00",
                            "updated_at": "2016-07-20T14:54:31.903+03:00"
                        }
                    ],
                    "is_netology": True,
                    "bg_url": "string",
                    "video_url": "string",
                    "demo": True,
                    "custom_author_names": "string",
                    "authors": [
                        {
                            "id": 1,
                            "email": "email_1_1@factory.tb",
                            "phone": "79525557412",
                            "name": "Dandre",
                            "last_name": "Fay",
                            "role_id": 1,
                            "auth_type": 0,
                            "last_activity_at": 1550260005,
                            "is_active": True,
                            "created_at": "2018-05-28T17:32:20+00:00",
                            "updated_at": "2019-04-11T06:21:32+00:00"
                        }
                    ],
                    "custom_contents_link": "string",
                    "hide_viewer_navigation": True,
                    "duration": 0,
                    "competences": [
                        "string"
                    ]
                }
            }

        # Initialize a TeachbaseClient object and authorize it
        client = TeachbaseClient()

        # Replace with a valid session ID and user data
        session_id = 1
        user_data = {'name': 'John Doe', 'email': 'johndoe@example.com'}

        response = client.register_user_for_session(session_id, user_data)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, dict)
        self.assertGreater(len(response), 0)


if __name__ == '__main__':
    unittest.main()

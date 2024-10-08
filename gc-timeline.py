from __future__ import print_function
import datetime
import os.path
import dateutil.parser

from google.oauth2 import credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']

def main():
    """Creates events in the user's Google Calendar."""
    creds = None
    # Token file stores the user's access and refresh tokens.
    if os.path.exists('token.json'):
        creds = credentials.Credentials.from_authorized_user_file('token.json', SCOPES)
    # If no valid credentials, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save credentials for next run.
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)

        # Define the events based on the plan
        events = [
            # Phase 1 Events
            {
                'summary': 'Improve Clarity and CTA Placement',
                'description': (
                    'Phase: Phase 1\n'
                    'Priority: High\n'
                    'Timing: 1-2 days\n'
                    'Tags: Quick Wins\n\n'
                    'Task: Review and optimize the current product descriptions to make them even clearer. '
                    'Ensure the CTA button is above the fold and prominent.\n\n'
                    'Details: Conduct usability testing on the placement of CTAs and ensure product descriptions focus on user needs.'
                ),
                'start': {'date': '2024-10-09'},
                'end': {'date': '2024-10-10'},
            },
            {
                'summary': 'Add Trust Badges and Certifications',
                'description': (
                    'Phase: Phase 1\n'
                    'Priority: High\n'
                    'Timing: 1-2 days\n'
                    'Tags: Quick Wins\n\n'
                    'Task: Add ISO certifications, industry awards, and any relevant trust badges to the landing pages.\n\n'
                    'Details: Display these prominently near CTAs or the product description section.'
                ),
                'start': {'date': '2024-10-11'},
                'end': {'date': '2024-10-12'},
            },
            {
                'summary': 'Simplify Forms',
                'description': (
                    'Phase: Phase 1\n'
                    'Priority: High\n'
                    'Timing: 3-5 days\n'
                    'Tags: Quick Wins\n\n'
                    'Task: Reduce the number of form fields and create a simple, user-friendly contact/quote form similar to Tinkoff.\n\n'
                    'Details: Focus on essential fields only. A/B test the simplified version vs. the current one.'
                ),
                'start': {'date': '2024-10-12'},
                'end': {'date': '2024-10-15'},
            },
            {
                'summary': 'Add Customer Testimonials and Case Studies',
                'description': (
                    'Phase: Phase 1\n'
                    'Priority: High\n'
                    'Timing: 5-7 days\n'
                    'Tags: Quick Wins\n\n'
                    'Task: Research competitors’ examples and add testimonials from key clients in B2B sectors.\n\n'
                    'Details: Create a dedicated section for case studies and testimonials with logos of well-known clients.'
                ),
                'start': {'date': '2024-10-13'},
                'end': {'date': '2024-10-18'},
            },
            {
                'summary': 'Enhance Social Proof through Clients',
                'description': (
                    'Phase: Phase 1\n'
                    'Priority: High\n'
                    'Timing: 5-7 days\n'
                    'Tags: Quick Wins\n\n'
                    'Task: Implement additional customer stories and testimonials to increase social proof.\n\n'
                    'Details: Gather real-life usage examples, possibly by conducting customer interviews.'
                ),
                'start': {'date': '2024-10-13'},
                'end': {'date': '2024-10-18'},
            },
            # Phase 2 Events
            {
                'summary': 'Test Discount/Free Trial Offers',
                'description': (
                    'Phase: Phase 2\n'
                    'Priority: Medium\n'
                    'Timing: 1-2 weeks\n'
                    'Tags: Testing and Iteration\n\n'
                    'Task: Develop a discount or free sample offer to test how it impacts conversion rates.\n\n'
                    'Details: A/B test the offer on specific ad campaigns or landing pages. Measure conversion lift.'
                ),
                'start': {'date': '2024-10-19'},
                'end': {'date': '2024-10-26'},
            },
            {
                'summary': 'Develop Industry-Specific Use Cases',
                'description': (
                    'Phase: Phase 2\n'
                    'Priority: Medium\n'
                    'Timing: 2-3 weeks\n'
                    'Tags: Testing and Iteration\n\n'
                    'Task: Brainstorm and develop specific use cases for each industry (medical, industrial, retail).\n\n'
                    'Details: Work with content writers and product teams to craft compelling use cases that resonate with your core audience.'
                ),
                'start': {'date': '2024-10-19'},
                'end': {'date': '2024-11-09'},
            },
            {
                'summary': 'Test Different CTA Text',
                'description': (
                    'Phase: Phase 2\n'
                    'Priority: Medium\n'
                    'Timing: 1-2 weeks\n'
                    'Tags: Testing and Iteration\n\n'
                    'Task: A/B test different CTA texts like "Request a Free Quote" or "Get More Information."\n\n'
                    'Details: Roll out variants on different campaigns and pages.'
                ),
                'start': {'date': '2024-10-19'},
                'end': {'date': '2024-11-02'},
            },
            # Phase 3 Events
            {
                'summary': 'Video Production',
                'description': (
                    'Phase: Phase 3\n'
                    'Priority: Medium\n'
                    'Timing: 2-3 months\n'
                    'Tags: Strategic Initiatives\n\n'
                    'Task: Create a video showcasing your production process and product use cases.\n\n'
                    'Details: Engage a video production team to script and shoot the video. Ensure it\'s optimized for both the website and social media.'
                ),
                'start': {'date': '2024-11-10'},
                'end': {'date': '2025-01-31'},
            },
            {
                'summary': 'Develop Interactive Product Calculator/Demo',
                'description': (
                    'Phase: Phase 3\n'
                    'Priority: Medium\n'
                    'Timing: 3 months\n'
                    'Tags: Strategic Initiatives\n\n'
                    'Task: Develop an interactive tool for customers to calculate costs or visualize benefits.\n\n'
                    'Details: Work with the development team to create an easy-to-use tool for B2B customers.'
                ),
                'start': {'date': '2024-11-10'},
                'end': {'date': '2025-01-31'},
            },
            {
                'summary': 'Form Progressive Disclosure',
                'description': (
                    'Phase: Phase 3\n'
                    'Priority: Medium\n'
                    'Timing: 1 month\n'
                    'Tags: Strategic Initiatives\n\n'
                    'Task: Redesign forms to include multi-step, progressive disclosure with a progress bar.\n\n'
                    'Details: Break down longer forms into manageable steps to encourage completion.'
                ),
                'start': {'date': '2024-11-10'},
                'end': {'date': '2024-12-10'},
            },
        ]

        # Insert events into Google Calendar
        calendar_id = 'primary'  # Use the primary calendar
        for event in events:
            event_result = service.events().insert(calendarId=calendar_id, body=event).execute()
            print('Event created: %s' % event_result.get('htmlLink'))

    except HttpError as error:
        print('An error occurred: %s' % error)

if __name__ == '__main__':
    main()

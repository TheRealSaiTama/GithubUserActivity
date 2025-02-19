import requests
import sys
from tabulate import tabulate

def fetchactivity(username):
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error: unable to fetch data for user {username}. Status code: {response.status_code}")
        return []
    return response.json()

def formatactivity(activity):
    eventtype = activity['type']
    reponame = activity['repo']['name']

    if eventtype == 'PushEvent':
        commitcount = len(activity['payload']['commits'])
        return f"Pushed {commitcount} commit(s) to {reponame}"
    elif eventtype == 'IssuesEvent':
        action = activity['payload']['action']
        return f"{action.capitalize()} an issue on {reponame}"
    elif eventtype == 'WatchEvent':
        return f"Starred {reponame}"
    else:
        return f"{eventtype} on {reponame}"

def filteractivity(activities, eventtype=None):
    if eventtype:
        return [activity for activity in activities if activity['type'] == eventtype]
    return activities

def main():
    if len(sys.argv) < 2:
        print("Usage: github-activity <username> [eventtype]")
        sys.exit(1)

    username = sys.argv[1]
    eventtype = sys.argv[2] if len(sys.argv) > 2 else None

    activities = fetchactivity(username)

    if not activities:
        print(f"No recent activity found for user {username}")
        return

    filteredactivities = filteractivity(activities, eventtype)

    if not filteredactivities:
        if eventtype:
            print(f"No recent activity of type {eventtype} found for user {username}")
        else:
            print(f"No recent activity found for user {username}")
        return

    table = [[formatactivity(activity)] for activity in filteredactivities]
    print(tabulate(table, headers=['Activity'], tablefmt='grid'))

if __name__ == '__main__':
    main()

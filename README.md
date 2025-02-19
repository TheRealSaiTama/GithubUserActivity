# GitHub User Activity

![GitHub User Activity](https://img.shields.io/badge/GitHub-User%20Activity-blue)

A command-line interface (CLI) tool to fetch and display the recent activity of a GitHub user in the terminal.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)
- [Roadmap](#roadmap)

## Features

- Fetch recent GitHub user activities.
- Filter activities by event type.
- Display activities in a tabular format.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/TheRealSaiTama/GithubUserActivity.git
   ```

2. Navigate to the project directory:
   ```bash
   cd GithubUserActivity
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To use the CLI tool, run the following command:

```bash
python main.py <username> [eventtype]
```

- `<username>`: The GitHub username to fetch activities for.
- `[eventtype]`: (Optional) Filter activities by event type (e.g., `PushEvent`, `IssuesEvent`).

## Example

Fetch and display all recent activities for a user:

```bash
python main.py octocat
```

Fetch and display only `PushEvent` activities for a user:

```bash
python main.py octocat PushEvent
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the [GPL-3.0 License](LICENSE).

## Roadmap

For more details, visit the [GitHub User Activity Roadmap](https://roadmap.sh/projects/github-user-activity).

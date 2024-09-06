# Github Organization Client

This project provides a client to interact with the GitHub API and fetch organization details, including public repositories.

## Files:
- **client.py**: Implements the `GithubOrgClient` class to retrieve and cache (memoize) data from GitHub, such as organization details and public repositories.
- **fixtures.py**: Contains test fixtures used for mocking during tests.
- **test_client.py**: Unit tests for `client.py` functions.
- **test_utils.py**: Unit tests for utility functions.
- **utils.py**: Includes utility functions like `get_json`, `access_nested_map`, and `memoize`.

## Usage:
- Import the `GithubOrgClient` class and call its methods to retrieve GitHub organization data.


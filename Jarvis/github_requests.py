from github import Github


# returns an array of all the names of the users repositories
def get_repositories(username: str):
    repositories = []
    try:
        print("Username: " + username)
        user = Github().get_user(username)
        for repo in user.get_repos():
            repositories.append(repo.name)

        return repositories
    except():
        print("An error occurred in get_repositories")

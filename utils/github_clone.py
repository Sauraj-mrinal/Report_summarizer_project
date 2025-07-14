import git
import os

def clone_repo(git_url, clone_dir="repo_clone"):
    if os.path.exists(clone_dir):
        print(f"Directory {clone_dir} already exists. Skipping clone.")
        return clone_dir
    git.Repo.clone_from(git_url, clone_dir)
    print(f"Repo cloned to {clone_dir}")
    return clone_dir
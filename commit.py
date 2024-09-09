import os
import subprocess

# Configuration
REPO_PATH = "/Users/paulodrefahl/Desktop/Projects/PAT"  # GitHub repository path
COMMIT_MESSAGE = "TrafficGuard 3.7v"  # Commit message
COMMIT_DATE = "2024-09-09T08:00:00"  # Commit date (YYYY-MM-DDTHH:MM:SS)
BRANCH_NAME = "main"  # Branch name

def run_command(command, cwd=None):
    """Run a shell command and capture the output."""
    result = subprocess.run(command, cwd=cwd, text=True, capture_output=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr.strip()}")
        exit(1)
    return result.stdout.strip()

def main():
    # Verify repository path
    if not os.path.exists(REPO_PATH):
        print(f"Error: Repository path '{REPO_PATH}' does not exist.")
        return
    os.chdir(REPO_PATH)
    
    # Check for changes
    print("Checking for changes...")
    status = run_command(["git", "status", "--porcelain"])
    if not status:
        print("No changes to commit. Exiting.")
        return
    
    # Add changes
    print("Adding changes...")
    run_command(["git", "add", "."])
    
    # Commit changes
    print("Committing changes...")
    run_command([
        "git", "-c", f"user.date={COMMIT_DATE}", "commit", "--date", COMMIT_DATE, "-m", COMMIT_MESSAGE
    ])
    
    # Push changes
    print("Pushing changes to GitHub...")
    run_command(["git", "push", "origin", BRANCH_NAME])
    
    print("Changes successfully committed and pushed to GitHub.")

if __name__ == "__main__":
    main()

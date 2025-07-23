import hashlib
import os
import time

def calculate_file_hash(file_path):
    """Calculate the SHA-256 hash of a file."""
    hash_sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        # Read the file in chunks to avoid memory issues with large files
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha256.update(chunk)
    return hash_sha256.hexdigest()

def monitor_file(file_path, interval=10):
    """Monitor a file for changes based on its hash value."""
    if not os.path.isfile(file_path):
        print(f"File {file_path} does not exist.")
        return

    # Calculate the initial hash
    previous_hash = calculate_file_hash(file_path)
    print(f"Monitoring {file_path} for changes...")
    print(f"Initial hash: {previous_hash}")

    while True:
        time.sleep(interval)  # Wait for the specified interval
        current_hash = calculate_file_hash(file_path)

        if current_hash != previous_hash:
            print(f"File {file_path} has changed!")
            print(f"New hash: {current_hash}")
            previous_hash = current_hash  # Update the previous hash

if __name__ == "__main__":
    # Specify the file to monitor and the interval in seconds
    file_to_monitor = "path/to/your/file.txt"  # Change this to your file path
    monitor_interval = 10  # Change this to your desired interval

    monitor_file(file_to_monitor, monitor_interval)

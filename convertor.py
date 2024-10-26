import re

def extract_file_id(url):
  """Extracts the file ID from a Google Drive URL.

  Args:
    url: The Google Drive URL.

  Returns:
    The extracted file ID, or None if not found.
  """

  pattern = r"d/([^/]+)"
  match = re.findall(pattern, url)
  return match[0] if match else None

if __name__ == "__main__":
  url = input("Enter the Google Drive URL: ")
  file_id = extract_file_id(url)

  if file_id:

    print(f'"FILE_ID={file_id}" >> $GITHUB_ENV')
    
  else:
    print("Invalid Google Drive URL")

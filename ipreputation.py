import requests
import html2text
import json
import argparse

def main():
  parser = argparse.ArgumentParser(description="Retrieve reputation data for an IP address")
  parser.add_argument("ip_address", help="The IP address for reputation lookup")

  args = parser.parse_args()
  ip_address = args.ip_address

  url = f"https://reputation.noc.org/?ip={ip_address}"

  # Make an HTTP GET request to the URL
  response = requests.get(url)
  html_content = response.text

  # Check if the request was successful (status code 200)
  if response.status_code == 200:
    # Convert the HTML to plain text
    text_content = html2text.html2text(html_content)

    # Find and extract the JSON content
    json_start = text_content.find('{')
    json_end = text_content.rfind('}') + 1
    json_str = text_content[json_start:json_end]

    # Parse the JSON string into a JSON object
    data = json.loads(json_str)

    # Print the JSON object
    print(json.dumps(data, indent=2))
  else:
    print("Failed to fetch content from the URL.")

if __name__ == "__main__":
  main()

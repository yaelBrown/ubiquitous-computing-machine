import json

if __name__ == "__main__":
  # Read secrets file
  with open('secrets.json') as secrets:
    data = json.load(secrets)

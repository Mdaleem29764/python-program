import requests
import json

def fetch_data(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        return data
    except requests.RequestException as e:
        print(f"Failed to fetch data from the API: {e}")
        return None
    except ValueError as e:
        print(f"Failed to parse JSON response: {e}")
        return None

def identify_citations(data):
    citations = []
    for item in data:
        response = item.get("Response", "")
        sources = item.get("Source", [])
        for source in sources:
            if source["context"] in response:
                citations.append({"id": source["id"], "link": source.get("link", "")})
    return citations

def main():
    api_url = "https://devapi.beyondchats.com/api/get_message_with_sources"
    data = fetch_data(api_url)
    if data:
        citations = identify_citations(data)
        print("Citations:")
        print(json.dumps(citations, indent=2))

if __name__ == "__main__":
    main()


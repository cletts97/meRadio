import urllib3, facebook, requests

import json

def main():
    token = 'EAAF8K7TUhd4BABtyeKhxDAnmWAGVhSwWViBFtTDcpznVkf5PylKgTt06esSqdUUGVPZBNVC8pkoxOZAaMLZAwZAPoDofGGfktUeat3ZAgG7iWYKOC03oKGPaY4Qc4l2FiqVIWxon5xms0ONgU1ef5mZBaLtPRvzGCUu9ptLpLriAAdZACWwqJhecBEVtlpnh0sorPMVeZBMWDDgbiZBjwQdXtE9ZBCP0ZA9UUofvj44F9UqcgZDZD'
    graph = facebook.GraphAPI(token)
    profile = graph.get_object(id='me', fields='first_name, last_name')
    print(json.dumps(profile, indent=4))

if __name__ == '__main__':
    main()

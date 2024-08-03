import requests
from tabulate import tabulate
from time import sleep

# List of subdomains to check
subdomains = [
    'www.osboxes.org/ubuntu/'
]

def status_dm(subdomain):
    try:
        response = requests.get(f'http://{subdomain}', timeout=5)
        return 'Up' if response.status_code == 200 else 'Down'
    except requests.RequestException:
        return 'Down'

def statusdisplay():
    headers = ['Subdomain', 'Status']
    table = [[subdomain, status_dm(subdomain)] for subdomain in subdomains]
    print(tabulate(table, headers=headers, tablefmt='pretty'))

def main():
    while True:
        statusdisplay()
        sleep(60)  # Wait for 1 minute

if __name__ == '__main__':
    main()

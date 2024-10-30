import requests
import csv

def get_mac_vendor(mac_address):
    url = f"https://www.macvendorlookup.com/api/v2/{mac_address}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def process_mac_addresses(input_file, output_file):
    with open(input_file, 'r') as file:
        mac_addresses = file.readlines()

    results = []
    for mac in mac_addresses:
        mac = mac.strip()
        vendor_info = get_mac_vendor(mac)
        if vendor_info:
            for info in vendor_info:
                results.append({
                    'MAC Address': mac,
                    'Company': info.get('company', 'N/A'),
                    'Address': info.get('address', 'N/A'),
                    'Country': info.get('country', 'N/A'),
                    'Type': info.get('type', 'N/A')
                })
        else:
            results.append({
                'MAC Address': mac,
                'Company': 'N/A',
                'Address': 'N/A',
                'Country': 'N/A',
                'Type': 'N/A'
            })

    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['MAC Address', 'Company', 'Address', 'Country', 'Type']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for result in results:
            writer.writerow(result)

    print(f"Results saved to {output_file}")

# Uso del script
input_file = 'C:/RootScripts/mac_addresses.txt' 
output_file = 'C:/RootScripts/mac_vendors.csv'
process_mac_addresses(input_file, output_file)
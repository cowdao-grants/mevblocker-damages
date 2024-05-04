"""
todos:

1. Rename this file configurations.py
2. Get your infura key (https://docs.infura.io/dashboard/create-api) and copy paste it bellow. Make sure you have activated the Ethereum Mainnet endpoint
3. Get your etherscan api key (https://docs.etherscan.io/getting-started/viewing-api-usage-statistics) and copy paste it bellow
4. Get your tenderly access token (https://docs.tenderly.co/account/projects/how-to-generate-api-access-token) and copy paste it bellow
5. Get your tenderly api url (Example: 'https://api.tenderly.co/api/v1/account/aurelie2/project/cowswap/')
6. Insert your incident name and relative csv path

"""

infura_api_key = 'INSERT-YOUR-INFURA-API-KEY' 
eth_scan_api_key = 'INSERT-YOUR-ETHERSCAN-API-KEY'
tenderly_access_token = 'INSERT-YOUR-TENDERLY-ACCESS-TOKEN'
tenderly_api_url = 'INSERT-YOUR-TENDERLY-API-URL'
name_of_incident = 'INSERT INCIDENT NAME'
csv_file_path = 'INSERT YOUR CSV PATH' #example: f'data/input/{name_of_incident}.csv'
infura_url = f"https://mainnet.infura.io/v3/{infura_api_key}"

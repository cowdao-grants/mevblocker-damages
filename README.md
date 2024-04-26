# Calculating potential loss of transaction intent leakage

- Input: a list of transaction hashes that we think have been leaked 
- Output: a file with the potential loss in dollars for each transaction as well as the total potential loss in dollar, ethereum, and original coin used in the transaction.

## The methodology: 
1. We have a list of transaction hashes that we think have been leaked 
2. We get the details of this transaction using the Infuria and Etherscan APIs
3. We simulate the result of each transaction if it would have been top of the block using the Tenderly API
4. We calculate the difference in dollars for each transaction
5. We sum the potential loss of each transaction to get the total potential loss in dollars. 

## Usage
1. Have a csv file with one column called ' user_tx' (space is important) having all the transactions hashes that you think were leeked inside the folder data/input
2. open the config_example.py file and follow the instructions for the configuration
3. Intall the requirements in your environment ``` pip install -r requirements.txt ``` 
4. run the Jupyter Notebook. The output file is called data/results/<INCIDENT_NAME>_final_results.csv - but the Jupyter Notebook is full of interesting information being printed out.

## Final results data catalog

The final result file has the following columns
| Column | Meaning |
| :--- | :--- |
| ```tx_hash``` | the transaction hash of the potentially leaked transaction |
| ```sender``` | address which initiated the transaction |
| ```delta_eth``` | this is the potential loss for that transaction, it is the difference in ethereum between the value of the transaction at top of block vs. at the actual position in the block. A value of -1 means that the leaked transaction cost the sender 1 ethereum |
| ```delta_dollar``` | difference in dollars between the value of the transaction at top of block vs. at the actual position in the block |
| ```token_name_A``` | name of one of the two tokens exchanged by the sender |
| ```token_contract_address_A``` |  token contract address of one of the two tokens exchanged by the sender |
| ```delta_token_A``` | difference in token A between if the transaction was at top of block vs. at the actual position in the block.  A value of -1 means that the leaked transaction cost the sender 1 token A  |
| ```token_name_B``` |  name of one of the two tokens exchanged by the sender |
| ```token_contract_address_B``` | token contract address of one of the two tokens exchanged by the sender |
| ```delta_token_B``` | difference in token B between if the transaction was at top of block vs. at the actual position in the block.  A value of -1 means that the leaked transaction cost the sender 1 token B

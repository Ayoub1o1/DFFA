import requests
import json

class DFFA:
    
    def __init__(self , baseurl , endpoint):
        self.baseurl = baseurl
        self.endpoint = endpoint


    def get_request(self, baseurl, endpoint):
        try:
            response = requests.get(baseurl + endpoint)

            if response.status_code != 200 :
                raise requests.ConnectionError("can't reach the API url.")
            else :
                return response.json()
        except requests.ConnectionError as e :
            print(f'Error {e}')
        except requests.JSONDecodeError as e:
            print(f'Error {e}')

    def parse_json(self , response , path = 'root'):
        # check if the item had content 

        if response is None or response == [] or response == {}:
            print(f"\n{path} has no content")
            return 

        # dic case
        if isinstance(response , dict):
            keys = list(response.keys())
            print("\nAvailable items:")

            for index, key in enumerate(keys):
                print(f'{index} : {key}')

            choice =  input('\nchoose the item (or quit):')

            if choice.lower() == 'quit':
                print('bye')
                return
            
            try :
                choice = int(choice)
                selected_key = keys[choice]

                self.parse_json(
                    response[selected_key],
                    path + '.' + selected_key
                )
            except (ValueError , IndexError):
                print('Invalid choice!')
        
        # list case

        elif isinstance(response , list):

            print('\nAvailiable items:')

            for index, key in enumerate(response):
                print(f'{index} : {type(key).__name__}')

            choice = input('\nChoose item (or quit):')

            if choice.lower() == 'quit':
                print('Bye!')
                return
            
            try : 
                choice = int(choice)

                self.parse_json(
                    response[choice],
                    path + f'[{choice}]'
                )
            except (ValueError , IndexError):
                print('Invalid choice')

        else:
            print('\nFinal Value:')
            print(response)



baseurl = "https://dragonball-api.com/api/"
endpoint = "characters"

baseurl2 = "https://rickandmortyapi.com/api/"
endpoint2 = "character"

data = DFFA(baseurl  , endpoint)

response = data.get_request(baseurl2 , endpoint2)
data.parse_json(response)
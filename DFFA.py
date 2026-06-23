import requests
from typing import Any, Optional

class RestartNavigation(Exception):
    pass

class QuitNavigation(Exception):
    pass

class DFFA:
    
    def get_request(self):

        url = input("Enter the API URL: ").strip()
        if not url:
            return None
            
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status() 
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Network/HTTP Error: {e}")
        except ValueError:
            print("Error: Response is not valid JSON.")
        return None

    def parse_content(self, data: Any, path: str = 'root'):
        while True:
            # 1. Check if item has content
            if data is None or data == [] or data == {}:
                print(f"\n{path} has no content.")
                if input('Press "back"/Enter to return, "quit" to exit: ').strip().lower() == 'quit':
                    raise QuitNavigation
                break

            # 2. Dictionary Case
            if isinstance(data, dict):
                keys = list(data.keys())
                print("\nAvailable items:")
                for i, k in enumerate(keys):
                    print(f"{i} : {k}")
                
                choice = input('\nChoose item (or "back"/"quit"): ').strip().lower()
                if choice == 'quit': raise QuitNavigation
                if choice == 'back': break
                
                try:
                    key = keys[int(choice)]
                    self.parse_content(data[key], f"{path}.{key}")
                except (ValueError, IndexError):
                    print("Invalid choice!")

            # 3. List Case
            elif isinstance(data, list):
                print("\nAvailable items:")
                for i, v in enumerate(data):
                    print(f"{i} : {type(v).__name__}")
                
                choice = input('\nChoose item (or "back"/"quit"): ').strip().lower()
                if choice == 'quit': raise QuitNavigation
                if choice == 'back': break
                
                try:
                    idx = int(choice)
                    self.parse_content(data[idx], f"{path}[{idx}]")
                except (ValueError, IndexError):
                    print("Invalid choice!")

            # 4. Final Value Case
            else:
                print(f"\nFinal Value at {path}:\n{data}")
                action = input('\nPress Enter to restart from zero, "back" to return, "quit" to exit: ').strip().lower()
                
                if action == 'quit':
                    raise QuitNavigation
                elif action == 'back':
                    break
                elif action == '':
                    raise RestartNavigation



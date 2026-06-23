from DFFA import DFFA , RestartNavigation , QuitNavigation

if __name__ == "__main__":
    dffa = DFFA()
    
    while True:
        try:
            # Fetch data
            data = dffa.get_request()
            if data is None:
                continue
                
            # Navigate data
            while True:
                try:
                    dffa.parse_content(data)
                    break 
                except RestartNavigation:
                    
                    print("\n--- Restarting from Root ---")
                    continue
                    
            # Ask if the user wants to query a new API
            if input("\nQuery another API? (y/n): ").strip().lower() != 'y':
                break
                
        except QuitNavigation:
            print("\nGoodbye!")
            break
        except KeyboardInterrupt:
            print("\nProgram forcibly interrupted. Goodbye!")
            break
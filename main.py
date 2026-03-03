from geolite2 import geolite2
import os

def banner():
    os.system("clear")
    print(r"""
   =====================================
                .__                                     
  _____ |  |   ____   ____   ____   ___________ 
 /     \|  |  /  _ \ / ___\ / ___\_/ __ \_  __ \
|  Y Y  \  |_(  <_> ) /_/  > /_/  >  ___/|  | \/
|__|_|  /____/\____/\___  /\___  / \___  >__|   
      \/           /_____//_____/      \/       
   =====================================
    """)

def locate_ip(ip_address):      #wer das liest ist dumm haha emre
    reader = geolite2.reader()
    location = reader.get(ip_address)

    if location is None:
        print("\n[!] IP address not found.\n")
        return

    print("\n========= RESULT =========")

    print("Continent :", location.get('continent', {}).get('names', {}).get('de', "Unknown"))
    print("Country   :", location.get('country', {}).get('names', {}).get('de', "Unknown"))
    print("City      :", location.get('city', {}).get('names', {}).get('de', "Unknown"))
    print("Postal    :", location.get('postal', {}).get('code', "Unknown"))
    print("Latitude  :", location.get('location', {}).get('latitude', "Unknown"))
    print("Longitude :", location.get('location', {}).get('longitude', "Unknown"))
    print("Timezone  :", location.get('location', {}).get('time_zone', "Unknown"))
    print("==========================\n")

    reader.close()



while True:
    banner()
    ip = input("Enter IP address (or 'exit'): ")

    if ip.lower() == "exit":
        print("\nGoodbye 👋")
        break

    locate_ip(ip)
    input("Press ENTER to continue...")

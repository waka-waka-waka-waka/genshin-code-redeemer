import requests
import re

def extract_unique_codes(url):
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
        pattern = r'\b[A-Z0-9]{12}\b'
        codes = re.findall(pattern, html_content)
        return list(set(codes))
    else:
        print("Failed to fetch webpage, might be down?")
        return []

def redeem_codes(codes, uid):
    redeemed_codes = set()
    for code in codes:
        if code not in redeemed_codes:
            redeem_url = f"https://sg-hk4e-api.hoyoverse.com/common/apicdkey/api/webExchangeCdkey?region=os_usa&game_biz=hk4e_global&lang=en&cdkey={code}&uid={uid}"
            response = requests.get(redeem_url)
            if response.status_code == 200:
                print(f"Code {code} redeemed successfully!")
                redeemed_codes.add(code)
            else:
                print(f"Failed to redeem code {code}.")
    return len(redeemed_codes)

def main():
    while True:
        print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡴⠞⢋⠉⠡⡀⠌⠹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡄⠌⢤⣮⣷⡄⠊⠄⣻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⢿⠶⢟⣡⣼⠿⣠⣵⡿⠷⠶⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡤⠶⠚⠹⣿⠀⢂⣿⣁⡄⢂⠔⠠⢉⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⠾⢋⠡⣐⣤⡷⠷⠻⢗⣾⢯⡉⠉⠋⢳⠎⣰⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣤⠟⡁⢂⣦⠾⠋⠁⠀⠀⠸⣧⣤⡴⡏⢠⣼⡿⠞⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⡾⢃⢐⡼⠋⠁⠀⢀⣠⡴⠶⠶⠛⠛⠓⠛⠲⠧⢤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⡇⠠⢾⣅⣠⡴⠞⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢙⡳⢦⣀⢀⣀⣠⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠉⠉⣩⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣦⡈⠉⠉⢁⡏⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡼⠁⠀⠀⠀⠀⠀⠀⢠⠀⠀⠀⠀⠀⠀⠀⠀⣄⠀⠀⠀⣿⡿⣷⣦⡉⠒⠶⠤⠦⢴⠀⠀
⠀⠀⠀⠀⠀⣀⡞⠁⠀⠀⠀⠀⠀⠀⣀⢸⣆⠀⠀⠀⠀⠀⠀⠀⢹⠱⣄⠠⢿⡿⣽⣻⠀⠀⠀⠀⢀⡞⠀⠀
⠀⣀⣤⡴⠞⠉⠀⠀⠀⠀⠀⠀⠀⠀⡇⡎⠘⢦⣀⡄⠀⠀⠀⠀⠠⡇⠘⠳⢆⡈⠛⢿⡇⠀⢰⠞⠋⠀⠀⠀
⠈⠳⣄⠀⠀⠀⠀⠀⢠⠂⠀⠀⠀⠀⣷⠃⠠⠚⠹⢦⡀⠀⠀⢤⣀⢻⠀⠀⠈⠱⣆⠀⠹⠀⠀⢳⡀⠀⠀⠀
⠀⠀⠈⠙⠲⡶⠂⠀⡎⠀⠀⠀⠀⢈⡟⠀⠀⢀⡀⠀⠙⠳⣤⣌⣫⡙⠃⠀⣴⣦⡜⣧⠀⠀⠀⠀⢧⠀⠀⠀
⠀⠀⠀⠀⣼⠁⠀⢸⠀⠀⠀⠀⠀⠾⡅⠀⢰⣿⣻⣷⠀⠀⠀⠀⠀⠀⠀⠘⣿⣽⠷⠘⣆⠀⠀⠀⠸⡆⠀⠀
⠀⠀⠀⣼⠃⠀⠀⡏⠀⠀⠀⠀⠀⢈⡇⠀⠘⠻⡽⠛⠀⢀⠀⠀⠀⠀⠀⡄⠀⠀⠠⠀⢹⣆⠀⠀⠀⢷⠀⠀
⠀⠀⠀⣿⠀⠀⢠⡇⠀⠀⠀⠀⠀⠀⣇⠀⠂⢀⠀⠄⠀⠈⠒⠒⠉⠉⠉⠀⠀⠀⠁⠀⢀⡿⠀⠀⠀⢸⡄⠀
⠀⠀⠰⣟⠀⠀⢰⡃⠀⠀⠀⠀⠀⠀⢿⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⢾⡁⠀⠀⠀⠘⡆⠀
⠀⠀⠐⣿⠀⠀⠸⡅⠀⠀⠀⠀⠀⠀⠸⣆⡀⠀⣀⣀⣀⣤⣤⣤⣶⣶⣶⣶⣶⣾⡿⣵⣼⠀⠀⠀⠀⠰⣇⠀
⠀⠀⠀⢹⡄⠀⠠⣧⠀⠀⠀⠀⠀⠀⠀⢻⣿⢿⣟⣿⢻⣯⣟⣿⣳⢿⣞⣷⣻⣾⣽⡿⠏⢀⣤⠃⠀⢸⡇⠀
        """)
        print("Welcome to waka's Genshin code redeemer!")
        uid = input("Enter your UID: ")
        if uid.isdigit() and len(uid) == 9:
            custom_url = input("Enter the URL you want to scrape for Genshin Codes. Leave empty to use default (/gig/): ")
            if custom_url.strip() == "":
                custom_url = "https://arch.b4k.co/vg/search/subject/%2Fgig%2F/type/op/"
            webpage_url = custom_url
            codes = extract_unique_codes(webpage_url)
            if codes:
                num_redeemed = redeem_codes(codes, uid)
                print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⡒⠢⡀⡔⠤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢇⠅⢇⠪⢐⠅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠠⢤⢚⢘⢪⡨⠘⢤⢄⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⢒⢉⢂⣂⠅⢏⠌⡒⠪⡢⢁⢂⢇⢢⡈⡉⡒⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⠔⡘⡐⠌⠒⠈⠁⠀⠀⠀⠉⠒⠱⠌⠒⠁⠀⠀⡠⡑⢔⠕⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡐⠅⡪⠪⡠⠤⣄⠤⠒⠒⠉⠉⠉⠉⠉⠉⠁⠐⠒⠓⠲⣉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⠨⠬⢢⠜⠊⠀⠀⠀⠠⠀⢂⠈⠀⡔⠀⠈⢀⠠⠀⠂⡀⠁⠢⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⠰⠁⠀⡀⠀⠠⠐⠀⠠⠂⠀⢰⠁⠀⠁⠀⠀⢀⠀⠀⢂⠀⢀⠱⡀⠀⠀⠀⠀⠀⠀⠀
⠀⡀⠀⠀⢀⣀⠔⠊⠀⠠⠀⢀⠐⠀⠠⢀⠃⠀⢂⡎⠀⠐⠈⠀⠈⠀⢤⠈⠀⡸⡦⡀⠐⡀⠀⠀⠀⠀⠀⠀
⠀⢃⠉⠉⠀⡀⠀⠄⠂⠄⠂⠀⡀⠐⠀⡆⠀⢄⠂⢣⠀⠂⠐⠈⠀⡀⡇⠑⡴⣫⡯⡯⡦⠐⡀⠀⠀⠀⠀⠀
⠀⠈⠢⣂⠁⠀⡀⠄⠊⠀⠠⠀⠀⠄⢰⠀⡰⠁⠀⠚⢍⠁⡀⠐⠀⠐⡕  ⠈⢌⠺⡯⠃⠀⠑⢄⠀⠀⠀⠀
⠀⠀⠀⠀⢑⠆⠀⠌⠀⠀⠂⠀⠂⠀⡜⠈⠀⠀⠀  ⣈⠱⢸⠐⠤⠄⠧⠀⠀   ⡙⠀⠐⠈⠄⠁⡒⠀⠀
⠀⠀⠀⠀⡌⠀⢐⠁⠀⠁⠀⠂⠐⠀⡇  ⠛⠳⢶⠞⠋⠀⠀⠀⠀ ⠀⠺⢦⣤⠶⢸⠀⢀⠁⠀⢑⠪⠄⠀⠀
⠀⠀⠀⡘⠀⠀⡂⠀⠈⢀⠈⠀⠠⠀⡃     ⠀⠀⠀⠐⢄⡠⢐⡠⠀⠀    ⠱⡀⠀⠈⠈⡎⠀⠀⠀
⠀⠀⢀⠃⠀⠁⡅⠀⠁⠀⡀⠈⢀⠀⡇⠀⠀                 ⠀⡇⠀⠁⠀⡃⠀⠀⠀
⠀⠀⠨⡀⠐⠀⢁⠀⠈⠀⢀⠠⠀⠀⣇⠀⠀               ⢀⡴⢳⠀⠈⠀⠄⠀⠀⠀
⠀⠀⠀⠱⡀⠠⠘⡄⠈⠀⡀⠀⠠⠀⠘⡯⣗⡶⣳⡽⡽⡽⣽⣺⢮⢶⣲⣢⣔⡖⢉⢐⢸⠀⠐⠀⡂⠀⠀⠀
⠀⠀⠀⠀⠑⢄⠠⠋⢆⢀⠀⠐⠀⠠⠀⠈⠓⠟⠗⣯⢟⣽⣳⢽⢽⢽⣺⡵⣗⣅⣒⠥⠂⠀⠄⡠⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢉⠲⠁⠑⠢⣀⠈⠀⠀⢂⣀⢴⣺⢽⢽⣺⣞⣽⠉⠁⢀⠀⠹⡺⡶⡦⣤⠴⠊⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠆⠀⡀⠄⠀⢠⣽⢽⢽⣳⢯⣻⣺⢽⣻⣺⣺⡺⠀⠠⠀⢀⠀⢱⠹⣽⣺⢽⡫⡯⣯⡻⡆⠀
⠀⠀⠀⠀⠀⠀⠈⡺⣍⢍⠲⠍⡚⠝⢯⠞⠝⡮⣗⠟⢀⢑⠃⠁⡀⠄⠠⢀⠀⡀⢟⡵⠫⣫⣻⡺⠵⠋⠀⠀
⠀⠀⠀⠀⠰⡩⢉⢊⠍⡓⡎⡐⠌⠌⡮⡹⠀⠈⠀⠀⠐⡀⠈⠐⢀⠂⠁⠠⠁⠀⢸⢆⢙⢘⠒⢦⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠑⠦⠥⣂⡍⡣⠡⢱⠝⠈⠀⠐⠈⠀⡀⠈⠂⢄⠡⠨⢀⠊⠀⠈⠀⣇⡆⠦⠓⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⠉⠈⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀
        """)
                print(f"{num_redeemed} codes redeemed successfully! Enjoy the Primos!")
            else:
                print("No codes found using that URL :(")
        else:
            print("Invalid UID. Your UID is a 9 digit number.")

        choice = input("Do you want to check other URLs? (yes/no): ")
        if choice.lower() != "yes":
            break

if __name__ == "__main__":
    main()

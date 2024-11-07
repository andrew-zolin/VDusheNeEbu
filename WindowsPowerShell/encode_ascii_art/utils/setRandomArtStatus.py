import sys, json
from pprint import pprint
sys.path.append("C:\\Users\\Andrery\\Documents\\WindowsPowerShell\\encode_ascii_art")

from utils.getArt import getArt, getRandomStatus, getActivityStatus, clear_file_from_line, CONFIG_PATH, PROFILE_PATH

def main():
      
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        config_text = f.read()
        new_config_json = json.loads(config_text)
        random_status = new_config_json["isRandom"]
        new_random_status = not random_status
            
        new_config_json["isRandom"] = new_random_status
        new_random_status_text = "Random Art" if new_random_status else "Permanent Art"
        print(f"Art rundom status was chengegd on {new_random_status_text}")

    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
            json.dump(new_config_json, f, ensure_ascii=False, indent=4)

    # getArt(getRandomStatus(CONFIG_PATH), getActivityStatus(CONFIG_PATH), CONFIG_PATH, PROFILE_PATH, 11)

if __name__ == "__main__":
    main()
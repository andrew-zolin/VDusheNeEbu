import sys, json
sys.path.append("C:\\Users\\Andrery\\Documents\\WindowsPowerShell\\encode_ascii_art")

from utils.getArt import getArt, getRandomStatus, clear_file_from_line, CONFIG_PATH, PROFILE_PATH

def main():
      
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        config_text = f.read()
        new_config_json = json.loads(config_text)
        activeity_status = new_config_json["isActive"]
        new_activeity_status = not activeity_status
        if not new_activeity_status:
            clear_file_from_line(PROFILE_PATH, 11)


        new_config_json["isActive"] = new_activeity_status 
        new_activeity_status_text = "Active Art" if new_activeity_status else "Inactive Art"
        print(f"Art activity status was chengegd on {new_activeity_status_text}")

    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
            json.dump(new_config_json, f, ensure_ascii=False, indent=4)
    
    # getArt(getRandomStatus(CONFIG_PATH), new_activeity_status, CONFIG_PATH, PROFILE_PATH, 11)

if __name__ == "__main__":
    main()
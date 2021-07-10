def init(device_name: str = "CABLE Input (VB-Audio Virtual Cable)"):
    try:
        mixer.init(devicename = device_name) 
        return True
    except:
        print("[ERROR] VB-Audio Virtual Cable is not installed. Install it from https://vb-audio.com/Cable/index.htm and try again.")
        return False

def play_sound(file_name: str, delay: int = 0):
    try:
        mixer.music.load(file_name)
        for i in range(delay, 0, -1):
            time.sleep(1)
            print(f"Playing sound in {i}")
        mixer.music.play()
        return True
    except:
        print("[ERROR] Audio Files are missing. Please re-download them from the Github repository.")
        return False

def print_logo():
    print("██████╗ ██╗  ██╗ █████╗ ███████╗███╗   ███╗ ██████╗ ██████╗  ██████╗  █████╗ ██████╗ ██████╗\n██╔══██╗██║  ██║██╔══██╗██╔════╝████╗ ████║██╔═══██╗██╔══██╗██╔═══██╗██╔══██╗██╔══██╗██╔══██╗\n██████╔╝███████║███████║███████╗██╔████╔██║██║   ██║██████╔╝██║   ██║███████║██████╔╝██║  ██║\n██╔═══╝ ██╔══██║██╔══██║╚════██║██║╚██╔╝██║██║   ██║██╔══██╗██║   ██║██╔══██║██╔══██╗██║  ██║\n██║     ██║  ██║██║  ██║███████║██║ ╚═╝ ██║╚██████╔╝██████╔╝╚██████╔╝██║  ██║██║  ██║██████╔╝\n╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝\n\nBuild: 1.0.0 | GitHub Repository: https://github.com/NuKeFluffy/Phasmoboard | Developer: NuKe Fluffy")

def translate():
    translator = {
        1: "Spirit Box",
        2: "Doors",
        3: "Foosteps",
        4: "Throwing",
        5: "Map Interactions",
        6: "Breathing & Heartbeats",
        7: "Custom",
        8: "Other"
    }
    return translator

def main():
    print_logo()
    print("Once in Phasmophobia, set your default microphone to 'CABLE Input (VB-Audio Virtual Cable)' in Audio Settings. This must also be done in Windows Settings to ensure all sounds go through.")

    if init():
        while True:
            while True:
                try:
                    section = int(input("\n[INPUT] Choose a Section:\n[1] Spirit Box\n[2] Doors\n[3] Footsteps\n[4] Throwing\n[5] Map Interactions\n[6] Breathing & Heartbeats\n[7] Custom\n[8] Other\n\n> "))
                except ValueError:
                    print("\n[ERROR] Provided value must be an integer.")
                
                if section <= 8 and section >= 1:
                    break
                else:
                    print(f"\n[ERROR] {section} not found.")

            while True:
                try:
                    if section >= 1 and section <= 8:
                        section_name = translate()[section]
                        file_names = next(walk(f"Sounds\\{section_name}"), (None, None, []))[2]
                        audio_files = ""
                        translator = {}

                        for i, file_name in enumerate(file_names):
                            audio_files += f"[{i + 1}] {file_name}\n"
                            translator[i + 1] = file_name 

                        audio_file = int(input(f"\n[INPUT] Choose an Audio File:\n{audio_files}\n[0] Go Back\n\n> "))
                    else:
                        print(f"\n[ERROR] {section} not found.")

                except ValueError:
                    print("\n[ERROR] Provided value must be an integer.")
            
                if audio_file <= len(file_names) and audio_file >= 0:
                    break
                else:
                    print(f"\n[ERROR] {audio_file} not found.")
            
            if audio_file == 0:
                continue

            file_name = f"Sounds\\{section_name}\\" + translator[audio_file]

            if not play_sound(file_name):
                return

            print(f"\n[INFO] Attempted to play the {translator[audio_file]} audio file.")

try:
    from pygame import mixer
    from os import walk
    import time

    if __name__ == '__main__':
        main()

except ModuleNotFoundError:
    print("[ERROR] Module Missing. Run setup.bat and try again.")
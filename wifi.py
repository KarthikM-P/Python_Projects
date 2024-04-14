import subprocess

# Get the Wi-Fi profiles
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
profiles = [line.split(":")[1][1:-1] for line in data if "All User Profile" in line]

# Iterate through profiles and fetch passwords
for profile in profiles:
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8', errors="backslashreplace").split("\n")
        password = [line.split(":")[1][1:-1] for line in results if "Key Content" in line][0]
        print("{:<30} | {:<}".format(profile, password))
    except IndexError:
        print("{:<30} | {:<}".format(profile, ""))
    except subprocess.CalledProcessError:
        print("{:<30} | {:<}".format(profile, "ERROR"))


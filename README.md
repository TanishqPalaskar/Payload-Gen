## Payload Generator for Havoc Framework and msfvenom

This tool generates payloads for the Havoc Framework and msfvenom based on user inputs. It asks for critical information such as LHOST, LPORT, architecture, OS, and payload type (e.g., `.php`, `.exe`, `.elf`).

### Features:
- **Havoc Framework**:
  - Generates payloads for Windows and Linux with support for x64 and x86 architectures.
- **msfvenom**:
  - Supports multiple payload formats including `.exe`, `.php`, and `.elf`.
  - Generates payloads for both Windows and Linux platforms.
  - Provides customization options like LHOST, LPORT, and architecture.

### Usage:
1. Run the script.
2. Choose whether to generate a Havoc or msfvenom payload.
3. Input the necessary details such as LHOST, LPORT, OS, architecture, and output file name.
4. The tool will generate the payload command and optionally run it if desired.

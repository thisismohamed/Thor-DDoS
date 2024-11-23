# DDoS Test Tool

This is a Python-based tool designed to test server load and evaluate network performance under heavy traffic conditions. It simulates a distributed denial-of-service (DDoS) attack to see how well a server can handle large amounts of requests. This tool is intended **only for ethical testing** purposes on servers that you own or have explicit permission to test.

## **Important Notice**
**DO NOT** use this tool to attack others or disrupt services. Unauthorized use of DDoS attacks is illegal and can result in criminal charges. Always ensure that you have explicit permission from the server owner before conducting any testing.

## Features
- **Customizable Host & Port**: You can specify the target server and port to test.
- **Threaded Requests**: Supports multi-threaded attacks for testing the server's ability to handle concurrent requests.
- **Random User-Agents**: Simulates real user requests with random user-agents.
- **Proxy Support**: Allows the simulation of requests with a specified proxy IP.
- **Bot Requests**: Simulates requests from various known bot URLs to test server response.
- **Ethical Testing Tool**: This tool should only be used for ethical testing and improving security.

## Requirements

- Python 3.x
- Install required libraries:
    ```bash
    pip install fake_useragent pyfiglet
    ```

## Usage

```bash
python main.py <hostname> <port> <threads>

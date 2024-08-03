# Project Title

Deploy a Website on Localhost Using VirtualBox, Ubuntu 22.04, and Nginx

## Introduction

This guide provides step-by-step instructions to install Oracle VirtualBox, run an Ubuntu 22.04 virtual machine, install Nginx inside the virtual machine, host a website, and scan the virtual machine from the host machine using Nmap.

## Features

- Install Oracle VirtualBox on various operating systems.
- Run an Ubuntu 22.04 virtual machine.
- Install and configure Nginx inside the Ubuntu virtual machine.
- Host a website on the virtual machine.
- Scan the virtual machine from the host machine using Nmap to observe open ports.

## Prerequisites

- A working installation of Windows,Linux distribution.
- Internet access to download required software.

## Installation

### Step 1: Download VirtualBox

1. Went to the official VirtualBox website: https://www.virtualbox.org/
2. Clicked on the "Downloads" link in the top navigation menu.

### Step 2: Choosen the Correct Package

1. On the Downloads page, selected the appropriate package for OS (e.g., Windows, macOS, or Linux).

### Step 3: Install VirtualBox

- **For Windows:**
  1. Downloaded the installer for Windows.
  2. Double-clicked on the downloaded file to start the installation.
  3. Followed the on-screen instructions and accepted the license agreement.
  4. Choosen the components required to install and the installation path.
  5. Completed the installation process.

### Step 4: Launched VirtualBox

1. Once the installation was completed,launched VirtualBox from application menu.

## Configuration

1. **Download and Started the Ubuntu 22.04 Image:**
   - Visited to this link- https://www.osboxes.org/ and downloaded an Ubuntu 22.04 image(Ubuntu 22.04 Jammy Jellyfish).
   - Started the Ubuntu 22.04 virtual machine through VirtualBox.

2. **Installed Nginx Inside the Ubuntu VM:**
   - Open a terminal in your Ubuntu VM and run:
     ```sh
     sudo apt update
     sudo apt-get install nginx
     ```
   - Start the Nginx service:
     ```sh
     sudo systemctl start nginx
     ```
  
## Usage

1. **For Hosting Website:**
   - Navigated to `/var/www/html` and edit the `index.html` file with HTML code.
     ```sh
     cd /var/www/html
     sudo nano index.html
     ```
   - Accessed the website by navigating to the IP address of Ubuntu VM in a web browser(Mozilaa Firefox).

## Testing

checked by running the IP address in webbrowser.

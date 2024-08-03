## Introduction

This guide details the steps to deploy a website on localhost using Apache2. Additionally. Free to use any web template or create your own simple HTML code.

## Features

- Localhost website deployment using Apache2.
- Flexible web template options: use a pre-existing template or design any of own HTML page.

## Prerequisites

- A working installation of any Linux Server such as Ubuntu.
- Sample frontend website for testing purpose.
- Apache2 installed on machine.

## Installation

**Install Apache2:**
   ```sh
   sudo apt-get install apache2
   sudo service apache2 start- to start the apache2 service
   sudo service apache2 status- for checking the apache2 service working or not.
   ```
## Configuration

Located the Apache2 Configuration File:
Opened default configuration file to find the location of the index.html file.
```sh

  sudo nano /etc/apache2/sites-available/000-default.conf
```

Edited the index.html File:

Navigated to the HTML directory.
```sh
  cd /var/www/html
```
Edited the index.html file with a sample HTML code.
```sh
sudo nano index.html
```

## Usage

Checked the ip using ifconfig & Once the Apache2 service is running and the index.html file was updated, accessed the website by navigating to your local ip in web browser.

## Testing
After completing the setup, tested the website by accessing the local ip in your web browser.
Ensured that custom HTML code is displayed correctly.


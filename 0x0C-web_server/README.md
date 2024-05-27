# Web Server

## General

- What is the main role of a web Server
- What is a child process
- Why web servers usually have a parent process and a child process
- What are the main HTTP requests

### Tasks

0. Tranfer a file to your server
    Write a Bash script that transfers a file from our client to a server:

    **Requirements:**

    - Accepts 4 parameters
        1. The path to the file to be transferred
        2. The IP of the server we want to transfer the file to
        3. The username scp connects with
        4. The path to the SSH private key that scp uses
    - Display Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY if less than 3 parameters passed
    - scp must transfer the file to the user home directory ~/
    - Strict host key checking must be disabled when using scp

    `Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY`

1. Install nginx web server
    Web servers are the piece of software generating and serving HTML pages, let’s install one!

    **Requirements:**

    - Install nginx on your web-01 server
    - Nginx should be listening on port 80
    - When querying Nginx at its root / with a GET request (requesting a page) using curl, it must return a page that contains the string Hello World!
    - As an answer file, write a Bash script that configures a new Ubuntu machine to respect above requirements (this script will be run on the server itself)
    - You can’t use systemctl for restarting nginx

2. 2-setup_a_domain_name - Register a domain

3. Redirection
    Configure your Nginx server so that /redirect_me is redirecting to another page.

    **Requirements:**

    - The redirection must be a “301 Moved Permanently”
    - You answer file should be a Bash script containing commands to automatically configure a Ubuntu machine to respect above requirements
    - Using what you did with 1-install_nginx_web_server, write 3-redirection so that it configures a brand new Ubuntu machine to the requirements asked in this task

4. Not found page 404
    Configure your Nginx server to have a custom 404 page that contains the string Ceci n'est pas une page.

    **Requirements:**

    - The page must return an HTTP 404 error code
    - The page must contain the string Ceci n'est pas une page
    - Using what you did with 3-redirection, write 4-not_found_page_404 so that it configures a brand new Ubuntu machine to the requirements asked in this task

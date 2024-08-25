
# Configuration Management with Puppet

This repository contains Puppet manifests for performing various configuration management tasks. Each task is implemented in a separate `.pp` file.

## Tasks

### 0. Create a File
**File:** `0-create_a_file.pp`

Using Puppet, this manifest creates a file at `/tmp/school` with the following specifications:

- **File path:** `/tmp/school`
- **File permissions:** `0744`
- **Owner:** `www-data`
- **Group:** `www-data`
- **File content:** `I love Puppet`


### 1. Install a Package
**File:** `1-install_a_package.pp`

This manifest installs the Flask package using `pip3` with the specified version:

- **Package:** `Flask`
- **Version:** `2.1.0`

### 2. Execute a Command
**File:** `2-execute_a_command.pp`

This manifest kills a process named `killmenow` using the `exec` Puppet resource with `pkill`.

**Requirements:**

- **Exec resource:** Used to execute the `pkill` command.

## Repository Structure

- **GitHub repository:** `alx-system_engineering-devops`
- **Directory:** `0x0A-configuration_management`
  - `0-create_a_file.pp`
  - `1-install_a_package.pp`
  - `2-execute_a_command.pp`
  - `README.md`
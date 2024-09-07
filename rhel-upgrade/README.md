# RHEL Upgrade Playbooks (7 to 9)

## Overview
This repository contains Ansible playbooks to automate the upgrade of Red Hat Enterprise Linux (RHEL) from version 7 to 9. The playbooks include all necessary steps, including subscription registration, upgrade processes, and post-upgrade tasks.

## Playbooks
- **rhel-7-8-playbook.yml**: Upgrade from RHEL 7 to 8.
- **rhel-8-9-playbook.yml**: Upgrade from RHEL 8 to 9.
- **rhel-7-9-playbook.yml**: Complete upgrade from RHEL 7 to 9 in one go.

## Prerequisites
- Ansible installed on the control node.
- SSH access to all target hosts.
- Red Hat subscription.
- Backup your system before starting the upgrade.

## How to Use
1. Clone the repository:
    ```bash
    git clone https://github.com/mbeema/devops.git
    cd devops/rhel-upgrade
    ```

2. Run the playbook for your target upgrade:
    ```bash
    ansible-playbook -i inventory rhel-7-8-playbook.yml
    ```

    Or for full upgrade from RHEL 7 to 9:
    ```bash
    ansible-playbook -i inventory rhel-7-9-playbook.yml
    ```

## Variables
All variables are stored in `vars/rhel-vars.yml`, customize these as per your environment.

## License
This project is licensed under the MIT License.



DEV:

ansible-playbook -i inventory/dev.inv rhel-7-8-playbook.yml
Snapshot VM
ansible-playbook -i inventory/dev.inv rhel-8-9-playbook.yml




QA:

ansible-playbook -i inventory/qa.inv rhel-7-8-playbook.yml
Snapshot VM
ansible-playbook -i inventory/qa.inv rhel-8-9-playbook.yml




PROD:

ansible-playbook -i inventory/prod.inv rhel-7-8-playbook.yml
Snapshot VM
ansible-playbook -i inventory/prod.inv rhel-8-9-playbook.yml


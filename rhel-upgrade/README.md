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


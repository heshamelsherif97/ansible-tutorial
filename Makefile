build_docker:
	docker build -t centos_python:latest .

run_docker:
	docker run --name centos_python -itd -v $(pwd):/usr/src/app centos_python:latest
	docker exec -it centos_python crond

run_task:
	docker exec -it centos_python ansible-playbook /usr/src/app/ansible.yaml --extra-vars='{"packages": [$(packages)]}'

ssh_container:
	docker exec -it centos_python /bin/bash

Run
```
make build_docker
```
in order to build the docker image
Run
```
make run_docker
```
in order to start the docker container in daemon mode

Run
```
make run_task packages="httpd, python3-devel"
```
which to run ansible on the container you can add packages as you want

Use
```
make ssh_container
```
to ssh into the container and inspect /opt/ directory
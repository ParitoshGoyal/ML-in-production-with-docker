# Django Docker NGINX Gunicorn HuggingFace

## 1. Create executable build_dev.sh

Optional: Edit the `build_dev.sh` file and add sensible values there.

Add execution permissions:

```bash
$ chmod +x build_dev.sh
```

## 2. Build and deploy the Docker containers

Run `build_dev.sh`:

```bash
$ ./build_dev.sh
```

## 3. Check if the build was successful

If you now go to `http://0.0.0.0/` you should see a "Hello, World!" page there.


## 4. Overview of useful commands

### Rebuild docker containers

```bash
$ docker-compose down
$ ./build_dev.sh
```

### SSH to the Docker containers

```bash
$ docker exec -it django_docker_gunicorn_1 bash
$ docker exec -it django_docker_nginx_1 bash
$ docker exec -it django_docker_db_1 bash
```

### View logs

To view the logs, use docker desktop
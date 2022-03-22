ImageToTextNew

### Run project
Run `docker-compose up -d`

### Build & upload app2 image to Docker Hub

Run following commands  
- `docker build -f ./docker/app2/Dockerfile -t kevinc123/image-to-text-docker:1.0.0 .`
- `docker push  kevinc123/image-to-text-docker:1.0.0`

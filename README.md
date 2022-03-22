ImageToTextNew

### Run project
Run `docker-compose up -d`

Open `http://localhost:5000` or `http://imagetotext.docker`

(Second option only works if you have container as reverse proxy)

### Build & upload app2 image to Docker Hub

Run following commands  
- `docker build -f ./docker/app2/Dockerfile -t kevinc123/image-to-text-docker:1.0.0 .`
- `docker push  kevinc123/image-to-text-docker:1.0.0`

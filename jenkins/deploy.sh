scp -o StrictHostKeyChecking=no docker-compose.yaml swarm-master:
ssh swarm-master << EOF

export DATABASE_URI=${DATABASE_URI}
docker stack deploy --compose-file docker-compose.yaml app

EOF
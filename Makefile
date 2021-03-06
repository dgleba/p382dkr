
# shell in django
djsh:
	docker-compose run djangodev /bin/bash

# clean docker containers 
dkcl:   
	docker ps 
	docker ps -a
	docker images
	docker volume ls 
	# remove this one.. 
	-docker rmi dkr382django2t_djangodev 
	# remove docker containers exited 
	-docker rm $$(docker ps -qa --no-trunc --filter "status=exited") 
	# remove tagged <none> 
	-docker rmi $$(docker images | grep "^<none>" | awk '{ print $3 }') 

dkv: 
	docker --version
	docker-compose -version

# fix permissions. make them group writable so www-data group can manage the files. move, delete, etc..  
perm:
	docker-compose run djangodev sh docker/fixpermsh
  
# having trouble setting env variable, but do I need it?  
perm2:  
	docker-compose run djangodev \
	 bash -c export fold=/myproject; chmod -R g+rws,o-w  $${fold}




# https://github.com/docker/compose/issues/2033 docker compose command line run sh multiple commands in one line
# $ requires escaping with $, so, $$
# continuation card  \
# - dash in front of command ignores error. -rm -f *.o

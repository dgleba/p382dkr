# you can see in this file I have tried many methods to get umask 0002 so that group can manage the project files....


# Try to make all my containers based on debian stretch-slim - this may reuse software across the system
#
# FROM python:3.5-slim-stretch --  Command "python setup.py egg_info" failed with error code 1 in /tmp/pip-install-9vqvu1aa/mysqlclient/ _ Removing intermediate container 21eec6526e85 _ ERROR: Service 'djangodev' failed to build: The command '/bin/sh -c pip install -r requirements.txt' returned a non-zero code: 1
#
FROM python:3.5-stretch  

ENV PYTHONUNBUFFERED 1


#
# these had no effect..
# https://stackoverflow.com/questions/10220531/how-to-set-system-wide-umask
# https://unix.stackexchange.com/questions/83056/setting-umask-for-su-root
#
RUN echo "session optional pam_umask.so umask=002" >> /etc/pam.d/common-session
RUN echo "session optional pam_umask.so umask=002" >> /etc/pam.d/common-session-noninteractive
RUN echo "umask 0002" >> /etc/profile
RUN echo "umask 0002" >> /root/.bash_profile
RUN echo "umask 0002" >> /root/.profile
RUN echo "alias ll='ls -alF'" >> /root/.profile



# get some utilities..
RUN apt-get update && apt-get install -y \
  mc \
  --no-install-recommends && rm -r /var/lib/apt/lists/*

  
# project files folder
#
ENV fold=/myproject
ADD . ${fold}
WORKDIR ${fold}
#
# $fold permissions..
# this stuff works for most of it, but not django-admin.py.  Also I want something more system wide...
#
# make group writable to share file management with the www-data group. All in www-data group can manage these files.
#   RUN chgrp -hR www-data ${fold} ; chown -R www-data  ${fold}
# also set the group sticky bit, so that the group is set for new files created. chmod g+s /home/shared – jris198944 May 13 '14 at 8:43 
   RUN chmod -R g+rws,o-w  ${fold}
# make only folders +x so they can be cd into.
   RUN find ${fold} -type d -exec chmod g+x {} +


# RUN umask 0002 ; pip install -r requirements.txt
RUN pip install -r requirements.txt


# not sure this works..
COPY ./docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
# umask returns 0002 but running startproject sftp://albe@10.4.1.227/srv/dkr/dkr382django2t/myproject/settings.py was created without write on group. -rw-r--r-- 1 root www-data 2645 Aug 25 settings.py


# had no effect?
CMD umask 0002;

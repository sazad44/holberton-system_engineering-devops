# Fixing NGINX to accept more files
exec { 'Fix NGINX Failed Requests':
  command => "/bin/echo ULIMIT='-n 5000' | sudo tee /etc/default/nginx && sudo service nginx restart"
}

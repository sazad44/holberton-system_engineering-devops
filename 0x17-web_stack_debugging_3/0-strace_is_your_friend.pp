file { 'class-wp-locale.php':
  ensure => file,
  path   => '/var/www/html/wp-includes/class-wp-locale.php'
}

exec { 'fix-wordpress':
  command => ('/bin/sed -i "s/phpp/php/g" /var/www/html/wp-settings.php')
}

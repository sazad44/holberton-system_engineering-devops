# Providing fix for holberton user having too many files
exec { 'Fix holberton user too many files open':
  command => "/bin/sed -i 's/holberton.*//g' /etc/security/limits.conf"
}

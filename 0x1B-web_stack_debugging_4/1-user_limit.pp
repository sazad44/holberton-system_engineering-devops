# Providing fix for holberton user having too many files
exec { 'Fix holberton user too many files open':
     command => "sed -i 's/holberton.*//g"
}

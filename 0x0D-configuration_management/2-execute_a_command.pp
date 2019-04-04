# Executes a command to kill a process
exec { 'pkill killmenow':
path => ['/usr/bin']
}

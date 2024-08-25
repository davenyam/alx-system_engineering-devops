#create a manifest the kills a process named kill menow

exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}

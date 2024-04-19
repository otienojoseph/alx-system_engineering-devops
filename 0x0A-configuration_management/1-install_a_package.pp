# Install flask using puppet

exec { 'flask':
  command => 'pip3 install flask==2.1.0',
  path    => '/usr/bin/'
  }

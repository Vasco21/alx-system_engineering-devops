# install -U Flask -v 2.1.0
exec { 'Flask':
  command => '/usr/bin/apt-get -y install-U Flask -v 2.1.0',
}

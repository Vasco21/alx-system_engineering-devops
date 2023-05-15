# install Flask -v 2.1.0
exec { 'Flask':
  command => '/usr/bin/apt-get -y install Flask -v 2.1.0',
}

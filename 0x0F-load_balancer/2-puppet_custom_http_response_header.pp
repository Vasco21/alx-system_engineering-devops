class custom_header {
  package { 'nginx':
    ensure => installed,
  }

  file { '/etc/nginx/conf.d/custom-header.conf':
    content => 'add_header X-Served-By $hostname;',
    owner   => 'root',
    group   => 'root',
    mode    => '0644',
    require => Package['nginx'],
    notify  => Service['nginx'],
  }

  service { 'nginx':
    ensure  => running,
    enable  => true,
    require => Package['nginx'],
  }
}

include custom_header

#!/usr/bin/env bash
# Seting up my client config file

file { 'etc/ssh/ssh_config':
	ensure => present,

content =>"

	#SSH Client configuration
	host*
	IdentityFile ~/.ssh/school
	PasswordAuthentication no
	",

}

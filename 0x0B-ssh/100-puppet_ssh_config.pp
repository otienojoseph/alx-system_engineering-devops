# Configure ssh config to use ssh without being asked for password

file { '2-ssh_config': 
    path => '/home/optimus/alx_cscience/alx-system_engineering-devops/0x0B-ssh/2-ssh_config',
    ensure => 'file',
    content => "
        Host custom
            HostName 54.160.112.244
            User ubuntu
            PasswordAuthentication no
            IdentityFile ~/.ssh/school
    "
    }

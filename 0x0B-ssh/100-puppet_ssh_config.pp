# Configure ssh config to use ssh without being asked for password
$config_path = '/home/optimus/alx_cscience/alx-system_engineering-devops/0x0B-ssh/2-ssh_config'

file { '2-ssh_config':
    ensure  => file,
    path    => $config_path,
    mode    => '0644',
    content => "
    Host custom
        HostName 54.160.112.244
        User ubuntu
        IdentityFile ~/.ssh/school
        PasswordAuthentication no
    "
    }

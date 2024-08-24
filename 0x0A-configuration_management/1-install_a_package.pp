#install flask and pip with puppet

package { 'python3-pip':
  ensure   => '3.8.10',
  provider => 'pip3',
}

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  =>  Package['python3-pip'],
}

package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
  require  =>  Package['Flask'],
}

resource aws_launch_configuration "my-first-launch-conf" {
    name = "webserver-launch"
    image_id = "${var.ami}"
    instance_type = "${var.instance_type}"
    security_groups = ["${aws_security_group.webserver_sg.id}"]
    key_name = "${var.key_name}"
    user_data = <<-EOF
    #!/bin/bash -xe
    exec > >(tee /var/log/user-data.log|logger -t user-data -s 2>/dev/console) 2>&1 # logs everything executed in script to a file
    /usr/bin/apt-get update # update apt-get
    DEBIAN_FRONTEND=noninteractive /usr/bin/apt-get upgrade -yq # upgrade all packages in non-interactive way
    /usr/bin/apt-get install apache2 -y # install apache package
    /usr/sbin/ufw allow in "Apache Full" # provides Apache access to ec2 through firewall
    /bin/echo "Hello world " >/var/www/html/index.html # echo string to index.html
    instance_ip=$(curl https://checkip.amazonaws.com) # get IP address of ec2 instance
    echo $instance_ip >>/var/www/html/index.html # update index.html file with retrieved ip address for ec2
    EOF
}
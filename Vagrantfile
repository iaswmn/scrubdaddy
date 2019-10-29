# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.box = "binarydata/debian-jessie"
  config.vm.network :forwarded_port, guest: 8000, host: 8001
  config.vm.network :public_network, ip: "192.168.68.8"

  config.ssh.username = "vagrant"
  config.ssh.password = "vagrant"


  config.vm.provider "virtualbox" do |vb|
    vb.cpus = 2
    vb.memory = "1024"
  end

  config.vm.provision "shell", path: "VagrantScriptPost.shell"
end

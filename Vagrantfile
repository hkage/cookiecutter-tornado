Vagrant.configure(2) do |config|
    config.vm.box = "ubuntu/trusty64"
    config.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box"
    config.vm.network :forwarded_port, guest: 8000, host: 8000, id: "tornado"
    config.vm.synced_folder ".", "/home/vagrant"
    config.vm.provision :shell, :path => "bootstrap.sh"
end

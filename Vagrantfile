Vagrant::Config.run do |config|
    config.vm.box = "ubuntu/trusty64"
    config.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box"
    config.vm.network :hostonly, "172.19.1.8"
    config.vm.network "forwarded_port", guest: 80, host: 8888
    config.vm.share_folder("tornado", "/tornado", ".", :nfs=> true)
    config.vm.provision :shell, :path => "bootstrap.sh"
end

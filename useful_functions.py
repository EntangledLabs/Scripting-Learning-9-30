import os, subprocess

# ======================
# Helper classes
# ======================

# Recursive chmod
class chmod():
    @classmethod
    def chmod_rec(cls, path, mode):
        for dirpath, dirnames, filenames in os.walk(path):
            os.chmod(dirpath, mode)
            for filename in filenames:
                os.chmod(os.path.join(dirpath, filename), mode)

# Wrapper for APT calls
class apt():
    @classmethod
    def install(cls, package):
        subprocess.call('apt install {} -y'.format(package), shell=True)

    @classmethod
    def remove(cls, package):
        subprocess.call('apt remove {} -y'.format(package), shell=True)
        subprocess.call('apt purge {} -y'.format(package), shell=True)

    @classmethod
    def autoremove(cls):
        subprocess.call('apt autoremove -y', shell=True)

    @classmethod
    def update(cls):
        subprocess.call('apt update', shell=True)

    @classmethod
    def upgrade(cls):
        subprocess.call('apt upgrade -y', shell=True)

    @classmethod
    def add_source(cls, repo):
        cls.install('software-properties-common')
        subprocess.call('add-apt-repository {} -y'.format(repo), shell=True)

# Wrapper for UFW calls
class ufw():
    @classmethod
    def enable(cls):
        subprocess.call('ufw enable', shell=True)

    @classmethod
    def reset(cls):
        subprocess.call('ufw --force reset', shell=True)

    @classmethod
    def defaults(cls):
        subprocess.call('ufw default deny incoming', shell=True)
        subprocess.call('ufw default allow outgoing', shell=True)

    @classmethod
    def add(cls, port):
        subprocess.call('ufw allow {}'.format(port), shell=True)

# Wrapper for systemctl calls
class systemctl():
    @classmethod
    def enable(cls, service):
        subprocess.call('systemctl enable {}'.format(service), shell=True)

    @classmethod
    def start(cls, service):
        subprocess.call('systemctl start {}'.format(service), shell=True)

    @classmethod
    def stop(cls, service):
        subprocess.call('systemctl stop {}'.format(service), shell=True)

    @classmethod
    def restart(cls, service):
        subprocess.call('systemctl restart {}'.format(service), shell=True)

    @classmethod
    def reload(cls, service):
        subprocess.call('systemctl reload {}'.format(service), shell=True)

from conans import ConanFile, RunEnvironment
from conans import tools

class LinuxHeadersConan(ConanFile):
    name = "linux-headers"
    version = "5.4.94"
    settings = "arch"
    url = "https://github.com/roarbr/conan-linux-headers"
    homepage = "https://www.kernel.org/"
    description = """Conan package for linux kernel headers.
                     For packages that need access to kernel headers and not the full kernel source """
    license = "Apache-2.0"

    exports_sources = "source/*"
    no_copy_source = True
    # linux_stable = "git://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git"
    linux_stable = "/home/roar/git/linux"

    def source(self):
        print("source(): Git clone " + self.linux_stable + ". Tag/branch: v" + self.version)
        git = tools.Git()
        git.clone(self.linux_stable, branch="v" + self.version, shallow=True)

    def build(self):
        print('build(): arch: ' + str(self.settings.get_safe("arch")))
        print("package_folder: " + str(self.package_folder))
        with tools.chdir(self.source_folder):
            self.run("echo Building linux headers")
            if self.settings.arch == "x86_64":
                print("Build ARCH=x86_64 headers_install")
                self.run("make headers_install ARCH=x86_64 INSTALL_HDR_PATH=" + self.package_folder)
            elif self.settings.arch == "armv8":
                print("Build ARCH=arm64 headers_install")
                self.run("make headers_install ARCH=arm64 INSTALL_HDR_PATH=" + self.package_folder)
            elif "arm" in self.settings.arch:
                print("Build ARCH=arm headers_install")
                self.run("make headers_install ARCH=arm INSTALL_HDR_PATH=" + self.package_folder)

    def package(self):
        print("package()")
#        self.copy("*app", dst="bin", keep_path=False)
#        self.copy("*app.exe", dst="bin", keep_path=False)

    def deploy(self):
        print("deploy()")
#        self.copy("*", src="bin", dst="bin")


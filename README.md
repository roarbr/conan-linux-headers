# conan-linux-headers
Conan package for linux kernel headers. For packages that need access to kernel
headers and not the full kernel source.

# Architecture mapping
The linux-headers can be build for any platform supported by the linux kernel.
This is performed by conan setting **arch** that is translated into
linux kbuild **ARCH=** setting.

For instance the conan arch=armv8 means 64-bit ARM, translated to ARCH=arm64 for kbuild.

Older ARM versions like armv6 is means ARCH=arm (32-bit ARM).
This build script assumes all other arm settings than armv8 means ARCH=arm.

Other platforms are used from conan **arch** to kbuild **ARCH** unmodified. Only 'x86_64' is tested apart from 'arm'.

# Build
The package clone git tag from kernel git stable.

Build examples:
* conan create . -k -s arch=x86_64
* conan create . -k -s arch=armv6
* conan create . -k -s arch=armv8

The flag '-k' is to keep the cloned source to avvoid git clone of the kernel source for each build. The kernel source is not
included in the package, only the headerfiles under the directory 'include/' after the command:

`make headers_install ARCH=<arch> INSTALL_HDR_PATH=<package directory>`

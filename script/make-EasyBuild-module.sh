#!/usr/bin/env bash

# Stop in case of error
set -e

# Print the content of the module
print_devel_module()
{
cat <<EOF
#%Module

proc ModulesHelp { } {
    puts stderr {   EasyBuild is a software build and installation framework
written in Python that allows you to install software in a structured,
repeatable and robust way. - Homepage: http://hpcugent.github.com/easybuild/

This module provides the development version of EasyBuild.
}
}

module-whatis {EasyBuild is a software build and installation framework
written in Python that allows you to install software in a structured,
repeatable and robust way. - Homepage: http://hpcugent.github.com/easybuild/

This module provides the development version of EasyBuild.
}

set root    "${INSTALL_DIR}"

conflict    EasyBuild

prepend-path    PATH            "\$root/easybuild-framework"

prepend-path    PYTHONPATH      "\$root/vsc-base/lib"
prepend-path    PYTHONPATH      "\$root/easybuild-framework"
prepend-path    PYTHONPATH      "\$root/easybuild-easyblocks"
prepend-path    PYTHONPATH      "\$root/easybuild-easyconfigs"

EOF
}

# Read parameters
INSTALL_DIR="$1"

cd "${INSTALL_DIR}"
INSTALL_DIR="${PWD}" # get the full path

# Create the module file
EB_DEVEL_MODULE_NAME="EasyBuild-develop"
EB_DEVEL_MODULE="${INSTALL_DIR}/eb-module/${EB_DEVEL_MODULE_NAME}"
print_devel_module > "${EB_DEVEL_MODULE}"

exit 0



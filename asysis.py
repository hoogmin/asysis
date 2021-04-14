"""
Asysis: Another system information script

A simple program to display information about your computer/machine to
your terminal/command-line.
"""

# SPDX-License-Identifier: BSD-3-Clause
# BSD 3-Clause License
#
# Copyright (c) 2021, Javier Martinez
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import platform
import getpass
import socket
import multiprocessing

def get_sys_username():
    return getpass.getuser()

def get_sys_hostname():
    return socket.gethostname()

def get_os():
    os_name = platform.system()
    if os_name == "Linux":
        return "GNU/Linux"
    else:
        return os_name

def get_sys_kernel():
    if platform.system() == "Windows":
        return platform.version()

    # version will yield a different value on Linux, so release is used
    return platform.release()

def get_machine_type():
    return platform.machine()

def get_cpu_type():
    processor_type = platform.processor()

    if processor_type == "":
        return "Cannot be determined (System does not provide this info)"
    
    return processor_type

def get_num_cpus():
    return multiprocessing.cpu_count()

def get_python_ver():
    return platform.python_version()

def get_python_impl():
    return platform.python_implementation()

# A dictionary for storing processed system info
sysinfo = {
    "username": get_sys_username(),
    "hostname": get_sys_hostname(),
    "os": get_os(),
    "kernel": get_sys_kernel(),
    "machine_type": get_machine_type(),
    "processor_type": get_cpu_type(),
    "num_cpus": get_num_cpus(),
    "python_ver": get_python_ver(),
    "python_impl": get_python_impl()
}

def display_info_full():
    print("") # for newline
    print("{user}@{host}".format(user=sysinfo["username"], host=sysinfo["hostname"]))
    print("")
    print("OS: {}".format(sysinfo["os"]))
    print("Host: {}".format(sysinfo["hostname"]))
    print("Kernel: {}".format(sysinfo["kernel"]))
    print("Architecture: {}".format(sysinfo["machine_type"]))
    print("CPU: {}".format(sysinfo["processor_type"]))
    print("Number of CPUs: {}".format(sysinfo["num_cpus"]))
    print("Runtime Version: {} ({})".format(sysinfo["python_ver"], sysinfo["python_impl"]))



display_info_full()

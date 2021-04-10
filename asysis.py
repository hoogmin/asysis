"""
Asysis: Another system information script

A simple program to display information about your computer/machine to
your terminal/command-line.
"""

# SPDX-License-Identifier: BSD-3-Clause
# Copyright (c) 2021, Javier Martinez
# You should have received a copy of the
# BSD license along with this software.
# If not, see <https://opensource.org/licenses/BSD-3-Clause>
# for license details.

import platform
import getpass
import socket
import multiprocessing

def get_sys_username():
    return getpass.getuser()

def get_sys_hostname():
    return socket.gethostname()

def get_os():
    return "{} {}".format(platform.system(), platform.release())

def get_sys_kernel():
    return platform.version()

def get_machine_type():
    return platform.machine()

def get_cpu_type():
    return platform.processor()

def get_num_cpus():
    return multiprocessing.cpu_count()

# A dictionary for storing processed system info
sysinfo = {
    "username": get_sys_username(),
    "hostname": get_sys_hostname(),
    "os": get_os(),
    "kernel": get_sys_kernel(),
    "machine_type": get_machine_type(),
    "processor_type": get_cpu_type(),
    "num_cpus": get_num_cpus()
}

def display_info_full():
    print("") # for newline
    print("{user}@{host}".format(user=sysinfo["username"], host=sysinfo["hostname"]))
    print("")
    print("OS: {}".format(sysinfo["os"]))
    print("Host: {}".format(sysinfo["hostname"]))
    print("Kernel: {}".format(sysinfo["kernel"]))
    print("Architecture: {}".format(sysinfo["machine_type"]))
    print("Processor Type: {}".format(sysinfo["processor_type"]))
    print("Number of CPUs: {}".format(sysinfo["num_cpus"]))



display_info_full()

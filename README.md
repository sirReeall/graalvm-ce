graalvm-ce
=========

This role will install [GraalVM Community Edition](https://www.graalvm.org/) via Ansiable on Centos 7.

The precomplied binaries are pulled from [GraalVM's GitHub Releases Page](https://github.com/graalvm/graalvm-ce-builds/releases).

Requirements
------------

Graalvm contains everything needed to start developing (including a JRE).

You will need to make sure that phsical location defined for graalvm_install_location is empty or this role will fail.

Role Variables
--------------

Name | Default | Description
--- | --- | ---
graalvm_version | `latest` | (TODO) The version to be downloaded and installed
graalvm_install_location | `/opt` | The location where graalvm should be installed.
graalvm_java_version | `8` | The Java version used by Graalvm, currently only supports values 8 or 11
graalvm_set_java_home | `true` | set to false if you do not want to set JAVA_HOME to the newly installed GraalVM

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: graalvm-ce}

License
-------

MIT
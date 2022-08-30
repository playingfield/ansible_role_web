nginx
=========

A brief description of the role goes here.

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto3 python libray is required.

It is good practice to create a file named `requirements.txt` for python libraries.

Role Variables
--------------

A description of the settable variables for this role should go here, including any variables that are in `defaults/main.yml`, `vars/main.yml`, and any variables that can/should be set via parameters to the role.
Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

Dependencies
------------

A list of other roles should go here, plus any details in regards to
parameters that may need to be set for other roles, or variables that are used from other roles.
Dependencies on other roles can be stated in `meta/main.yml` (hard) or `requirements.yml` (loose).

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```yaml
    - hosts: servers
      roles:
         - role: username.rolename
           the_var: 42
```

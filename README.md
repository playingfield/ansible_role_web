ansible_role_web
=========

A role to install a web server like httpd or nginx.

Requirements
------------

Linux.

Role Variables
--------------

`package` either 'httpd' or 'nginx'.
`service` same as package most of the time.

Dependencies
------------

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```yaml
    - hosts: web
      roles:
         - role: playingfield.ansible_role_web
```

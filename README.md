ansible_role_web
=========

A role to install a web server like **httpd** (aka Apache) or **Nginx**.

Requirements
------------

Linux.

Role Variables
--------------

```yml
# defaults
desired_state: present  # or absent
package: nginx  # or httpd
service: nginx  # or httpd
webroot: /usr/share/nginx/html  # or /var/www/html
```

Dependencies
------------
None.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```yaml
    - hosts: web
      roles:
         - role: playingfield.ansible_role_web
```

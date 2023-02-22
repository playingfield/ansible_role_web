ansible_role_web
=========

A role to install a web server like **httpd** (aka Apache) or **Nginx**.

Codespace
---------
This example can be run in a browser-based codespace. Click 'Use this template' and select 'Open in a codespace'.
After the codespace is started and extensions installed. Select the terminal panel and type: `molecule converge`.
Once that's finished you can browse the Molecule Introduction at [http://localhost:8000/](http://localhost:8000/).

Requirements
------------

Linux.

Role Variables
--------------

```yml
# defaults
desired_state: present  # or absent
verify_state: false  # or true
package: nginx  # or httpd
service: nginx  # or httpd
webroot: /usr/share/nginx/html  # or /var/www/html
webrepo: 'https://github.com/playingfield/molecule_intro.git'
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

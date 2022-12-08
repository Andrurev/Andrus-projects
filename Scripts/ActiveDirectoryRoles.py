# Import the required libraries
import ldap3

# Set the AD server and credentials
server = "ad.example.com"
user = "admin"
password = "password"

# Connect to the AD server
conn = ldap3.Connection(server, user, password)
conn.bind()

# Set the user and role DNs
user_dn = "cn=John Smith,ou=Users,dc=ad,dc=example,dc=com"
role_dn = "cn=Administrators,cn=Builtin,dc=ad,dc=example,dc=com"

# Add the user to the role
conn.modify(user_dn, {"memberOf": [(ldap3.MODIFY_ADD, [role_dn])]})

# Check the user's roles
response = conn.search(user_dn, "(objectClass=*)", attributes=["memberOf"])
if response:
    user = response[0]
    if "memberOf" in user:
        print("User is a member of the following roles:")
        for role in user["memberOf"]:
            print(role)

# Disconnect from the AD server
conn.unbind()

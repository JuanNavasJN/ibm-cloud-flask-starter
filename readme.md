### Install ibmcloud cli

https://cloud.ibm.com/docs/cli?topic=cli-install-ibmcloud-cli

```sh
ibmcloud login
ibmcloud cf install # install cloud foundry cli
ibmcloud target --cf
ibmcloud cf push

# to create organization
ibmcloud account org-create <organization_name>
ibmcloud account orgs  # list organizations


#extra
ibmcloud target -r <region> # change region
```

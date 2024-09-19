# Containers-VMs
As part of my Enterprise Software Platforms course, I implemented a Contact Management System webapp to explore deployments to Containers &amp; Virtual Machines.

The two folders contain mostly the same content. The only differences are:
1. The vm folder contains a Vagrantfile to deploy the code to a virtual machine, whereas the docker folder contains a Dockerfile to deploy the code to a container.
2. The requirements.txt have minor differences because I was unable to use the same in both the environments. Will explore if it is possible to make the same and merge the folders.

It is a simple Contact Management System web application, which allows users to add a contact, edit their details, and delete it. An additional feature is the /gc-stats webpage which displays the garbage collection stats for the application.

For my observations on the Containers vs VMs performance, check the PDF report attached.